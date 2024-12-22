import tkinter as tk
from tkinter import ttk 

window = tk.Tk()
# ubah background
window.configure(bg="white")
# adjust size
window.geometry("500x500")
# ubah title
window.title("Program Sapa")

combo = ttk.Combobox(window, values=["Celcius", "Fahrenheit", "Kelvin", "Budi", "Caca", "Dede", "Fifi"])
combo.pack(pady=20, padx=20, fill="x", expand= True)



window.mainloop()