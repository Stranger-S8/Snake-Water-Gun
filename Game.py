from tkinter import* 
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import random as r
import time as t
import threading
import queue

lines="""1. Snake drinks Water; Snake wins.
2. Water rusts Gun; Water wins.
3. Gun shoots Snake; Gun wins.
4. If both players choose the same option, the round is a tie.
5. Players make their choice secretly and reveal them simultaneously.
6. Ties do not award any points.
7. Enjoy the game and aim to outsmart your opponent!"""

s=""" © 2024 Strange Games. All rights reserved.
This game is licensed for personal use only.
Unauthorized distribution or modification is prohibited."""

result=""
user_choice=""
computer_choice=""

# Create a queue to communicate with the GUI thread
gui_queue = queue.Queue()

def start_loading():
    def load():
        for i in range(1, 101):
            gui_queue.put(i)
            t.sleep(0.05)
        gui_queue.put("done")
    
    load_thread = threading.Thread(target=load)
    load_thread.start()
    check_queue()

def check_queue():
    try:
        progress_value = gui_queue.get_nowait()
        if progress_value == "done":
            main_window()
        else:
            progress['value'] = progress_value
            loading.after(50, check_queue)
    except queue.Empty:
        loading.after(50, check_queue)

def clear():
    global result
    global user_choice
    global computer_choice
    
    t.sleep(3)
    result=""
    user_choice=""
    computer_choice=""

    lab3.config(text=user_choice)
    lab4.config(text=computer_choice)
    lab5.config(text=result)

