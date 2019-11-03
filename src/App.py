import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
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

    def btnAnalyze_clicked(self):
        pass

    def btnInputBrowse_clicked(self):
        inputFile = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lneInputFile.setText(inputFile)

    def btnOutputBrowse_clicked(self):
        outputFile, _filter = QFileDialog.getSaveFileName()
        self.lneOutputFile.setText(outputFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
