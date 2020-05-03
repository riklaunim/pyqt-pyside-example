import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

import image_viewer_pyside


class ImageViewer(QtWidgets.QMainWindow, image_viewer_pyside.Ui_ImageViewerWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = ImageViewer()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
