import random

from PySide6.QtCharts import QLineSeries, QValueAxis
from PySide6.QtCore import Qt


class UtStatistics():
	def __init__(self):
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
