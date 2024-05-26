import sys
import os
import subprocess
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QMenuBar, QAction, QComboBox

# Set the Qt platform plugin path
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/usr/lib/x86_64-linux-gnu/qt5/plugins"

class MakerUSB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Menu bar
        self.menuBar = QMenuBar(self)
        fileMenu = self.menuBar.addMenu("File")
        
        openIsoAction = QAction("Open ISO", self)
        openIsoAction.triggered.connect(self.showFileDialog)
        fileMenu.addAction(openIsoAction)

        aboutMenu = self.menuBar.addMenu("About")
        
        aboutAction = QAction("About Maker USB", self)
        aboutAction.triggered.connect(self.showAbout)
        aboutMenu.addAction(aboutAction)
        
        layout.setMenuBar(self.menuBar)

        # Main layout
        self.selectFileLabel = QLabel("No ISO file selected", self)
        layout.addWidget(self.selectFileLabel)

        self.selectFileButton = QPushButton("Select ISO File", self)
        self.selectFileButton.clicked.connect(self.showFileDialog)
        layout.addWidget(self.selectFileButton)

        self.selectUsbDriveLabel = QLabel("No USB drive selected", self)
        layout.addWidget(self.selectUsbDriveLabel)

        self.usbDriveComboBox = QComboBox(self)
        self.updateUsbDriveList()
        layout.addWidget(self.usbDriveComboBox)

        self.selectHardDriveLabel = QLabel("No hard drive selected", self)
        layout.addWidget(self.selectHardDriveLabel)

        self.hardDriveComboBox = QComboBox(self)
        self.updateHardDriveList()
        layout.addWidget(self.hardDriveComboBox)

        self.startButton = QPushButton("Create Bootable USB", self)
        self.startButton.clicked.connect(self.createBootableUSB)
        layout.addWidget(self.startButton)

        self.setLayout(layout)
        self.setWindowTitle('Maker USB')
        self.show()

    def showFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Select ISO File", "", "ISO Files (*.iso);;All Files (*)", options=options)
        if fileName:
            self.selectFileLabel.setText(fileName)
            self.isoFile = fileName

    def updateUsbDriveList(self):
        self.usbDriveComboBox.clear()
        usb_drives = self.get_removable_drives()
        self.usbDriveComboBox.addItems(usb_drives)

    def updateHardDriveList(self):
        self.hardDriveComboBox.clear()
        hard_drives = self.get_hard_drives()
        self.hardDriveComboBox.addItems(hard_drives)

    def get_removable_drives(self):
        drives = []
        for disk in psutil.disk_partitions(all=True):
            if 'removable' in disk.opts and '/dev/sd' in disk.device:
                drives.append(disk.device)
        return drives

    def get_hard_drives(self):
        drives = []
        for disk in psutil.disk_partitions(all=True):
            if 'removable' not in disk.opts and ('/dev/sd' in disk.device or '/dev/nvme' in disk.device):
                drives.append(disk.device)
        return drives

    def createBootableUSB(self):
        try:
            if not hasattr(self, 'isoFile'):
                QMessageBox.warning(self, "Error", "Please select an ISO file")
                return

            usbDrive = self.usbDriveComboBox.currentText()
            if not usbDrive:
                QMessageBox.warning(self, "Error", "Please select a USB drive")
                return

            # Example command to create bootable USB using 'dd'
            command = f"sudo dd if={self.isoFile} of={usbDrive} bs=4M status=progress && sync"
            result = subprocess.run(command, shell=True, check=True)

            QMessageBox.information(self, "Success", "Bootable USB created successfully!")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to create bootable USB: {e}")

    def showAbout(self):
        about_text = (
            "Version 1.0\n\n"
            "This program is an open-source USB maker application.\n\n"
            "Created by Angelina Botez\n\n"
            "GNU General Public License v3.0\n"
            "For more details, visit: https://www.gnu.org/licenses/gpl-3.0.html"
        )
        QMessageBox.information(self, "About Maker USB", about_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MakerUSB()
    sys.exit(app.exec_())

