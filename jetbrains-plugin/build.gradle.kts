plugins {
    kotlin("jvm") version "1.9.24"
    id("org.jetbrains.intellij") version "1.17.4"
}

group = providers.gradleProperty("pluginGroup").get()
version = providers.gradleProperty("pluginVersion").get()

repositories {
    mavenCentral()
}

intellij {
    version.set(providers.gradleProperty("platformVersion"))
    type.set(providers.gradleProperty("platformType"))
}

tasks {
    patchPluginXml {
        version.set(providers.gradleProperty("pluginVersion"))
        sinceBuild.set("241")
        untilBuild.set("")
    }

    withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
        kotlinOptions.jvmTarget = "17"
    }
}

kotlin {
    jvmToolchain(17)
}
