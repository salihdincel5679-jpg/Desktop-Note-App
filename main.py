from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Note App")
window.geometry("400x400")



Main_frame = Frame(
    window
)
Main_frame.pack(pady=20,
    fill="both",
    expand=True
)
Main_frame.columnconfigure(0, weight=1)

Header_for_note = Label(
    Main_frame,
    text="Note App",
    font=("Arial", 25),
)
Header_for_note.grid(row=0, 
                    column=0,
                    sticky="w"
)

ttk.Separator(Main_frame, orient=HORIZONTAL).grid(row=1, column=0, sticky="ew")

Text_of_Note = Text(Main_frame,
                    bg="gray",
                    fg="white",
                    font=("Arial", 14)                   
)
Text_of_Note.grid(row=2,
                column=0,
                sticky="nsew",
                pady=(20, 0)
)   
Main_frame.rowconfigure(2, weight=1)

window.mainloop()