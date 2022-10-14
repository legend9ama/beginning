import tkinter as tk
from tkinter import *
from tkinter import Tk, Menu, Frame
import cv2
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk
import os,sys, pathlib
turnOn = None
cascPath = "C:/Users/USER5/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
win = tk.Tk()
win.geometry("800x600")
my_menu = Menu(win)
win.bind('<Escape>', lambda e: win.quit())
win.title("Face Recognition v.1.0")
lmain = tk.Label(win)
lmain.pack()

def inform():
	messagebox.showinfo("Information", "Face Recognition 1.0/bulterer edition")

def show_frame():
    global turnOn
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if turnOn==1:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
mix_com = show_frame()
def all_command(): 
    global turnOn
    global mix_com
    turnOn=1 
    return turnOn, mix_com
def nall_command():
    global turnOn
    global mix_com
    turnOn=0
    return turnOn, mix_com

fileMenu = Menu(my_menu, tearoff=0)
fileMenu.add_command(label='About', command=inform)
fileMenu.add_command(label="Exit", command=win.quit)
detectionMenu = Menu(my_menu, tearoff=0)
detectionMenu.add_command(label="Camera")
recognizeMenu= Menu(my_menu, tearoff=0)
recognizeMenu.add_command(label="TurnOn", command=all_command)
recognizeMenu.add_command(label="TurnOff", command=nall_command)
my_menu.add_cascade(label="File", menu=fileMenu)
my_menu.add_cascade(label="Detection", menu=detectionMenu)
my_menu.add_cascade(label="Face Recognition", menu=recognizeMenu)
win.config(menu=my_menu)
win.mainloop()