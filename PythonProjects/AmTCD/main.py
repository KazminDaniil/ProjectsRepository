from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font

import funk
from funk import *
from funk import _get_KeyU_

file_path = None
KeyO = 11
bufer = []


root = Tk()
root.title('AmTCD.txt')
root.geometry('660x405')
def _click_to_destroy_():
    answer = messagebox.askokcancel("Выход", "Вы точно хотате выйти?")
    if answer:
        root.destroy()
def _click_to_destroy_event_(event):
    answer = messagebox.askokcancel("Выход", "Вы точно хотате выйти?")
    if answer:
        root.destroy()
def _modal_win_():
    messagebox.showinfo("О программе", "Программа для 'прозрачного шифрования' (c) Pavlov G.E., Russia, 2023")
def _no_modal_win_():
    nmw = Tk()
    nmw.title('Справка')
    nmw.geometry("600x300")
    nmw_text = Frame(nmw)
    nmw_text.pack(fill=BOTH, expand=1)
    nmw_label = Text(nmw_text, bg='white', fg='black', padx=10, pady=10, wrap=WORD, spacing3=10, width=30)
    nmw_label.pack(expand=1, fill=BOTH, side=LEFT)
    nmw_label.insert(INSERT, spravka_text)
    nmw_label.configure(state='disabled')
    nmw_butt = Button(nmw_label, text="Закрыть", command=nmw.destroy)
    nmw_butt.pack(expand=1, anchor=SE)
def _chenge_KeyU_(entry1):
    text = entry1.get()
    if text:
        if str(text).isdigit():
            funk._save_keyU_(text)
        else:
            messagebox.showinfo("Ошибка", "Поле должно содержать число")
    else:
        messagebox.showinfo("Ошибка", "Поле пустое")
    entry1.delete(0, 'end')
def _change_size_(num):
    if num:
        if str(num).isdigit():
            current_font = text_fild["font"]
            font_family = font.Font(font=current_font).actual()['family']
            new_font_size = num
            new_font = (font_family, new_font_size)
            text_fild.configure(font=new_font)
            #text_fild.configure(yscrollcommand=scrollbar.set)
        else:
            messagebox.showinfo("Ошибка", "Поле должно содержать число")
    else:
        messagebox.showinfo("Ошибка", "Поле пустое")
def _change_font_(radio_var):
    selected_font = radio_var.get()
    current_font = text_fild["font"]
    font_size = font.Font(font=current_font).actual()['size']
    new_font = (selected_font, font_size)
    text_fild.configure(font=new_font)
def _params_():
    param_winn = Tk()
    param_winn.title("Параметры")
    label = Label(param_winn, text="Ключ:")
    label.grid(row=0, column=0, padx=10, pady=10)
    entry1 = Entry(param_winn)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    button1 = Button(param_winn, text="Изменить ключ", command= lambda: _chenge_KeyU_(entry1))
    button1.grid(row=0, column=2, padx=10, pady=10)
    label1 = Label(param_winn, text="Размер шрифта")
    label1.grid(row=1, column=0, padx=10, pady=10)
    entry2 = Entry(param_winn)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    button2 = Button(param_winn, text="Изменить размер шрифта", command= lambda: _change_size_(entry2.get()))
    button2.grid(row=1, column=2, padx=10, pady=10)
    radio_frame = Frame(param_winn)
    radio_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    radio_var = StringVar()
    radio_var.set("Arial")
    option1 = Radiobutton(radio_frame, text="Arial", variable=radio_var, value="Arial", command= lambda: _change_font_(radio_var))
    option1.pack(anchor="w")
    option2 = Radiobutton(radio_frame, text="Helvetica", variable=radio_var, command= lambda: _change_font_(radio_var))
    option2.pack(anchor="w")
    option3 = Radiobutton(radio_frame, text="Verdana", variable=radio_var, command= lambda: _change_font_(radio_var))
    option3.pack(anchor="w")
def _copy_():
    selected_text = text_fild.get("sel.first", "sel.last")
    root.clipboard_clear()
    root.clipboard_append(selected_text)
    print(selected_text)
def _paste_():
    text = root.clipboard_get()
    text_fild.insert(INSERT, text)
