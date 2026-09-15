# Image Width Sorter

An app that automatically splits manga page images into two folders based on their pixel width.

## Purpose

In many manga scans, some pages are **single-page** while others are **double-page spreads**. This inconsistency slows down and reduces the accuracy of later processing steps, such as **image upscaling**, since upscaling tools usually work better when their input images have more consistent dimensions.

This app solves that by checking the **pixel width** of each image and automatically sorting them into two categories, making subsequent processing (like upscaling) faster and more organized.

## How It Works

1. The user provides a folder containing manga images to the app.
2. The app automatically creates two new folders inside that same path:
   - `1` → for images with a width **less than 1800 pixels** (single pages)
   - `2` → for images with a width **greater than 1800 pixels** (double-page spreads)
3. Every image is checked by width and **moved (cut)** into the corresponding folder — meaning the original file is removed from its source path and relocated, not copied.

### Sorting Criteria

| Image Width | Destination |
|---|---|
| Less than 1800 pixels | Folder `1` |
| Greater than 1800 pixels | Folder `2` |

## Libraries Used

- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) — for a modern graphical user interface
- [`tkinterdnd2`](https://github.com/pmgagne/tkinterdnd2) — for drag-and-drop support
- [`Pillow`](https://python-pillow.org/) — for reading images and extracting their dimensions

## Installation

```bash
pip install customtkinter tkinterdnd2 Pillow
```

## Usage

1. Run the app.
2. Select the folder containing your manga images, or drag and drop it into the app.
3. The app automatically sorts and moves the images.
4. Once finished, the images can be found split between the `1` and `2` folders inside the original input path.

## Note

Since images are moved (cut) rather than copied, the original files are removed from the source folder and relocated to the destination folders. It's recommended to back up your images before running the app.