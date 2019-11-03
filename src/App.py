import sys
from threading import Thread
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent= None):
        super().__init__()
        self.setupUi(self)

        #========== Connect event handlers ==========#
        self.btnAnalyze.clicked.connect(self.btnAnalyze_clicked)
        self.btnInputBrowse.clicked.connect(self.btnInputBrowse_clicked)
        self.btnOutputBrowse.clicked.connect(self.btnOutputBrowse_clicked)
        #============================================#


    #+++++++++++++++ Event handlers +++++++++++++++#
    def btnAnalyze_clicked(self):
        inputFile, outputFile, language = self.getCLIArgs()
        proc = subprocess.Popen(['cohmetrix','-i',inputFile,'-o',outputFile,'-l',language,'-n','-8'], stdout=subprocess.PIPE)
        t = Thread(target=self.stdOutReader, args=[proc])
        t.start()

    def btnInputBrowse_clicked(self):
        inputFile = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lneInputFile.setText(inputFile)

    def btnOutputBrowse_clicked(self):
        outputFile, _filter = QFileDialog.getSaveFileName()
        self.lneOutputFile.setText(outputFile)
    #++++++++++++++++++++++++++++++++++++++++++++++#
    

    #+++++++++++++++ Helpers ++++++++++++++++++++++#
    def stdOutReader(self, proc):
        for line in iter(proc.stdout.readline, b''):
            self.txtStdOut.append(line.decode('utf-8'))

    def getCLIArgs(self):
        return (self.lneInputFile.text(), self.lneOutputFile.text(), self.cbLanguage.currentText())
    #++++++++++++++++++++++++++++++++++++++++++++++#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
