import tkinter as tk

param_winn = tk.Tk()
param_winn.title("Параметры")
label = tk.Label(param_winn, text="Ключ:")
label.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(param_winn)
entry1.grid(row=0, column=1, padx=10, pady=10)
button1 = tk.Button(param_winn, text="Изменить ключ")
button1.grid(row=0, column=2, padx=10, pady=10)
label1 = tk.Label(param_winn, text="Размер шрифта")
label1.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(param_winn)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry2.insert(0, x)
button2 = tk.Button(param_winn, text="Изменить размер шрифта")
button2.grid(row=1, column=2, padx=10, pady=10)
radio_frame = tk.Frame(param_winn)
radio_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
radio_var = tk.StringVar()
radio_var.set("Arial")
option1 = tk.Radiobutton(radio_frame, text="Arial", variable=radio_var, value="Arial")
option1.pack(anchor="w")
option2 = tk.Radiobutton(radio_frame, text="Helvetica", variable=radio_var, value="Helvetica")
option2.pack(anchor="w")
option3 = tk.Radiobutton(radio_frame, text="Verdana", variable=radio_var, value="Verdana")
option3.pack(anchor="w")


param_winn.mainloop()
