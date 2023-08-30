import tkinter as tk
from rottonTomatoes import *
from main import *
from imdb import *


def netflix():
    results.pack(fill='both', expand=1)
    main_page.forget()
    text_widget.delete("1.0", "end")
    data = netflix_data()
    print(data)
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
    print(data)
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
    print(data)


def back():
    main_page.pack(fill='both', expand=1)
    results.forget()


window = tk.Tk()
window.title("Popular Movies Today")

main_page = tk.Frame(window)
results = tk.Frame(window)

# netflix button
frame1 = tk.Button(main_page, width=40, height=12, bg="red", command=netflix)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# imdb button
frame2 = tk.Button(main_page, width=45, height=12, bg="yellow", command=imdb)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# rotten tomatoes button
frame3 = tk.Button(main_page, width=45, height=12, bg="green", command=rotten)
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# back button
frame3 = tk.Button(results, width=45, height=12, bg="blue", text="back", command=back)
frame3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

# results
text_widget = tk.Text(results, height=20, width=50)
text_widget.pack()

main_page.pack(fill='both', expand=1)


window.mainloop()