def _save_file_kak_():
    global file_path
    global KeyO
    print("Начало _save_file_kak_: ", file_path)
    file_path = filedialog.asksaveasfilename(title="Выбор файла",
                                             filetypes=(("Текстовые документы (*.txt)", "*txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'w', encoding='utf-8')
    KeyU = int(_get_KeyU_())
    print("Print KeyU: ", KeyU)
    Key = KeyU * int(KeyO)
    print("Print Key: ", Key)
    S = text_fild.get('1.0', END)
    SS = funk.codeText(S, Key)
    f.write("[mess]" + '\n' + "[keyopen] = " + str(KeyO) + '\n' + "[mess] = " + SS)
    f.close()
def _save_file_():
    global file_path
    global KeyO
    print("Начало _save_file_: ", file_path)
    if file_path == None:
        _save_file_kak_()
    else:
        print('Proverka')
        f = open(file_path, 'w', encoding='utf-8')
        KeyU = int(_get_KeyU_())
        #print("Print KeyU: ", KeyU)
        Key = KeyU * int(KeyO)
        #print("Print Key: ", Key)
        S = text_fild.get('1.0', END)
        SS = funk.codeText(S, Key)
        f.write("[mess]" + '\n' + "[keyopen] = " + str(KeyO) + '\n' + "[mess] = " + SS)
        f.close()
def _save_file_event_(event):
    global file_path
    global KeyO
    print("Начало _save_file_: ", file_path)
    if file_path == None:
        _save_file_kak_()
    else:
        print('Proverka')
        f = open(file_path, 'w', encoding='utf-8')
        KeyU = int(_get_KeyU_())
        #print("Print KeyU: ", KeyU)
        Key = KeyU * int(KeyO)
        #print("Print Key: ", Key)
        S = text_fild.get('1.0', END)
        SS = funk.codeText(S, Key)
        f.write("[mess]" + '\n' + "[keyopen] = " + str(KeyO) + '\n' + "[mess] = " + SS)
        f.close()
def _open_file_():
    global file_path
    global KeyO
    print("Начало _open_file_: ", file_path)
    file_path = filedialog.askopenfilename(title="Выбор файла",
                                           filetypes=(("Текстовые документы (*.txt)", "*txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'r', encoding='utf-8')
    f.readline()
    f.readline()
    f.readline(9)
    KeyU = int(_get_KeyU_())
    #print("Print KeyU: ", KeyU)
    Key = KeyU * int(KeyO)
    #print("Print Key: ", Key)
    S = funk.codeText(f.readline(), Key)
    if file_path != None:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', S)
    print("Файл открыт: " + file_path)
def _open_file_event_(event):
    global file_path
    global KeyO
    print("Начало _open_file_: ", file_path)
    file_path = filedialog.askopenfilename(title="Выбор файла",
                                           filetypes=(("Текстовые документы (*.txt)", "*txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'r', encoding='utf-8')
    f.readline()
    f.readline()
    f.readline(9)
    KeyU = int(_get_KeyU_())
    #print("Print KeyU: ", KeyU)
    Key = KeyU * int(KeyO)
    #print("Print Key: ", Key)
    S = funk.codeText(f.readline(), Key)
    if file_path != None:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', S)
    print("Файл открыт: " + file_path)

def _new_btn_clicked_(entry, new_win):
    global file_path
    file_path_tmp = file_path
    file_path = entry.get()
    new_win.destroy()
    print(file_path)
def _create_new_():
    global file_path
    global indikator
    text_fild.delete('1.0', END)
    new_win = Tk()
    new_win.title('Новый файл')
    new_win.geometry("200x75")
    text = Label(new_win, text="Имя файла: ").grid(column=0, row=0)
    btn = Button(new_win, text="Принять", command= lambda: _new_btn_clicked_(entry, new_win)).grid(column=1, row=1)
    entry = Entry(new_win, width=20)
    entry.grid(column=0, row=1)
def _create_new_event_(event):
    global file_path
    global indikator
    text_fild.delete('1.0', END)
    new_win = Tk()
    new_win.title('Новый файл')
    new_win.geometry("200x75")
    text = Label(new_win, text="Имя файла: ").grid(column=0, row=0)
    btn = Button(new_win, text="Принять", command= lambda: _new_btn_clicked_(entry, new_win)).grid(column=1, row=1)
    entry = Entry(new_win, width=20)
    entry.grid(column=0, row=1)
def update_statusbar(event):
    cursor_pos = text_fild.index(INSERT)
    statusbar.config(text="Курсор: {}".format(cursor_pos))


root_menu = Menu()
root.config(menu=root_menu)
root.resizable(width=False, height=False)

file_menu = Menu(root_menu, tearoff=0)
file_menu.add_command(label="Новый           Ctrl+N", command=_create_new_)
file_menu.add_command(label="Открыть         Ctrl+O", command=_open_file_)
file_menu.add_command(label="Сохранить       Ctrl+S", command=_save_file_)
file_menu.add_command(label="Сохранить как...      ", command=_save_file_kak_)
file_menu.add_separator()
file_menu.add_command(label="Выход           Ctrl+Q", command=_click_to_destroy_)

pravka_menu = Menu(root_menu, tearoff=0)
pravka_menu.add_command(label="Копировать", command=_copy_)
pravka_menu.add_command(label="Вставить", command=_paste_)
pravka_menu.add_separator()
pravka_menu.add_command(label="Параметры...", command=_params_)

spravka_menu = Menu(root_menu, tearoff=0)
spravka_menu.add_command(label="Содержание", command=_no_modal_win_)
spravka_menu.add_separator()
spravka_menu.add_command(label="О программе...", command=_modal_win_)

root_menu.add_cascade(label="Файл", menu=file_menu)
root_menu.add_cascade(label="Правка", menu=pravka_menu)
root_menu.add_cascade(label="Справка", menu=spravka_menu)

f_text = Frame(root)
f_text.grid(sticky="nsew")

text_fild = Text(f_text)
text_fild.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(f_text, command=text_fild.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
text_fild.config(yscrollcommand=scrollbar.set)

statusbar = Label(root, text="Курсор: 1.0", bd=1, relief=SUNKEN, anchor=W)
statusbar.grid(row=1, column=0, sticky="we")

root.grid_columnconfigure(0, weight=1)

root.bind("<KeyRelease>", update_statusbar)
root.bind("<Motion>", update_statusbar)

root.bind("<Control-Key-q>", _click_to_destroy_event_)
root.bind("<Control-Key-n>", _create_new_event_)
root.bind("<Control-Key-o>", _open_file_event_)
root.bind("<Control-Key-s>", _save_file_event_)

root.mainloop()