loading = Tk()
def main_window():
    def rules():
        def destroy():
            root.destroy()
        
        root = Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        c_x = int(width/2-400/2)
        c_y = int(height/2-600/2)
        
        root.resizable(False,False)
        root.overrideredirect(True)
        root.config(bg="#ADD8E6")
        root.geometry(f"600x400+{c_x}+{c_y}")

        heading = Label(root, text="Game Rules", font=("Arial", 20, "bold"), bg="#2C2F33", fg="#FFD700", pady=20)
        heading.pack()

        lab = Label(root, text=lines, width=50, bg="#ADD8E6", fg="black", justify="left", font=("Arial", 14))
        lab.pack(expand=True, padx=20, pady=20)

        close = Button(root, text="Close", width=10, height=3, bg="Red", fg="black", relief="raised", command=destroy, font=("Helvetica",10,"bold"))
        close.pack(side="bottom")

        root.mainloop()
    def game(choice):
        global result
        global user_choice
        global computer_choice
        
        options = ["Snake", "Water", "Gun"]
        computer_choice = r.choice(options)
        user_choice = choice

        if user_choice == computer_choice:
            result = "Draw!"
        elif (user_choice == "Snake" and computer_choice == "Water") or \
             (user_choice == "Water" and computer_choice == "Gun") or \
             (user_choice == "Gun" and computer_choice == "Snake"):
            result = "User Wins!"
        else:
            result = "Computer Wins!"
        lab3.config(text=user_choice)
        lab4.config(text=computer_choice)
        lab5.config(text=result)
    def clear():
        global result
        global user_choice
        global computer_choice
        
        t.sleep(3)
        result=""
        user_choice=""
        computer_choice=""

        lab3.config(text=user_choice)
        lab4.config(text=computer_choice)
        lab5.config(text=result)
    loading.destroy()
    win = Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    c_x = int(width/2-1024/2)
    c_y = int(height/2-720/2)

    win.title("Strange Game")
    win.config(bg="#3B0B39")
    win.geometry(f"1024x700+{c_x}+{c_y}")
    win.resizable(True, True)
    win.iconbitmap(r"snake.ico")

    lab = Label(win, text="Snake Water Gun", font=("Helvetica", 40, "bold"), bg="#3B0B39", fg="#FFD700")
    lab.pack()
    
    frame = Frame(win, bg="#3B0B39")
    frame.pack(pady=20)

    frame1 = Frame(win, bg="#3B0B39")
    frame1.pack(pady=0)

    frame2 = Frame(win, bg="#3B0B39")
    frame2.pack(pady=20)

    frame3 = Frame(win, bg="#3B0B39")
    frame3.pack(pady=20)

    a = Image.open("snake.png")
    b = Image.open("water.png")
    c = Image.open("gun.png")

    a_r = a.resize((200, 200), Image.LANCZOS)
    b_r = b.resize((200, 200), Image.LANCZOS)
    c_r = c.resize((200, 200), Image.LANCZOS)
    
    snake_icon = ImageTk.PhotoImage(a_r)
    water_icon = ImageTk.PhotoImage(b_r)
    gun_icon = ImageTk.PhotoImage(c_r)
    
    snake = Label(frame, image=snake_icon, width=200, height=200, bg="#3B0B39")
    snake.pack(side="left", padx=5)
    water = Label(frame, image=water_icon, width=200, height=200, bg="#3B0B39")
    water.pack(side="left", padx=5)
    gun = Label(frame, image=gun_icon, width=200, height=200, bg="#3B0B39")
    gun.pack(side="left", padx=5)

    b_1 = Button(frame1, text="Snake", width=10, height=3, bg="#FF6347", fg="#FFFFFF", relief="raised", font=("Helvetica", 10, "bold"), command=lambda:game("Snake"), activebackground="cyan")
    b_1.pack(side="left", padx=80, pady=0)
    b_2 = Button(frame1, text="Water", width=10, height=3, bg="#1E90FF", fg="#FFFFFF", relief="raised", font=("Helvetica", 10, "bold"), command=lambda:game("Water"), activebackground="cyan")
    b_2.pack(side="left", padx=80, pady=0)
    b_3 = Button(frame1, text="Gun", width=10, height=3, bg="#D3D3D3", fg="#FFFFFF", relief="raised", font=("Helvetica", 10, "bold"), command=lambda:game("Gun"), activebackground="cyan")
    b_3.pack(side="left", padx=80, pady=0)

    lab1 = Label(frame2, text="User", width=20, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="#FFD700")
    lab1.pack(padx=130, pady=0, side="left")
    lab2 = Label(frame2, text="Computer", width=20, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="#FFD700")
    lab2.pack(padx=130, pady=0, side="left")

    lab3 = Label(frame3, text=user_choice, width=20, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="Red")
    lab3.pack(padx=130, pady=10, side="left")
    lab4 = Label(frame3, text=computer_choice, width=20, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="Red")
    lab4.pack(padx=130, pady=10, side="left")

    lab5 = Label(win, text=result, width=20, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="Light green")
    lab5.pack(padx=70)

    rules = Button(win, text="Rules", width=10, height=3, bg="Red", fg="#FFFFFF", relief="raised", font=("Helvetica", 10, "bold"), command=rules, activebackground="cyan")
    rules.pack(side="left", padx=0, pady=0, anchor="w")

    snake.a_r = snake_icon
    water.b_r = water_icon
    gun.c_r = gun_icon
    win.mainloop()

width = loading.winfo_screenwidth()
height = loading.winfo_screenheight()
c_x = int(width/2-1024/2)
c_y = int(height/2-720/2)

loading.geometry(f"1024x720+{c_x}+{c_y}")
loading.resizable(False, False)
loading.config(bg="#15DACB")

a = Image.open("logo.png")
a_r = a.resize((484, 258), Image.LANCZOS)
logo = ImageTk.PhotoImage(a_r)

logo_pic = Label(loading, image=logo, width=484, height=258, bg="#15DACB")
logo_pic.place(x=250, y=170)

lic = Label(loading, text=s, width=60, font=("Helvetica", 15, "bold"), bg="#3B0B39", fg="cyan", highlightbackground="Black", bd=4, highlightthickness=2)
lic.pack(side="bottom", pady=0, ipadx=0) 

p_label = Label(loading, text="loading...", font=("Trebuchet Ms", 20, "bold"), bg="#15DACB", fg="#FFFFFF")
p_label.place(x=280, y=430)

progress = ttk.Progressbar(loading, orient="horizontal", length=500, mode="determinate")
progress.place(x=280, y=480)
loading.overrideredirect(True)
start_loading()
loading.mainloop()
