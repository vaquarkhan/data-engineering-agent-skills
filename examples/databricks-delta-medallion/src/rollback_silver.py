import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    snapshot = Path(args.snapshot)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(snapshot, output)
    print(f"Restored silver output from snapshot {snapshot} into {output}.")


if __name__ == "__main__":
    main()
