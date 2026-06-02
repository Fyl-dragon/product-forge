#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_skill(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the local ProductForge skill pack into ~/.codex/skills.")
    parser.add_argument("--source", default="skills", help="Local skill-pack directory.")
    parser.add_argument("--target", default=str(Path.home() / ".codex" / "skills"), help="Codex skills directory.")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    target = Path(args.target).expanduser().resolve()

    if not source.exists():
        raise SystemExit(f"Source skill pack not found: {source}")

    target.mkdir(parents=True, exist_ok=True)
    for skill_dir in sorted(path for path in source.iterdir() if path.is_dir()):
        copy_skill(skill_dir, target / skill_dir.name)
        print(f"Installed {skill_dir.name} -> {target / skill_dir.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
