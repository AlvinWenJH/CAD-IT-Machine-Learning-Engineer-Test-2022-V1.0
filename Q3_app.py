import tkinter as tk
from tkinter import ttk
from tkinter import Text

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization
import pickle

window = tk.Tk()
canvas = tk.Canvas(window, height = 700, width = 700, bg = "#263D42")

Title = canvas.create_text(350, 100, text="Extract Data from PDF", fill="white", font=('Helvetica 30 bold'))

canvas.create_text(350, 200, text="Input Text : ", fill="white", font=('Helvetica 18 bold'))

Result = canvas.create_text(350, 450, text='Result : --', fill="white", font=('Helvetica 15 bold'))

Input_text = tk.Text(window, height = 3, width = 50)
canvas.create_window(350, 250, window=Input_text)

def load():
  model = load_model("Q3.h5")
  from_disk = pickle.load(open("vectorizer.pkl", "rb"))
  vectorizer = TextVectorization.from_config(from_disk['config'])
  vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
  vectorizer.set_weights(from_disk['weights'])
  return model, vectorizer

def Inference():
  s = Input_text.get("1.0", "end")
  with tf.device("/cpu:0"):
    X = vectorizer(s).numpy()
    y_pred = model.predict(np.expand_dims(X,axis=0))
  label = np.argmax(y_pred)
  label_dict = dict(zip(['AIMX','OWNX','CONT','BASE','MISC'],[0, 4, 2, 1, 3]))
  result = list(label_dict.keys())[list(label_dict.values()).index(label)]
  canvas.itemconfig(Result, text='Result : '+str(result))

with tf.device("/cpu:0"):
  model,vectorizer = load()
Classify = tk.Button(window,text = 'Classify', fg =  "#263D42", bg = "white",command=Inference)
Classify.place(relwidth = 0.2, relheight=0.06, relx = 0.4, rely = 0.5)

canvas.pack()
window.mainloop()