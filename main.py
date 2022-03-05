import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QValueAxis, QLineSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile
from ui.MainWindowTest import Ui_MainWindow
from UtStatistic.utstatistic import FillStatistics


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # setup UI
        self.setupUi(self)
        # setup stackedWidget_Pages_Widgets
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # setup Overview

        # setup Charts
        self.chart = FillStatistics()
        # Creating QChart
        self.chart.setAnimationOptions(QChart.AllAnimations)
        FillStatistics.add_series("Magnitude (Column 1)", [0, 1])
        # Creating QChartView
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.horizontalLayout.addWidget(self.chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())