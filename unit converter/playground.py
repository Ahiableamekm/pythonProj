def add(*args):
    result = 0
    for n in args:
        result += n

    return result

def button_clicked():
    my_label['text'] = entry.get()


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)




my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

my_label['text'] = "New text"
my_label.config(text="New text")



my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(row=1, column=1)

an_button = tkinter.Button(text="Try me", command=button_clicked)
an_button.grid(row=0, column=2)


entry = tkinter.Entry(width=10)
entry.grid(row=2, column=3)


print(add(2, 5, 7, 8, 9 , 0, 2))