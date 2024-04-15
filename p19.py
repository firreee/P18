import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Computer Screen")

# Create the canvas for the computer screen
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack()

# Create the rectangle for the computer screen
computer_screen = canvas.create_rectangle(0, 0, 500, 300, fill="lightgray")

# Create the rectangle for the top bar of the computer screen
top_bar = canvas.create_rectangle(0, 0, 500, 25, fill="darkgray")

# Create the text for the filename and path
filename_text = canvas.create_text(250, 12, text="1/1  100% +", fill="black")

# Add extras to the screen (optional)
# You can add more elements to the canvas to create a more complete computer screen look

window.mainloop()
