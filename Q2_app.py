from importlib.resources import path
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import Text, filedialog
import re
from tabula.io import read_pdf
import PyPDF2
import numpy as np
import pandas as pd
import os

window = tk.Tk()
canvas = tk.Canvas(window, height = 700, width = 700, bg = "#263D42")
filepath = canvas.create_text(350, 245, text='', fill="white", font=('Helvetica 10'))
prog = canvas.create_text(350, 450, text='Status : --', fill="white", font=('Helvetica 15 bold'))
output = canvas.create_text(350, 525, text='', fill="white", font=('Helvetica 10'))
def browse_button():
    filename = filedialog.askopenfilename(initialdir="your directory path", title="file uploader",
                               filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    canvas.itemconfig(filepath, text=filename)
    

Browse = tk.Button(text="Browse", command=browse_button)
Browse.place(relwidth = 0.15, relheight=0.06, relx = 0.425, rely = 0.4)

canvas.create_text(350, 100, text="Extract Data from PDF", fill="white", font=('Helvetica 30 bold'))
canvas.create_text(350, 200, text="Load PDF : ", fill="white", font=('Helvetica 18 bold'))
# canvas.create_text(300, 650, text="Result : ", fill="white", font=('Helvetica 18 bold'))
canvas.pack()

def get_idxs(df):
  idxs = []
  for idx,word in enumerate(df.values[:,0]):
     if str(word)[0].isupper():
      idxs.append(idx)
  return idxs

def get_Description(df,idxs):
  return df.values[idxs[0]:idxs[1],1][0]

def get_PossibleRootCause(df,idxs):
  return ('; ').join(df.values[idxs[1]:idxs[2],1])

def get_PageNum(pgnum):
  return int([x for x in pgnum if x is not np.nan][0])



def Extract_data():
  filename = canvas.itemcget(filepath, 'text')
  reader = PyPDF2.PdfFileReader(open(filename, mode='rb' ))
  n = reader.getNumPages() 
  desc = []
  prc = []
  pagenum = []
  for i in range(1,n+1):
    dfs = read_pdf(filename,pages=i,stream=True,guess=False)
    pgnum = dfs[0].values[-1]
    for df in dfs:
      idxs = get_idxs(df)
      desc.append(get_Description(df,idxs))
      prc.append(get_PossibleRootCause(df,idxs))
      pagenum.append(get_PageNum(pgnum))
  output_df = pd.DataFrame({'Description':desc,'Possible Root Cause':prc,'Page Number':pagenum})
  outputfile = re.split('/|//',filename)[-1][:-4]
  outputfolder = os.path.join(os.getcwd(),'output')
  if not os.path.exists(outputfolder):
    os.mkdir(outputfolder)
  global outputpath
  outputpath = os.path.join(outputfolder,outputfile+'.xlsx')
  output_df.to_excel(outputpath)
  canvas.itemconfig(prog, text='Status : Done')
  canvas.itemconfig(output, text=outputpath)

Save = tk.Button(window,text = 'Save to excel', fg =  "#263D42", bg = "white", command=Extract_data)
Save.place(relwidth = 0.15, relheight=0.06, relx = 0.425, rely = 0.67)

def open_outputFolder():
  outputpath = canvas.itemcget(output, 'text')
  os.startfile(outputpath)

Open = tk.Button(text="Open Output File", command=open_outputFolder)
Open.place(relwidth = 0.2, relheight=0.06, relx = 0.4, rely = 0.87)

Font_tuple = ("Helvetica", 15, "bold")
Font_tuple_small = ("Helvetica", 12)
Save.configure(font = Font_tuple_small)


window.mainloop()