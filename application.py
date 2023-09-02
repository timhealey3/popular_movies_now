import tkinter as tk
from rottonTomatoes import *
from netflix import *
from imdb import *


def netflix():
    results.pack(fill='both', expand=1)
    main_page.forget()
    text_widget.delete("1.0", "end")
    data = netflix_data()
    x = 0
    text_widget.insert("end", f"Most Popular Netflix Movies\n\n")
    while x < 10:
        text_widget.insert("end", f"{x+1}. {data[x]}\n")
        x += 1


def imdb():
    results.pack(fill='both', expand=1)
    main_page.forget()
    text_widget.delete("1.0", "end")
    data = imdb_data()
    x = 0
    text_widget.insert("end", f"Most Popular IMDB Movies\n\n")
    while x < 10:
        text_widget.insert("end", f"{x+1}. {data[x]}\n")
        x += 1


def rotten():
    results.pack(fill='both', expand=1)
    main_page.forget()
    text_widget.delete("1.0", "end")
    data = rotten_data()
    x = 0
    text_widget.insert("end", f"Most Popular Rotten Tomatoes Movies\n\n")
    while x < 10:
        text_widget.insert("end", f"{x+1}. {data[x]}\n")
        x += 1


def back():
    main_page.pack(fill='both', expand=1)
    results.forget()


def button_hover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


window = tk.Tk()
window.title("Popular Movies Today")

main_page = tk.Frame(window)
results = tk.Frame(window)

# netflix button
frame1 = tk.Button(main_page, width=40, height=12, text="Netflix", bg="red", command=netflix)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# imdb button
frame2 = tk.Button(main_page, width=45, height=12, text="IMDB", bg="yellow", command=imdb)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# rotten tomatoes button
frame3 = tk.Button(main_page, width=45, height=12, text="Rotten Tomatoes", bg="green4", command=rotten)
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# back button
frame4 = tk.Button(results, width=45, height=12, text="Back", bg="light sky blue", command=back)
frame4.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

# results
text_widget = tk.Text(results, height=20, width=50)
text_widget.pack()

main_page.pack(fill='both', expand=1)
button_hover(frame1, "light coral", "red")
button_hover(frame2, "Khaki2", "yellow")
button_hover(frame3, "OliveDrab4", "green4")
button_hover(frame4, "sky blue", "light sky blue")

window.mainloop()
