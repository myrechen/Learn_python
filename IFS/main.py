import sys
from PyQt5.QtWidgets import QApplication, QWidget

# import Ui_coefficientcontrol
import Ui_affinetranscontrol

import Ui_ifscontrol

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # MainWindow = QWidget()

    # ui = Ui_coefficientcontrol.CoefficientControlWidget()
    # ui.setCoefficientName("X")

    # ui = Ui_affinetranscontrol.AffineTransWidget()
    ui = Ui_ifscontrol.IFSControlWidget()
    ui.resize(1600, 800)

    ui.show()
    

    # MainWindow.show()
    sys.exit(app.exec_())
