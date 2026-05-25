package com.vaquarkhan.dataengineeringskills

import com.intellij.openapi.actionSystem.AnAction
import com.intellij.openapi.actionSystem.AnActionEvent
import com.intellij.openapi.application.ApplicationManager
import com.intellij.openapi.progress.ProgressIndicator
import com.intellij.openapi.progress.Task
import com.intellij.openapi.project.Project
import com.intellij.openapi.ui.Messages
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.nio.charset.StandardCharsets
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.StandardOpenOption

abstract class BaseInstallAction : AnAction() {
    protected fun requireProjectRoot(project: Project?): Path? {
        val basePath = project?.basePath
        if (basePath.isNullOrBlank()) {
            Messages.showErrorDialog("Open a project before installing the skill pack.", "Data Engineering Agent Skills")
            return null
        }
        return Path.of(basePath)
    }

    protected fun chooseOption(project: Project?, title: String, values: List<String>): String? {
        val selectedIndex = Messages.showChooseDialog(
            project,
            "Select an option:",
            title,
            null,
            values.toTypedArray(),
            values.firstOrNull()
        )
        return if (selectedIndex >= 0) values[selectedIndex] else null
    }

    protected fun install(project: Project, workspaceRoot: Path, files: List<String>, label: String) {
        val collisions = files.filter { Files.exists(workspaceRoot.resolve(it)) }
        val overwrite = if (collisions.isNotEmpty()) {
            val result = Messages.showYesNoCancelDialog(
                project,
                "${collisions.size} file(s) already exist for $label. Overwrite them?",
                "Data Engineering Agent Skills",
                "Overwrite",
                "Skip Existing",
                "Cancel",
                null
            )
            when (result) {
                Messages.YES -> true
                Messages.NO -> false
                else -> return
            }
        } else {
            false
        }

        object : Task.Backgroundable(project, "Installing $label", false) {
            override fun run(indicator: ProgressIndicator) {
                val client = HttpClient.newBuilder().build()
                var installed = 0
                var skipped = 0

                files.forEachIndexed { index, relativePath ->
                    indicator.fraction = (index + 1).toDouble() / files.size.toDouble()
                    indicator.text = "Installing $relativePath"

                    val target = workspaceRoot.resolve(relativePath)
                    if (Files.exists(target) && !overwrite) {
                        skipped += 1
                        return@forEachIndexed
                    }

                    val content = fetchText(client, relativePath)
                    Files.createDirectories(target.parent)
                    Files.writeString(
                        target,
                        content,
                        StandardCharsets.UTF_8,
                        StandardOpenOption.CREATE,
                        StandardOpenOption.TRUNCATE_EXISTING,
                        StandardOpenOption.WRITE
                    )
                    installed += 1
                }

                ApplicationManager.getApplication().invokeLater {
                    Messages.showInfoMessage(
                        project,
                        "Installed $installed file(s) for $label.${if (skipped > 0) " Skipped $skipped existing file(s)." else ""}",
                        "Data Engineering Agent Skills"
                    )
                }
            }
        }.queue()
    }

    private fun fetchText(client: HttpClient, relativePath: String): String {
        val normalized = relativePath.replace("\\", "/")
        val url = "${InstallerData.RAW_BASE_URL}/$normalized"
        val request = HttpRequest.newBuilder(URI.create(url)).GET().build()
        val response = client.send(request, HttpResponse.BodyHandlers.ofString())
        if (response.statusCode() != 200) {
            error("Failed to download $relativePath from $url (${response.statusCode()})")
        }
        return response.body()
    }
}

class InstallFullToolkitAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val root = requireProjectRoot(e.project) ?: return
        val files = (
            InstallerData.coreFiles +
                InstallerData.agentAdapters.values.flatten() +
                InstallerData.starterPacks.values.flatten() +
                InstallerData.mcpTemplates.values.flatten() +
                listOf("mcp/README.md")
            ).distinct()
        install(e.project!!, root, files, "full toolkit")
    }
}

class InstallCorePackAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val root = requireProjectRoot(e.project) ?: return
        install(e.project!!, root, InstallerData.coreFiles, "core pack")
    }
}

class InstallAgentAdaptersAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val root = requireProjectRoot(project) ?: return
        val options = InstallerData.agentAdapters.keys.toList() + "All"
        val choice = chooseOption(project, "Install Agent Adapters", options) ?: return
        val files = if (choice == "All") InstallerData.agentAdapters.values.flatten().distinct() else InstallerData.agentAdapters[choice].orEmpty()
        install(project, root, files, "$choice adapters")
    }
}

class InstallStarterPackAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val root = requireProjectRoot(project) ?: return
        val choice = chooseOption(project, "Install Starter Pack", InstallerData.starterPacks.keys.toList()) ?: return
        install(project, root, InstallerData.starterPacks[choice].orEmpty(), "$choice starter pack")
    }
}

class InstallMcpTemplatesAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val root = requireProjectRoot(project) ?: return
        val options = InstallerData.mcpTemplates.keys.toList() + "All"
        val choice = chooseOption(project, "Install MCP Templates", options) ?: return
        val files = if (choice == "All") {
            (listOf("mcp/README.md") + InstallerData.mcpTemplates.values.flatten()).distinct()
        } else {
            listOf("mcp/README.md") + InstallerData.mcpTemplates[choice].orEmpty()
        }
        install(project, root, files, "$choice MCP templates")
    }
}

class ScaffoldRunnableExampleAction : BaseInstallAction() {
    override fun actionPerformed(e: AnActionEvent) {
        val project = e.project ?: return
        val root = requireProjectRoot(project) ?: return
        val choice = chooseOption(project, "Scaffold Runnable Example", InstallerData.runnableExamples.keys.toList()) ?: return
        install(project, root, InstallerData.runnableExamples[choice].orEmpty(), "$choice example")
    }
}
