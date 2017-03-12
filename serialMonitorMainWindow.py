# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow

from serialmonitorUI import Ui_serialMonitor

from serial.tools import list_ports

import serial

from PyQt4.QtCore import QThread, SIGNAL, pyqtSignal

import time

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



class serialMonitorMainWindow(QMainWindow, Ui_serialMonitor):
    def __init__(self):

        # Set up main window
        super(serialMonitorMainWindow, self).__init__()
        self.setupUi(self)

        # Signals and Slots
        self.refreshButton.clicked.connect(self.refresh)
        self.connectButton.toggled.connect(self.connect)
        self.sendButton.clicked.connect(self.send)
        self.clearButton.clicked.connect(self.clear)
        self.lineEdit.returnPressed.connect(self.send)

        # Global class in scope of main window
        self.connection = serial.Serial()

        self.haveMessage = pyqtSignal(str,name='HAVEMESSAGE')
        self.monitorConnection = listenThread()
        self.monitorConnection.start()
        self.monitorConnection.connect(self.monitorConnection, SIGNAL('HAVEMESSAGE'), self.checkSerialPortForString)

    def send(self):

        data = str(self.getTextFromLineEdit())

        if self.connection.is_open:

            self.connection.write(data + '\n')

        outputString = '<html><b><font color="blue">Sent Message:</font></b></html>' + '   ' + data

        self.textBrowser.append(outputString)
        self.lineEdit.clear()

    def connect(self,checked):

        if checked:

            self.connectButton.setText('Discon.')
            self.setupConnection()

            if (self.connection.is_open):

                self.textBrowser.setText('Connection Successful')

            else:

                self.textBrowser.setText('Something went wrong')
                self.textBrowser.setText('Could possibly have connection port open to other devices. Disconnect and try again.')

        elif not checked:

            self.connectButton.setText('Connect')
            self.disconnect()

    def disconnect(self):

        self.connection.close()

    def refresh(self):

        portList = list_ports.comports()
        ports = []

        for port in portList:

            ports.append(str(port[0]))

        self.selectCommPortComboBox.clear()
        self.selectCommPortComboBox.addItems(ports)

        self.updateBaudRates()

        # Display ports to end user
        self.textBrowser.setText('Refreshing Communication Ports...')
        self.textBrowser.append('Found ports at:')
        self.textBrowser.append(str(ports))
        self.textBrowser.append('Select appropriate port from menu and connect')

    def clear(self):

        self.textBrowser.clear()

    def updateBaudRates(self):

        self.selectBaudRateComboBox.clear()

        baudRatelist = ['9600', '19200', '38400', '57600', '115200']

        self.selectBaudRateComboBox.addItems(baudRatelist)

    def getTextFromLineEdit(self):

        dataToSend = self.lineEdit.text()

        return str(dataToSend)

    def setupConnection(self):

        self.connection.port = str(self.selectCommPortComboBox.currentText())
        self.connection.baudrate = int(self.selectBaudRateComboBox.currentText())
        self.connection.open()


    def getMessages(self,data):

        recieveMessage = '<html><b><font color="red">Received Message:</font></b></html>' + '   ' + data
        self.textBrowser.append(recieveMessage)


    def checkSerialPortForString(self,message):

        if message == 'havestring':

            if self.connection.is_open:

                if self.connection.in_waiting > 0:

                    data = str(self.connection.read(self.connection.in_waiting))
                    self.getMessages(data)

class listenThread(QThread):


    def __init__(self):

        QThread.__init__(self)
        self.connection = serial.Serial()
        self.connection.port = 'COM6'

    def __del__(self):

        self.wait()

    def returnMessage(self):

        return 0

    def haveMessage(self):

        return 0

    def run(self):

        while 1:
            message = 'havestring'
            self.emit(SIGNAL("HAVEMESSAGE"),message)
            #self.sleep(0.1)
            time.sleep(0.3)
                

        













    


