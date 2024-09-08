# main.py

from tkinter import *
import math
import file_paths
from buttons import setup_buttons
from config import FONT_NAME, GREY


# ---------------------------- CONSTANTS ------------------------------- #

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None
is_paused = False
current_time = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, is_paused 
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    other_label.config(text="Ready to Focus?😉")
    check_mark.config(text="")
    reps = 0
    is_paused = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        other_label.config(text="LONG BREAK 😴")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        other_label.config(text="SHORT BREAK 😌")

    else:
        count_down(work_sec)
        other_label.config(text="FOCUS 🧐")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def  count_down(count):
    global timer, current_time, is_paused
    current_time = count  # Save the current time

    if not is_paused:  # Only count down if not paused
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            timer =  window.after(1000, count_down, count - 1)
        else:
            start_timer()
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✓"
            check_mark.config(text=marks)

# ---------------------------- PAUSE AND RESUME MECHANISM ------------------------------- #

def pause_timer(event):
    pause_label.config(image=clicked_pause_img)  # Change image on click
    window.after(150, lambda: pause_label.config(image=pause_img)) # Reset image after 150ms
    global is_paused
    is_paused = True

def resume_timer(event):
    resume_label.config(image=clicked_resume_img)  # Change image on click
    window.after(150, lambda: resume_label.config(image=resume_img)) # Reset image after 150ms
    global is_paused
    is_paused = False
    count_down(current_time)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREY)
window.minsize(height=600, width=600)

label = Label(text="Focus Keeper", font=(FONT_NAME, 30, "normal"), bg=GREY)
label.grid(column=1, row=0)

other_label = Label(text="Ready to Focus?😉", font=(FONT_NAME, 25, "normal"), bg=GREY)
other_label.grid(column=1, row=4)
# Load and resize the provided image
canvas = Canvas(width=400, height=400, bg=GREY, highlightthickness=0)
canvas.grid(column=1, row=1, pady=20)

img = PhotoImage(file=file_paths.image_path).subsample(2, 2)  # Resizes the image by half
canvas.create_image(235, 230, image=img)

timer_text = canvas.create_text(200, 200, text="00:00", fill="white", font=(FONT_NAME, 40))


# Using image for pause and resume button
pause_img = PhotoImage(file=file_paths.pause_button_image_path)
clicked_pause_img = PhotoImage(file=file_paths.clicked_pause_button_image_path)  # Image when button is clicked

pause_label = Label(image=pause_img, bg=GREY)
pause_label.grid(column=0, row=4)
pause_label.bind("<Button-1>", pause_timer)

resume_img = PhotoImage(file=file_paths.resume_button_image_path)
clicked_resume_img = PhotoImage(file=file_paths.clicked_resume_button_image_path)  # Image when button is clicked


resume_label = Label(image=resume_img, bg=GREY)
resume_label.grid(column=2, row=4)
resume_label.bind("<Button-1>", resume_timer)

# ---------------------------- Buttons Setup ------------------------------- #
start_label, reset_label, start_img, clicked_start_img, reset_img, clicked_reset_img = setup_buttons(
    window,
    canvas,
    start_timer,
    reset_timer,
    file_paths,
    GREY,
    timer_text
)

window.grid_columnconfigure(1, weight=1)
check_mark = Label(font=(FONT_NAME, 20, "normal"), bg=GREY)
check_mark.grid(column=1, row=3)


window.mainloop()


