#!/usr/bin/env python3
"""檔案依副檔名自動分類到資料夾的 CLI"""
from __future__ import annotations
import argparse, shutil
from pathlib import Path

def main() -> None:
    p = argparse.ArgumentParser(description='檔案依副檔名自動分類到資料夾的 CLI')
    p.add_argument("dir", type=Path)
    p.add_argument("--apply", action="store_true", help="真的移動；預設只預覽")
    args = p.parse_args()
    for f in sorted(args.dir.iterdir()):
        if not f.is_file():
            continue
        ext = (f.suffix[1:] or "noext").lower()
        dest_dir = args.dir / ext
        dest = dest_dir / f.name
        print(f"{f.name} -> {ext}/{f.name}")
        if args.apply:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(f), str(dest))

if __name__ == "__main__":
    main()
