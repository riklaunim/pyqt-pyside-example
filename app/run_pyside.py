import sys

from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QApplication

import image_viewer_pyside


class ImageViewer(QtWidgets.QMainWindow, image_viewer_pyside.Ui_ImageViewerWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openImageButton.clicked.connect(self.open_image_action)

    def open_image_action(self):
        prompt = ConfirmationPrompt(self).get_widget()
        prompt.accepted.connect(self.show_image_picker)
        prompt.open()
        return prompt

    def show_image_picker(self):
        picker = ImagePicker(self).get_widget()
        picker.fileSelected.connect(self.image_file_selected)
        picker.show()
        return picker

    def image_file_selected(self, file):
        self.currentFile.setText(file)
        picture = QtGui.QPixmap(file)
        self.imageLabel.setPixmap(picture)


class ConfirmationPrompt:
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        widget = QtWidgets.QMessageBox(self.ui)
        widget.setText('Do you really want to open an image?')
        widget.setIcon(widget.Question)
        widget.addButton('Yes', widget.AcceptRole)
        widget.addButton('No', widget.RejectRole)
        widget.setDetailedText('This is just a show-off for OS differences in prompt windows')
        return widget


class ImagePicker:
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        picker = QtWidgets.QFileDialog(self.ui)
        picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/bmp', 'image/tiff', 'image/gif', 'image/webp'])
        return picker


def main():
    app = QApplication(sys.argv)
    form = ImageViewer()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
