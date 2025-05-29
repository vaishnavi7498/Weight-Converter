import tkinter as tk
from tkinter import *

window = Tk()
window.title("CONVERTER")
window.geometry("500x500")

Label(window,text="WEIGHT CONVERTER", font=("Arial",20), bg="black", fg="white").pack()

kg = tk.IntVar()

def convert_to_gram():
    kg1 = kg.get()
    gram = float(kg1)*1000
    Label(window,text="This weightin grams would be", font=("Arial",15)).pack()
    Label(window,text=gram,bg="pink").pack()

def convert_to_ounce():
    kg1 = kg.get()
    ounce = float(kg1)*35.27
    Label(window,text="This weightin ounce would be", font=("Arial",15)).pack()
    Label(window,text=ounce,bg="pink").pack()

def convert_to_pound():
    kg1 = kg.get()
    pound = float(kg1)*2.20462
    Label(window,text="This weightin pound would be", font=("Arial",15)).pack()
    Label(window,text=pound,bg="pink").pack()

Label(window,text="Enter the weight in kgs", font=("Arial",18)).pack()

Entry(window,textvariable=kg , font=(15)).pack()

Button(window,text="Convert to Gram", bg="gray",command=convert_to_gram).pack()


Button(window,text="Convert to Ounce", bg="gray",command=convert_to_ounce).pack()


Button(window,text="Convert to Pound", bg="gray",command=convert_to_pound).pack()

window.mainloop()