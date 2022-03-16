import random

from PySide6 import QtCharts
from PySide6.QtCore import Qt

from ui.MainWindowTest import Ui_MainWindow
from PySide6.QtWidgets import QSizePolicy, QMainWindow
from PySide6.QtCharts import QChart, QChartView
from PySide6.QtGui import QPainter


class FillStatistics(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()

		self.chart = QtCharts.QChart()
		self.size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		self.series = QtCharts.QLineSeries()
		self.chart_view = QChartView(self.chart)


	def add_series(self, name, columns):
		# Create QLineSeries

		self.series.setName(name)

		for i in range(20):
			x = i
			y = random.randint(1, 100)

			if x > 0 and y > 0:
				self.series.append(x, y)

		return self.series


	def setupCharts(self):
		# setup Charts
		#self.chart = FillStatistics.add_series(self, "Franz", 2)
		FillStatistics.add_series(self, "Franz", 2)
		# Creating QChart
		self.chart.setAnimationOptions(QChart.AllAnimations)
		self.add_series("Magnitude (Column 1)", [0, 1])
		# Creating QChartView
		# self.chart_view = QChartView(self.chart)
		self.chart_view.setRenderHint(QPainter.Antialiasing)

		# Setting X-axis
		# self.axis_x = QDateTimeAxis()
		self.axis_x = QtCharts.QValueAxis()
		self.axis_x.setTickCount(10)
		# self.axis_x.setFormat("dd.MM (h:mm)")
		self.axis_x.setTitleText("Date")
		self.chart.addAxis(self.axis_x, Qt.AlignBottom)
		self.series.attachAxis(self.axis_x)

		# Setting Y-axis
		self.axis_y = QtCharts.QValueAxis()
		self.axis_y.setTickCount(10)
		self.axis_y.setLabelFormat("%.2f")
		self.axis_y.setTitleText("Test")
		self.chart.addAxis(self.axis_y, Qt.AlignLeft)
		self.series.attachAxis(self.axis_y)

		self.size.setHorizontalStretch(4)
		self.chart_view.setSizePolicy(self.size)
		self.horizontalLayout.addWidget(self.chart_view)
