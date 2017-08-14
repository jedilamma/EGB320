from Networking import * 
from Gui import *

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

#fig, ax = plt.subplots()
#plt.subplots_adjust(bottom=0.1)
#plt.ioff()
fig1 = matplotlib.pyplot.gcf()
fig1.set_size_inches(2.5, 2.5)
#fig.savefig('test2png.png', dpi=100)

class Index(object):
    def start(self, event):
        print ('test1')

    def stop(self, event):
        print ('test2')

callback = Index()
axStart = plt.axes([0.05, 0.65, 0.5, 0.275])
axStop = plt.axes([0.05, 0.25, 0.5, 0.275])
bnext = Button(axStart, 'start')
bnext.on_clicked(callback.start)
bprev = Button(axStop, 'stop')
bprev.on_clicked(callback.stop)
#plt.draw()
#plt.show()


#robot = rb.Robot()
#nws = Network_server()
#nws.connect()

#gui = Gui()
#while 1:
    #gui.update()
  #nws.update()

from PyQt5.QtGui  import QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication

class Settings():
    width = 1024
    height = 768
    BLOCK_WIDTH = int(width/20)
    BLOCK_HEIGHT = int(height/20)
    NUM_BLOCKS_X = int(width/20)
    NUM_BLOCKS_Y = int(height/20)


class GameWindow(QGraphicsView):
    def __init__( self, parent = None ):
        super().__init__(parent)

        self.sx = Settings.width
        self.sy = Settings.height
        self.lines = []
        #self.draw_grid()
        #self.set_opacity(0.3)
        
        self.scene = QGraphicsScene(0,0,Settings.width,Settings.height)
        self.setScene(self.scene)
       
        self.x = 0
        self.y = 0
        self.w = 5
        self.h = 5
        pen   = QPen(QColor('dodgerblue'))
        #pen   = QPen(QColor(Qt.green))
        brush = QBrush(pen.color())
        #brush = QBrush(pen.color().darker(150))

        # As opposed to using QPen and QBrush, this colors the periphery only
        #dot = scene.addEllipse(self.x, self.y, self.w, self.h, QColor('dodgerblue')) 
        self.dot = self.scene.addEllipse(self.x, self.y, self.w, self.h, pen, brush)
        self.dot.setFlag(QGraphicsItem.ItemIsMovable)

        
    def draw_grid(self):
        width = Settings.NUM_BLOCKS_X * Settings.BLOCK_WIDTH
        height = Settings.NUM_BLOCKS_Y * Settings.BLOCK_HEIGHT
        #self.setSceneRect(0,0,width,height)
        
        #self.setItemIndexMethod(QTwidgets.QgraphicsScene.NoIndex)
        pen = QPen(QColor(0,0,0),1,Qt.SolidLine)
        for x in range(-320, Settings.NUM_BLOCKS_X+1):
            xc = x * Settings.BLOCK_WIDTH         
            self.lines.append(self.scene.addLine(xc,0-height/2,xc,height,pen))

        for y in range(-240 ,Settings.NUM_BLOCKS_Y+1):
            yc = y * Settings.BLOCK_HEIGHT
            self.lines.append(self.scene.addLine(0-width/2,yc,width,yc,pen))

    def set_visible(self,visible=True):
        for line in self.lines:
            line.setVisible(visible)

    def delete_grid(self):
        for line in self.lines:
            self.removeItem(line)
        del self.lines[:]

    def set_opacity(self,opacity):
        for line in self.lines:
            line.setOpacity(opacity)



import sys

fps = 50
refresh_period = 1000/fps # ms
app = QApplication(sys.argv)

gw = GameWindow()
gw.draw_grid()
gw.resize(Settings.width,Settings.height)
gw.show()


# if the steps match the gw aspect ratio, the dot will move along the main diagonal,
# otherwise the dot will drift
xstep = 4
ystep = 3
#ystep = xstep * gw.sy / gw.sx

def moveDot():
    # In place of the next four lines, one can have a function 
    # or a feed from an external source to update gw.x and gw.y
    gw.x += xstep
    #gw.x %= gw.sx

    gw.y += ystep
    #gw.y %= gw.sy

    gw.dot.setRect(gw.x,gw.y,gw.w,gw.h)

timer = QTimer()
timer.timeout.connect(moveDot)

# Comment this line out to be able to click and drag the dot
timer.start(refresh_period)

sys.exit(app.exec_())