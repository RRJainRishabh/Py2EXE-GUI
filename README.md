# Py2EXE GUI

**Py2EXE GUI** is a minimal, user-friendly tool that lets you convert Python `.py` scripts into `.exe` files on Windows using a graphical interface.

## 🚀 Features

- 🔍 Browse and select any Python script
- ⚙️ Instantly convert it to a standalone `.exe` using PyInstaller
- ✅ No terminal knowledge required
- 🖱️ GUI built with `tkinter`
- 🧳 Outputs are stored in a clean `dist/` folder

## 📦 Download

👉 [Download latest EXE](https://github.com/RRJainRishabh/py2exe-gui/releases/latest)

> No Python installation required to run the `.exe` itself (as long as it was compiled with `--onefile`).

## 🛠️ Requirements for Source Build

If you want to run the `.py` version or compile it yourself:

```bash
pip install pyinstaller
python gui_exe_converter.py