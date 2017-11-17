import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt

class MDIArea(QMdiArea):
	def __init__(self, background_pixmap, parent = None):
		QMdiArea.__init__(self, parent)
		self.background_pixmap = background_pixmap
		self.centered = False

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self.viewport())

		if not self.centered:
			painter.drawPixmap(0, 0, self.width, self.height, self.background_pixmap)
		else:
			painter.fillRect(event.rect(), self.palette().color(QPalette.Window))
			x = (self.width() - self.display_pixmap.width())/2
			y = (self.height() - self.display_pixmap.height())/2
			painter.drawPixmap(x, y, self.display_pixmap)

		painter.end()

	def resizeEvent(self, event):
		self.display_pixmap = self.background_pixmap.scaled(event.size(), Qt.KeepAspectRatio)

def window():
	app = QApplication(sys.argv)

	m = MDIArea(QPixmap("../art/angry_raptors.png"))
	m.centered = True
	m.show()
	sys.exit(app.exec_())
