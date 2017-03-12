# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialmonitor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_serialMonitor(object):
    def setupUi(self, serialMonitor):
        serialMonitor.setObjectName(_fromUtf8("serialMonitor"))
        serialMonitor.resize(875, 651)
        self.centralWidget = QtGui.QWidget(serialMonitor)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setMargin(11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mainWindowLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mainWindowLabel.setFont(font)
        self.mainWindowLabel.setObjectName(_fromUtf8("mainWindowLabel"))
        self.horizontalLayout_3.addWidget(self.mainWindowLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.selectCommPortComboBox = QtGui.QComboBox(self.centralWidget)
        self.selectCommPortComboBox.setEditable(False)
        self.selectCommPortComboBox.setObjectName(_fromUtf8("selectCommPortComboBox"))
        self.horizontalLayout_3.addWidget(self.selectCommPortComboBox)
        self.selectBaudRateComboBox = QtGui.QComboBox(self.centralWidget)
        self.selectBaudRateComboBox.setObjectName(_fromUtf8("selectBaudRateComboBox"))
        self.horizontalLayout_3.addWidget(self.selectBaudRateComboBox)
        self.refreshButton = QtGui.QPushButton(self.centralWidget)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.horizontalLayout_3.addWidget(self.refreshButton)
        self.connectButton = QtGui.QPushButton(self.centralWidget)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.connectButton.setCheckable(True)
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.sendButton = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout.addWidget(self.sendButton)
        self.clearButton = QtGui.QPushButton(self.centralWidget)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        serialMonitor.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(serialMonitor)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        serialMonitor.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(serialMonitor)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        serialMonitor.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(serialMonitor)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        serialMonitor.setStatusBar(self.statusBar)

        self.retranslateUi(serialMonitor)
        QtCore.QMetaObject.connectSlotsByName(serialMonitor)

    def retranslateUi(self, serialMonitor):
        serialMonitor.setWindowTitle(_translate("serialMonitor", "Serial Monitor", None))
        self.mainWindowLabel.setText(_translate("serialMonitor", "Serial Monitor", None))
        self.refreshButton.setText(_translate("serialMonitor", "Refresh", None))
        self.connectButton.setText(_translate("serialMonitor", "Connect", None))
        self.sendButton.setText(_translate("serialMonitor", "Send", None))
        self.clearButton.setText(_translate("serialMonitor", "Clear", None))

