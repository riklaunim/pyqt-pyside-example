import os
import pathlib

from unittest import mock

from PySide2 import QtCore

from app import run_pyside


class TestPySideImageViewer:
    """
    Tests limited as qtbot expects PyQt
    """
    def test_if_main_window_renders(self, qtbot):
        window = run_pyside.ImageViewer()
        qtbot.addWidget(window)
        assert window.currentFile.text() == 'No file selected'
        assert window.openImageButton.text() == 'Open image'

    def test_if_image_is_displayed(self, qtbot):
        path = pathlib.Path().absolute()
        file = os.path.join(path, 'tests/test.jpg')

        window = run_pyside.ImageViewer()
        qtbot.addWidget(window)
        window.image_file_selected(file)
        assert window.currentFile.text().endswith('/test.jpg')
        assert window.currentFile.text() == file
        assert window.imageLabel.pixmap().width() == 242
        assert window.imageLabel.pixmap().height() == 221

    @mock.patch('app.run_pyside.ImageViewer.show_image_picker')
    def test_if_show_image_picker_is_called_on_prompt_accept(self, show_image_picker, qtbot):
        window = run_pyside.ImageViewer()
        qtbot.addWidget(window)
        prompt = window.open_image_action()
        prompt.accept()
        assert show_image_picker.called

    @mock.patch('app.run_pyside.ImageViewer.show_image_picker')
    def test_if_show_image_picker_is_not_called_when_prompt_not_accept(self, show_image_picker, qtbot):
        window = run_pyside.ImageViewer()
        qtbot.addWidget(window)
        window.open_image_action()
        assert not show_image_picker.called

    @mock.patch('app.run_pyside.ImageViewer.image_file_selected')
    def test_if_image_file_selected_is_called_on_file_selection(self, image_file_selected, qtbot):
        path = pathlib.Path().absolute()
        file = os.path.join(path, 'tests/test.jpg')

        def accept():
            picker.accept()

        window = run_pyside.ImageViewer()
        qtbot.addWidget(window)
        picker = window.show_image_picker()
        picker.selectFile(file)

        picker.done(1)
        QtCore.QTimer.singleShot(100, accept)
        picker.exec_()
        assert image_file_selected.called
