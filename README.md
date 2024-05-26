## Angelina's Notepad and Maker USB

This repository contains two open-source applications created by Angelina Botez:

* **Notepad:** A text editor built with PyQt5.
* **Maker USB:** A USB drive formatter for creating bootable drives using `dd`. (Uses PyQt5 and psutil)

## Features

**Notepad**

* Create, open, save, and edit text files
* Basic text editing functionalities (undo, redo, cut, copy, paste, delete, find, replace, select all)
* Zoom in and out
* Displays version and license information in an "About" dialog

**Maker USB**

* Select ISO file and USB drive
* Creates bootable USB drives using `dd`
* Displays version and license information in an "About" dialog

## Getting Started

### Prerequisites

You'll need Python 3 and Git installed on your system.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AngelinaUk/angelinaproject.git
   cd angelinaproject
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install pyqt5 psutil
   ```

### Running the Applications

#### Notepad

```bash
python3 notepad.py
```

#### Maker USB

```bash
python3 makerusb.py
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## About

- Created by Angelina Botez
- Version 1.0
