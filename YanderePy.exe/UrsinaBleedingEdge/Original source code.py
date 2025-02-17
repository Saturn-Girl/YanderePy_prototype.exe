import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os # unused but for 70-71 76 - 77
import time
import tkinter as tk
from tkinter import messagebox
from pywavefront import wavefront
import json


root = tk.Tk()
root.withdraw()  

class Start: 

   
    def calculateground(self): 
        GroundX = 10.3
        GroundY = 7.3
        GroundZ = 5.2
        dat = float(GroundX) * float(GroundZ)
        sumA = float(GroundY) * float(dat)

    def xyz(self):
        #calculation here
        x = 5.12
        y = 8.15
        z = 4.12
        dat1 = float(x) + float(z)
        dat2 = float(dat1) + float(y)

    def bit(self):
        #32 bit logic here
        bitbytes = 16
        bitdata = 16
        dat3 = int(bitbytes) + int(bitdata)
        if dat3 > 64:
            
            print("default Base data")

class SchoolWear_Gender:

    def SaturnDevA(self,schoolwear,gender):
        gender = "male"

        if schoolwear == "Housewear":
            self.schoolwear = "house"
        if schoolwear == "uniform":
            self.schoolwear = "uniform"
    def PythonChan(self,schoolwear,gender):
        self.gender = "female"
        if schoolwear == "Nude":
            self.schoolwear = "nude"
        if schoolwear == "Uniform":
            self.schoolwear = "Uniform"
            
class Endings:

    def BadEnding(self):
        if CharacterKissedNaked == "Info":
            self.info = {
                1: "Au Microscopii B-Chan",
                2: "SaturnDevA",
                3: "Jhonney",
            }
            
    
    def GenocideEnding1(self):
        
        print("Systsem > Lofi-Chan: haha ha hahahahahahahaahahahahahahaha")
        time.sleep(2)
        print("Systsem > Lofi-Chan: Why I am laughing because you reached the Genocide ending, don't ever think I will be Monika from DDLC.")
        time.sleep(2)
        print("Systsem > GoodByte pointless YanderePy.exe")
        time.sleep(2)
        
        if os.path.exists("Kill.vbs"):
            os.startfile("Kill.vbs")
            messagebox.showwarning("Warning", "The game will delete PygamePlayer.db")
        else:
            print("Error: Kill.vbs not found.")

        if os.path.exists("Pygameplayer.dll"):
            os.remove("PygamePlayer.dll")
            
        else:
            print("Error: PygamePlayer.dll not found.")
class Update:
    
   

    def __init__(self): # i wish i only have 15 over 50 at these subject epp esp english filipino mapeh AP
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.display = (self.screen_width, self.screen_height)
        pygame.display.set_mode(self.display, pygame.DOUBLEBUF | pygame.OPENGL) # math is my only favorite subject
        pygame.display.set_caption("YanderePy.exe (32 bit)") # i am stupid(bobo) at epp esp english filipino mapeh AP

    

        
   
def main(): # kill me
    update = Update()
    start = Start()
    start.calculateground()
    start.xyz()
    start.bit()

if __name__ == "__main__":
    main()
