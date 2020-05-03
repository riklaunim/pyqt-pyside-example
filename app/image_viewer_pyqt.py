# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageViewerWindow(object):
    def setupUi(self, ImageViewerWindow):
        ImageViewerWindow.setObjectName("ImageViewerWindow")
        ImageViewerWindow.resize(654, 374)
        self.centralwidget = QtWidgets.QWidget(ImageViewerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.openImageButton.setObjectName("openImageButton")
        self.horizontalLayout.addWidget(self.openImageButton)
        self.currentFile = QtWidgets.QLabel(self.centralwidget)
        self.currentFile.setObjectName("currentFile")
        self.horizontalLayout.addWidget(self.currentFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        ImageViewerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ImageViewerWindow)
        self.statusbar.setObjectName("statusbar")
        ImageViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageViewerWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageViewerWindow)

    def retranslateUi(self, ImageViewerWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageViewerWindow.setWindowTitle(_translate("ImageViewerWindow", "Example Image Viewer"))
        self.openImageButton.setText(_translate("ImageViewerWindow", "Open image"))
        self.currentFile.setText(_translate("ImageViewerWindow", "No file selected"))
