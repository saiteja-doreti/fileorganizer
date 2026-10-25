"""File Organizer: sorts files in a folder into subfolders by type.

Usage:
    python organizer.py <folder>             # organize files
    python organizer.py <folder> --dry-run   # preview only, move nothing
"""
import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".aac", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".java", ".js", ".html", ".css", ".json"},
}


def category_for(path: Path) -> str:
    """Return the category name for a file based on its extension."""
    ext = path.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return "Others"


def unique_target(target: Path) -> Path:
    """Add a number to the file name if it already exists, so nothing is overwritten."""
    counter = 1
    new_target = target
    while new_target.exists():
        new_target = target.with_name(f"{target.stem}_{counter}{target.suffix}")
        counter += 1
    return new_target


def organize(folder: Path, dry_run: bool = False) -> dict:
    """Move files into category folders. Returns a count per category."""
    counts = {}
    for item in sorted(folder.iterdir()):
        if not item.is_file():
            continue
        category = category_for(item)
        destination = folder / category
        target = unique_target(destination / item.name)
        print(f"{'[preview] ' if dry_run else ''}{item.name} -> {category}/")
        if not dry_run:
            destination.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
        counts[category] = counts.get(category, 0) + 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument("folder", type=Path, help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")
    args = parser.parse_args()

    if not args.folder.is_dir():
        raise SystemExit(f"Error: '{args.folder}' is not a folder.")

    counts = organize(args.folder, args.dry_run)
    total = sum(counts.values())
    print(f"\nDone. {total} file(s) {'would be ' if args.dry_run else ''}organized.")
    for name, n in sorted(counts.items()):
        print(f"  {name}: {n}")


if __name__ == "__main__":
    main()
