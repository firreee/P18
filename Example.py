import sys
from tkinter import Tk, Label, Text, Button, Frame

def calc_miles():
    global error_msg, km_entry, miles_entry
    error_msg.delete("1.0", "end")  
    try:
        kilometers = float(km_entry.get("1.0", "end-1c"))
        if kilometers <= 0:
            raise ValueError("Kilometers must be greater than zero")
        miles = kilometers * 0.62137
        miles_entry.delete("1.0", "end")
        miles_entry.insert("end", f"{miles:.2f}")
    except ValueError as e:
        error_msg.insert("end", str(e))  

def clear_fields():
    km_entry.delete("1.0", "end")
    miles_entry.delete("1.0", "end")
    error_msg.delete("1.0", "end")  

def quit_app():
    winmain.destroy()
    sys.exit()

def main():
    global error_msg, km_entry, miles_entry, winmain
    winmain = Tk()
    winmain.geometry('800x600+600+300')
    winmain.title("Kilometers to Miles Converter")
    winmain.configure(bg='#000000')  

    lbltext = Label(winmain, text="Kilometers to Miles Converter", font=("Roboto", 30), bg='#000000', fg='#FFFFFF')
    lbltext.pack(pady=20)  

    km_frame = Frame(winmain, bg='#000000')
    km_frame.pack(pady=20)  

    km_label = Label(km_frame, text="Kilometers:", bg='#000000', fg='#FFFFFF', width=10)  
    km_label.grid(row=0, column=0, padx=10)  

    km_entry = Text(km_frame, height=1, width=25)
    km_entry.grid(row=0, column=1, padx=10)  

    miles_frame = Frame(winmain, bg='#000000')
    miles_frame.pack()  

    miles_label = Label(miles_frame, text="Miles:", bg='#000000', fg='#FFFFFF', width=10)  
    miles_label.grid(row=0, column=0, padx=10)  

    miles_entry = Text(miles_frame, height=1, width=25)
    miles_entry.grid(row=0, column=1, padx=10)  

    error_msg = Text(winmain, height=2, width=50, fg="red", bg='#000000')
    error_msg.pack(pady=20)  

    button_frame = Frame(winmain, bg='#000000')
    button_frame.pack()  

    calc_button = Button(button_frame, text="Calc", command=calc_miles, bg='#000000', fg='#FFFFFF')
    calc_button.grid(row=0, column=0, padx=(10, 25), pady=5)  

    clear_button = Button(button_frame, text="Clear", command=clear_fields, bg='#000000', fg='#FFFFFF')
    clear_button.grid(row=0, column=1, padx=(25, 10), pady=5)  

    quit_button = Button(winmain, text="QUIT", command=quit_app, bg='#000000', fg='#FFFFFF')
    quit_button.pack()  

    winmain.mainloop()

main()
