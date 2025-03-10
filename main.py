from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer",bg=YELLOW, fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0: 
        count_down(long_break_sec)
        title_text.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_text.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_text.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min =math.floor(count / 60)
    if count_min < 10:
        count_min =f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count>0:
       global timer
       timer = window.after(10, count_down, count-1)
    else:
        start_count()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PMODORO")
window.config(padx=100,pady=50, bg=YELLOW)


title_text = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME,50))
title_text.grid(column=1, row=0)

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=img)
time_text = canvas.create_text(100,140,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_count)
start.grid(column=0, row=2)
 
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()