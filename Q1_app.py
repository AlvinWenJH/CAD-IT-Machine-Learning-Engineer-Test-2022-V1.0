import numpy as np
import joblib
import tkinter as tk
from tkinter import ttk
from tkinter import Text, filedialog
import pandas as pd

window = tk.Tk()
canvas = tk.Canvas(window, height = 700, width = 700, bg = "#263D42")
txt = canvas.create_text(420, 650, text='-', fill="white", font=('Helvetica 18 bold'))

canvas.create_text(350, 100, text="Faulty Check", fill="white", font=('Helvetica 30 bold'))
canvas.create_text(250, 200, text="Select Model : ", fill="white", font=('Helvetica 18 bold'))
canvas.create_text(300, 650, text="Result : ", fill="white", font=('Helvetica 18 bold'))

canvas.create_text(150, 325, text="CHP1Temp1(Deg C) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(150, 375, text="CHP1Temp2(Deg C) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(162, 425, text="CHP1Vib1(mm/s) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(162, 475, text="CHP1Vib2(mm/s) : ", fill="white", font=('Helvetica 12 bold'))

canvas.create_text(450, 325, text="CHP2Temp1(Deg C) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(450, 375, text="CHP2Temp2(Deg C) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(462, 425, text="CHP2Vib1(mm/s) : ", fill="white", font=('Helvetica 12 bold'))
canvas.create_text(462, 475, text="CHP2Vib2(mm/s) : ", fill="white", font=('Helvetica 12 bold'))
canvas.pack()

choices = ['RandomForest', 'XGBoost', 'MLP']
variable = tk.StringVar(window)
variable.set('GB')

CH1Temp1 = tk.Entry (window,width=15)
canvas.create_window(285, 325, window=CH1Temp1)

CH1Temp2 = tk.Entry (window,width=15)
canvas.create_window(285, 375, window=CH1Temp2)

CHP1Vib1 = tk.Entry (window,width=15)
canvas.create_window(285, 425, window=CHP1Vib1)

CHP1Vib2 = tk.Entry (window,width=15)
canvas.create_window(285, 475, window=CHP1Vib2)

CH2Temp1 = tk.Entry (window,width=15)
canvas.create_window(585, 325, window=CH2Temp1)

CH2Temp2 = tk.Entry (window,width=15)
canvas.create_window(585, 375, window=CH2Temp2)

CHP2Vib1 = tk.Entry (window,width=15)
canvas.create_window(585, 425, window=CHP2Vib1)

CHP2Vib2 = tk.Entry (window,width=15)
canvas.create_window(585, 475, window=CHP2Vib2)


w = ttk.Combobox(window, values = choices)
w.place(relwidth = 0.2, relheight=0.05, relx = 0.425, rely = 0.34)

def Inference():
    X = np.zeros(8)  
    X[0] = CH1Temp1.get()
    X[1] = CH1Temp2.get()
    X[2] = CH2Temp1.get()
    X[3] = CH2Temp2.get()

    X[4] = CHP1Vib1.get()
    X[5] = CHP1Vib2.get()
    X[6] = CHP2Vib1.get()
    X[7] = CHP2Vib2.get()
    
    X = X.reshape(-1,8)
    model = w.get()
    filename = model+".sav"
    joblib_model = joblib.load(filename)
    ypred = joblib_model.predict(X)

    if ypred[0] == 0:
      ans = 'Not Faulty'
    else:
      ans = 'Faulty'

    canvas.itemconfig(txt, text=ans)

Run = tk.Button(window,text = 'Run', fg =  "#263D42", bg = "white", command=Inference)
Run.place(relwidth = 0.15, relheight=0.06, relx = 0.425, rely = 0.77)

Font_tuple = ("Helvetica", 15, "bold")
Font_tuple_small = ("Helvetica", 12)
Run.configure(font = Font_tuple)
w.configure(font = Font_tuple_small)

window.mainloop()