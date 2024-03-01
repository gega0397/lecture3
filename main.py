import sys
import os

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import math


class MainWidget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi(os.path.join(os.getcwd(), 'calculator.ui'), self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))
        self.calculate.clicked.connect(self._calculate)
        self.calculators = {
            "wre": self._calculate_wre,
            "samkutxedi": self._calculate_samkutxedi,
            "trapecia": self._calculate_trapecia,
            "kvadrati": self._calculate_kvadrati,
        }
        self.shapes = {"wre", "samkutxedi", "trapecia", "kvadrati"}

    def select_shape(self):

        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main)
        )

    def _calculate(self):

        shape = self.stackedWidget.currentWidget().objectName().split("_", 2)[0]
        print(shape)
        if shape in self.shapes:
            res, err = self.calculators[shape]()
            if err:
                QtWidgets.QMessageBox.warning(self, "Invalid Inputs", "გვერდების სიგრძეები არასწორია")
            else:
                #res = self._calculate_wre()
                print('wre:',res)
                area = getattr(self, f'lcd_{shape}_area', self.main)
                perimeter = getattr(self, f'lcd_{shape}_perimeter', self.main)
                area.display(res['area'])
                perimeter.display(res['len'])

    def _calculate_wre(self):

        _val = self.r1.value()
        if _val <= 0:
            return (None, True)
        _area = math.pi * _val ** 2
        _len = math.pi * _val * 2
        return ({"area": _area, "len": _len}, False)

    def _calculate_samkutxedi(self):

        self.gverdebi_s = [self.s1.value(), self.s2.value(), self.s3.value()]
        _len = sum(self.gverdebi_s)
        for gverdi in self.gverdebi_s:
            print(self.gverdebi_s)
            if gverdi >= (_len - gverdi) or gverdi <= 0:
                return (None, True)
        s = _len / 2
        _area = math.sqrt(s * (s - self.gverdebi_s[0]) * (s - self.gverdebi_s[1]) * (s - self.gverdebi_s[2]))
        return ({"area": _area, "len": _len}, False)

    def _calculate_trapecia(self):

        self.gverdebi_t = [self.b1.value(), self.b2.value(), self.b3.value(), self.b4.value()]
        print(self.gverdebi_t)
        for gverdi in self.gverdebi_t:
            if gverdi <= 0:
                return (None, True)
        try:
            _area = ((self.gverdebi_t[1] + self.gverdebi_t[0])/2) *\
                math.sqrt((math.pow(self.gverdebi_t[2], 2) -\
                           math.pow(
                                ((math.pow((self.gverdebi_t[0]-self.gverdebi_t[1]), 2) +\
                                math.pow(self.gverdebi_t[2],2) - math.pow(self.gverdebi_t[3], 2)) /\
                                (2*(self.gverdebi_t[0] - self.gverdebi_t[1]))\
                            ), 2)))
            _len = sum(self.gverdebi_t)
            if _area > 0:
                return ({"area": _area, "len": _len}, False)
        except ZeroDivisionError as e:
            print(e)
        return (None, True)

    def _calculate_kvadrati(self):

        _val = self.k1.value()
        if _val <= 0:
            return (None, True)
        _area = _val ** 2
        _len = _val * 4
        return ({"area": _area, "len": _len}, False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
