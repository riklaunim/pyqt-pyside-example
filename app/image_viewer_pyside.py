# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ImageViewerWindow(object):
    def setupUi(self, ImageViewerWindow):
        if not ImageViewerWindow.objectName():
            ImageViewerWindow.setObjectName(u"ImageViewerWindow")
        ImageViewerWindow.resize(654, 374)
        self.centralwidget = QWidget(ImageViewerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openImageButton = QPushButton(self.centralwidget)
        self.openImageButton.setObjectName(u"openImageButton")

        self.horizontalLayout.addWidget(self.openImageButton)

        self.currentFile = QLabel(self.centralwidget)
        self.currentFile.setObjectName(u"currentFile")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.currentFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.imageLabel)

        ImageViewerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImageViewerWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImageViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageViewerWindow)

        QMetaObject.connectSlotsByName(ImageViewerWindow)
    # setupUi

    def retranslateUi(self, ImageViewerWindow):
        ImageViewerWindow.setWindowTitle(QCoreApplication.translate("ImageViewerWindow", u"Example Image Viewer", None))
        self.openImageButton.setText(QCoreApplication.translate("ImageViewerWindow", u"Open image", None))
        self.currentFile.setText(QCoreApplication.translate("ImageViewerWindow", u"No file selected", None))
        self.imageLabel.setText("")
    # retranslateUi

