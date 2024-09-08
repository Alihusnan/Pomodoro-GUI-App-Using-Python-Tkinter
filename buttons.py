# buttons.py

from tkinter import Label, PhotoImage

# ---------------------------- BUTTONS ------------------------------- #
def setup_buttons(window, canvas, start_timer, reset_timer, file_paths, grey_color, timer_text):

    
    # Function for handling start click event
    def on_click_start(event):
            start_label.config(image=clicked_start_img)  # Change image on click
            window.after(150, lambda: start_label.config(image=start_img)) # Reset image after 150ms
            start_timer() 


    # Function for handling reset click event
    def on_click_reset(event):
        reset_label.config(image=clicked_reset_img)  # Change image on click
        window.after(150, lambda: reset_label.config(image=reset_img))  # Reset image after 150ms
        canvas.itemconfig(timer_text, text="00:00")
        reset_timer()

    # Using image for start button
    start_img = PhotoImage(file=file_paths.start_button_image_path)
    clicked_start_img = PhotoImage(file=file_paths.clicked_start_button_image_path)  # Image when button is clicked

    # Using image for reset button
    reset_img = PhotoImage(file=file_paths.reset_button_image_path)
    clicked_reset_img = PhotoImage(file=file_paths.clicked_reset_button_image_path)  # Image when button is clicked


    # Start and Reset buttons (placed below the image) using Label widgets with event bindings
    start_label = Label(image=start_img, bg=grey_color)
    start_label.grid(column=0, row=3, pady=(0, 30))
    start_label.bind("<Button-1>", on_click_start)  # Bind left-click to simulate button click

    reset_label = Label(image=reset_img, bg=grey_color)
    reset_label.grid(column=2, row=3, pady=(0, 30))
    reset_label.bind("<Button-1>", on_click_reset)  # Bind left-click to simulate button click


    # Return button references and images to avoid garbage collection
    return start_label, reset_label, start_img, clicked_start_img, reset_img, clicked_reset_img

