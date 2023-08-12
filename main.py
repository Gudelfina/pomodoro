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
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(text_timer, text="00:00")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label["text"] += "✓"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=1, row=3)

end = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
end.grid(column=3, row=3)


checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
checkmark_label.config(padx=10, pady=10)
checkmark_label.grid(column=2, row=4)


window.mainloop()
