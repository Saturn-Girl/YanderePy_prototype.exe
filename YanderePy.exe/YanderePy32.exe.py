from ursina import * 
from tkinter import * 
from tkinter import messagebox 
import os  # unused import except for deleting files
import time
import sys
import json


app = Ursina()
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='error', font = "50")  
w.pack() 
class Start:
    def __init__(self):
        print("a game by Saturn Computing Integrated Graphics")
        print("Developer: CalculatorOS_dev.exe")
        print("music art 3d model and programing is made by CalculatorOS_dev.exe")
        print("CalculatorOS_dev.exe programer mathematician musician and artist 2d/3d")
        time.sleep(2)
        print("Checking save data")
        time.sleep(2)
        
        if os.path.exists("Save1.json"):
            Save1 = True 
            with open('Save1.json', 'r') as file:
                data = json.load(file)
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("Save1.json"):
            Save1 = True
            with open('Save1.json', 'r') as file:
                data = json.load(file)
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("Save2.json"):
            with open('Save2.json', 'r') as file:
                data = json.load(file)
            Save2 = True
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("Save3.json"):
            with open('Save3.json', 'r') as file:
                data = json.load(file)
            Save3 = True
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("Save4.json"):
            Save4 = True
            with open('Save4.json', 'r') as file:
                data = json.load(file)
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("Save5.json"):
            Save5 = True
            with open('Save5.json', 'r') as file:
                data = json.load(file)
            print("Save file found")
        else:
            print("Info: Save data not found no data or object")
        if os.path.exists("UrsinaBleedingEdge\Pygame.json"):
            with open('UrsinaBleedingEdge\Pygame.json', 'r') as file:
                data = json.load(file)
            print("file found")
        else:
            messagebox.showerror("File not found", "Error Pygame.json not found")
            time.sleep(2)
            sys.exit()
            

class ModelLoader:
    if os.path.exists("Blender.obj"):
        Blender_model = load_model('Blender.obj')
    else:
        print("Model not found")
    if os.path.exists("Blender.obj"):
        Blender_model = load_model('UBlender.obj')
    else:
        print("Model not found")
    if os.path.exists("Blender.obj"):
        Blender_model = load_model('UBlender.obj')
    else:
        print("Model not found")
class Dialogue:
    if os.path.exists("Dialogue.json"):
        with open('Save1.json', 'r') as file:
            data = json.load(file)
            print("Save file found")
    else:
        print("Info: Save data not found no data or object")
        messagebox.showerror("File not found", "Error file not found")

time.sleep(2)      

class WeaponNameNumber:
    WeaponKatana = False
    WeaponKnife = False
    WeaponGun = False
    if WeaponKatana:
        print("weapon is katana")
    if WeaponKnife:
        print("Weapon is knife")
    if WeaponGun:
        print("Weapon is Gun")

class PlayerPythonChan:
    def __init__(self, Charactername1, age1):
        self.Charactername1 = Charactername1
        self.age1 = age1
    
    def CommitMurder(self):
        IsMurdered = False
        if IsMurdered:
            print("rival murdered")

class System32:
    Murdered = True
    PervertMode = True     
    
    if PervertMode:
        print("System > Panty shot  complete")
    else:
        print("System > No phone detectd to take panties")
    if Murdered:
        print("System character murdered")
    else:
        print("System > no weapon detected no murder")

class Ending:

    def TrueEnding(self):
        TrueEnding1 = "Normal"
        TrueEnding2 = "BadEnding1"
        TrueEnding3 = "BadEnding2"
        TrueEnding4 = "Genocide1"
        FalseEnding = "JenessaEnding"
        if TrueEnding1 == "Normal":
            print("you got your senpai the end")
            time.sleep(5)
            sys.exit()
        if TrueEnding2 == "BadEnding1":
            print("you got your senpai the end")
            IsHavingIntimacy = True
            if IsHavingIntimacy:
                if os.path.exists("YanderePy32.dll"):
                    os.remove("YanderePy32.dll")
                else:
                    print("Error:")
                time.sleep(5)
                os.remove(__file__)
        if FalseEnding == "JenessaEnding":
            os.remove(__file__)
        if TrueEnding1 == "Normal":
            print("you got your senpai the end")
            time.sleep(5)
            sys.exit()
class KarenScript:
    sentence = "I wanna speak to your manager do you understood"
    if sentence == "I wanna speak to your manager do you understood":
        print(f"sentence is {sentence}")
class Update:
    def CheckGun(self):
        Gun = "Ak47"
        if Gun == "Ak47":
            print(f"Your Gun is {Gun}")
        else:
            print(f"the gun you have is NOT {Gun}")
    def Draw(self):
        X = 10.2
        Y = 8.13
        dat1 = float(X) + float(Y)

    def Graphics(self):
        Graphics = True
        if Graphics:
            ObjectX = 5.2
            ObjectY = 7.2
            dat2 = float(ObjectX) + float(ObjectY)
            print(f" Moved calculation from {dat2}")

Character1 = PlayerPythonChan("PythonChan", 18)
EditorCamera()
app.run()
