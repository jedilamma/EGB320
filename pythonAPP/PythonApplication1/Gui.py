import tkinter as tk
import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt




class Gui():
    """wrapper for creating gui objects"""

    def __init__(self):
        print("loading gui objects")
        #self.tkinstance = tk()
        self.x = 0
        self.y = 0
        self.resolution = 25;        
        self.fig=plt.figure()
        self.ax = plt.axes()
        

        plt.ion()

    def update(self):
        #fig = plt.gcf()
        #fig.canvas.draw()
        #fig.canvas.flush_events()
        self.ax.clear()
        self.ax.grid()
        patches = []
        self.x += 1
        self.y += 1
        circle = Circle((self.x,self.y),0.5)
        ball = Circle((-2,-4),0.2)
        patches.append(circle)
        patches.append(ball)
        p = PatchCollection(patches, alpha = 0.9)
        self.ax.add_collection(p)
        self.ax.set_aspect(1.0)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_title('Robot Grid')
        
        plt.pause(0.0001)
        plt.draw()
        plt.show()


        #plt.clf()
        #plt.cla()
        #plt.close()  
    def create_button(frame,location):
        i = 0;    
    
    def create_text(frame,data):
        i = 0





