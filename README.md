## Angelina's Utilities Collection

This repository contains open-source applications and utilities created by Angelina Botez:

* **Notepad:** A text editor built with PyQt5.
* **Maker USB:** A USB drive formatter for creating bootable drives using `dd`. (Uses PyQt5 and psutil)
* **System Info:** A command-line utility written in C that displays comprehensive system information.

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

**System Info**

* Displays operating system information (name, version, kernel, architecture)
* Shows CPU model and core count
* Reports memory usage (RAM and swap)
* Shows system uptime and process count
* Displays current user information
* Shows disk usage for mounted filesystems
* Command-line options for help and version information

## Getting Started

### Prerequisites

**For Python applications (Notepad and Maker USB):**
- Python 3
- Git

**For System Info utility:**
- GCC compiler (or any C compiler)
- Make (optional, for easier compilation)

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

#### System Info

First, compile the program:

```bash
make
```

Or compile manually:

```bash
gcc -Wall -Wextra -O2 -o sysinfo sysinfo.c
```

Then run it:

```bash
./sysinfo
```

To see available options:

```bash
./sysinfo --help
```

To install system-wide (optional, requires sudo):

```bash
sudo make install
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## About

- Created by Angelina Botez
- Version 1.0
