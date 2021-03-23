# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:54:36 2021

@author: Newe
name : application.py
"""


import shutil, ctypes, sys, os

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
        
    open('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\gosleep.py', 'a')
    shutil.move('gosleep.py', 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\gosleep.py')  
    os.system("start C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\gosleep.py")
    
else:
    print("ERROR : NO UAC rights")
        
