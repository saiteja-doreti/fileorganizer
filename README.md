# File Organizer

A Python command-line tool that cleans up a messy folder by sorting files into subfolders (Images, Documents, Videos, Audio, Archives, Code, Others).

## Features
- Sorts files by extension
- `--dry-run` mode to preview changes safely
- Never overwrites files: duplicates get a number added (`photo_1.jpg`)
- Pure Python, no extra packages needed

## Requirements
Python 3.8 or newer

## Usage
```bash
# Preview first
python organizer.py "C:/Users/you/Downloads" --dry-run

# Then organize
python organizer.py "C:/Users/you/Downloads"
```

## Example output
```
photo.jpg -> Images/
resume.pdf -> Documents/
song.mp3 -> Audio/

Done. 3 file(s) organized.
```

## Customize
Add or change file types in the `CATEGORIES` dictionary at the top of `organizer.py`.

## What I learned
File handling with `pathlib` and `shutil`, command-line arguments with `argparse`, and safe file operations.
