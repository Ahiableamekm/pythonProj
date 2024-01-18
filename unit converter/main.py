import tkinter


FONT = ("Arial", 15, "bold")
window = tkinter.Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=300, height=150)
window.config(padx=25, pady=25)

def mile_to_km():
    mile_input = mile_entry.get()
    km_result["text"] = str(round(float(mile_input) * 1.609344))
    


equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

mile_label = tkinter.Label(text="Mile", font=FONT)
mile_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

mile_entry = tkinter.Entry(width=7)
mile_entry.grid(row=0, column=1)

cal_button = tkinter.Button(text="Calculate", command=mile_to_km)
cal_button.grid(row=2, column=1)

km_result = tkinter.Label(text="0", font=FONT)
km_result.grid(row=1, column=1)


window.mainloop()