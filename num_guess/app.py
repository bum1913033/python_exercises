#imports
import tkinter as tk
from tkinter import *
import random

#functions
def check_guess():
    global guess_count
    try:
        guess = int(guess_entry.get())
        if guess < number:
            result_label.config(text=f'Your guess {guess} is lower. Try again!')
        elif guess > number:
            result_label.config(text=f'Your guess {guess} is higher. Try again!')
        else:
            result_label.config(text=f'Congratulations! The answer was {number}!')
            guess_btn.config(state='disable')
        
        guess_count += 1
        if guess_count >= 5:
            result_label.config(text=f'Sorry, you\'ve guessed five times.\n The correct number was {number}.')
            guess_btn.config(state='disable')
    except:
        result_label.config(text='Your guess cannot be null or float.')

def validate(new_value):
    try:
        int(new_value)
        return True
    except ValueError:
        guess_entry.delete(0, tk.END)
        result_label.config(text="The value that you are attempting to guess\n is not an integer.")
        return False

#main
root = tk.Tk()
root.title("Guess the Number!")

#canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

number = random.randint(1,10)
guess_count = 0

#instruction label
instruction_label = tk.Label(root, text="Guess a number between 1 and 10:", font="VCR_OSD_Mono")
instruction_label.grid(columnspan=3, column=0, row=0)

#guess entry
guess_entry = tk.Entry(root, validate='key')
guess_entry.config(validatecommand=(guess_entry.register(validate), '%P'))
guess_entry.grid(column=1, row=1)

#result label
result_label = tk.Label(root, font="VCR_OSD_Mono")
result_label.grid(columnspan=3, column=0, row=2)

#guess button
guess_btn = tk.Button(root, text="Guess", command=check_guess, bg="#20bebe", fg="white", height=2, width=15)
guess_btn.grid(column=2, row=1)

root.mainloop()