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
        prompt = ConfirmationPrompt(self)
        if prompt.confirm():
            picker = self._get_image_picker()
            picker.exec_()

    def _get_image_picker(self):
        picker = QtWidgets.QFileDialog(self)
        picker.setMimeTypeFilters(['image/jpeg', 'image/png', 'image/bmp', 'image/tiff', 'image/gif', 'image/webp'])
        picker.fileSelected.connect(self.image_file_selected)
        return picker

    def image_file_selected(self, file):
        self.currentFile.setText(file)
        picture = QtGui.QPixmap(file)
        self.imageLabel.setPixmap(picture)


class ConfirmationPrompt:
    CONFIRM = 'Yes'
    REJECT = 'No'

    def __init__(self, ui):
        self.ui = ui

    def confirm(self):
        confirm_prompt = self._build_confirmation_message_box()
        confirm_prompt.exec_()
        return confirm_prompt.clickedButton().text() == self.CONFIRM

    def _build_confirmation_message_box(self):
        box = QtWidgets.QMessageBox(self.ui)
        box.setText('Do yu really want to open an image?')
        box.setIcon(box.Question)
        box.addButton(self.CONFIRM, box.AcceptRole)
        box.addButton(self.REJECT, box.RejectRole)
        box.setDetailedText('This is just a show-off for OS differences in prompt windows')
        return box


def main():
    app = QApplication(sys.argv)
    form = ImageViewer()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
