import tkinter as tk
import customtkinter as ctk
import torch
import numpy
import  cv2
from PIL import Image, ImageTk
import vlc

app = tk.Tk()
app.geometry("600x600")
app.title("Drowsy")
ctk.set_appearance_mode("dark")


vidFrame = tk.Frame(master=app, height=480,width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()

cap = cv2.VideoCapture(0)
def detect():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10,detect)


detect()
app.mainloop()