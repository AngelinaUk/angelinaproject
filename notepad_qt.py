import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.textEdit.setFont(QFont("Arial", 12))

        self.statusBar()

        menubar = self.menuBar()
        
        # File menu
        fileMenu = menubar.addMenu("File")
        newAction = QAction("New", self)
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        openAction = QAction("Open", self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction("Save", self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        saveAsAction = QAction("Save As", self)
        saveAsAction.triggered.connect(self.saveAsFile)
        fileMenu.addAction(saveAsAction)

        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Edit menu
        editMenu = menubar.addMenu("Edit")
        undoAction = QAction("Undo", self)
        undoAction.triggered.connect(self.textEdit.undo)
        editMenu.addAction(undoAction)

        redoAction = QAction("Redo", self)
        redoAction.triggered.connect(self.textEdit.redo)
        editMenu.addAction(redoAction)

        cutAction = QAction("Cut", self)
        cutAction.triggered.connect(self.textEdit.cut)
        editMenu.addAction(cutAction)

        copyAction = QAction("Copy", self)
        copyAction.triggered.connect(self.textEdit.copy)
        editMenu.addAction(copyAction)

        pasteAction = QAction("Paste", self)
        pasteAction.triggered.connect(self.textEdit.paste)
        editMenu.addAction(pasteAction)

        deleteAction = QAction("Delete", self)
        deleteAction.triggered.connect(self.deleteText)
        editMenu.addAction(deleteAction)

        findAction = QAction("Find", self)
        findAction.triggered.connect(self.findText)
        editMenu.addAction(findAction)

        replaceAction = QAction("Replace", self)
        replaceAction.triggered.connect(self.replaceText)
        editMenu.addAction(replaceAction)

        selectAllAction = QAction("Select All", self)
        selectAllAction.triggered.connect(self.textEdit.selectAll)
        editMenu.addAction(selectAllAction)

        # View menu
        viewMenu = menubar.addMenu("View")
        zoomInAction = QAction("Zoom In", self)
        zoomInAction.triggered.connect(self.zoomIn)
        viewMenu.addAction(zoomInAction)

        zoomOutAction = QAction("Zoom Out", self)
        zoomOutAction.triggered.connect(self.zoomOut)
        viewMenu.addAction(zoomOutAction)

        # Help menu
        helpMenu = menubar.addMenu("Help")
        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(self.showAbout)
        helpMenu.addAction(aboutAction)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Notepad')
        self.show()

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def saveAsFile(self):
        self.saveFile()

    def deleteText(self):
        cursor = self.textEdit.textCursor()
        cursor.removeSelectedText()

    def findText(self):
        findDialog = FindDialog(self)
        findDialog.exec_()

    def replaceText(self):
        replaceDialog = ReplaceDialog(self)
        replaceDialog.exec_()

    def zoomIn(self):
        self.textEdit.zoomIn()

    def zoomOut(self):
        self.textEdit.zoomOut()

    def showAbout(self):
        about_text = (
            "Version 1.0\n\n"
            "This program is an open-source Notepad application.\n\n"
            "Created by Angelina Botez\n\n"
            "GNU General Public License v3.0\n"
            "For more details, visit: https://www.gnu.org/licenses/gpl-3.0.html"
        )
        QMessageBox.information(self, "About Notepad", about_text)

class FindDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Find")
        self.setText("Find feature is not implemented yet.")

class ReplaceDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Replace")
        self.setText("Replace feature is not implemented yet.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
