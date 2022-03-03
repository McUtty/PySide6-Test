import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QValueAxis, QLineSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
from PySide6.QtCore import QFile
from ui.MainWindowTest import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # setup UI
        self.setupUi(self)
        # setup stackedWidget_Pages_Widgets
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # setup Overview
        # self.tableView_questions.set

        # setup Charts
        # Creating QChart
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.add_series("Magnitude (Column 1)", [0, 1])
        # Creating QChartView
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.horizontalLayout.addWidget(self.chart_view)

    def add_series(self, name, columns):
        # Create QLineSeries
        self.series = QLineSeries()
        self.series.setName(name)

        # Filling QLineSeries
        # for i in range(self.statistic_tableView. .rowCount()):
        #     # Getting the data
        #     t = self.statistic_tableView.index(i, 0).data()
        #
        #     date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"
        #
        #     x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
        #
        #     y = float(self.statistic_tableView.index(i, 1).data())
        for i in range(20):
            x = i
            y = random.randint(1, 100)

            if x > 0 and y > 0:

                self.series.append(x, y)

        self.chart.addSeries(self.series)

        # Setting X-axis
        # self.axis_x = QDateTimeAxis()
        self.axis_x = QValueAxis()
        self.axis_x.setTickCount(10)
        # self.axis_x.setFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        # Setting Y-axis
        self.axis_y = QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Test")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())