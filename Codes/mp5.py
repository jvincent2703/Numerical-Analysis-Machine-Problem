import both1 as mp1
import both2 as mp2
import both3 as mp3
import both4 as mp4
import math
import sympy as sym
import numpy as np

class UI:
    
    def __init__(self):
        pass
    
    def loop(self):
        ongoing = True
        
        while ongoing:
            print("Main Menu: ")
            print("1. Machine Problem 1")
            print("2. Machine Problem 2")
            print("3. Machine Problem 3")
            print("4. Machine Problem 4")
            print("5. Exit")
            mm = input("Choose from 1-5: ")
            if mm == '1':
                mp1.process()
            if mm == '2':
                mp2.Calculator()
            if mm == '3':
                mp3.main()
            if mm == '4':
                pp = mp4.NumericalIntegration()
                pp.calculate()
            if mm == '5':
                ongoing = False
ui = UI()
ui.loop()