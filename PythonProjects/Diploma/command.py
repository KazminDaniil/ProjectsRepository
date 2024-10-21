import os
import webbrowser
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, filedialog
def show_documentation():
    filename = 'Документация.html'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)

    webbrowser.open('file://' + filepath)

def create_file(event):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])


def open_file(text_input):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_input.delete('1.0', tk.END)
                text_input.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при открытии файла: {e}")


def save_file(text_input, saved_file_path):
    if saved_file_path:
        save_existing_file(text_input, saved_file_path)
    else:
        save_file_as(text_input)

def save_existing_file(text_input, saved_file_path):
    try:
        with open(saved_file_path, 'w', encoding='utf-8') as file:
            content = text_input.get("1.0", tk.END)
            file.write(content)
        messagebox.showinfo("Файл", f"Файл {saved_file_path} сохранен")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")

def save_file_as(text_input):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                content = text_input.get("1.0", tk.END)
                file.write(content)
            messagebox.showinfo("Файл", f"Файл {file_path} сохранен")
            return file_path
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при сохранении файла: {e}")
    return None


def handle_return(event, text_input):
    cursor_position = text_input.index(tk.INSERT)
    current_line = text_input.get(f"{cursor_position} linestart", cursor_position)

    indentation = ""
    for char in current_line:
        if char == ' ' or char == '\t':
            indentation += char
        else:
            break

    if ':' in current_line:
        indentation += "\t"

    text_input.insert(tk.INSERT, '\n' + indentation)
    return "break"


def show_font_dialog(root, text_input):
    font_dialog = tk.Toplevel(root)
    font_dialog.title("Выбор шрифта")

    # Получить список доступных шрифтов
    font_families = tkfont.families()

    # Создать текстовое поле для поиска шрифта
    font_search_label = tk.Label(font_dialog, text="Найти шрифт:")
    font_search_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    font_search_entry = tk.Entry(font_dialog)
    font_search_entry.grid(row=0, column=1, padx=5, pady=5)

    # Создать список шрифтов
    font_label = tk.Label(font_dialog, text="Шрифт:")
    font_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    font_listbox = tk.Listbox(font_dialog, selectmode=tk.SINGLE)
    for font in font_families:
        font_listbox.insert(tk.END, font)
    font_listbox.grid(row=1, column=1, padx=5, pady=5)

    # Создать текстовое поле для поиска размера шрифта
    size_search_label = tk.Label(font_dialog, text="Найти размер:")
    size_search_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    size_search_entry = tk.Entry(font_dialog)
    size_search_entry.grid(row=0, column=3, padx=5, pady=5)

    # Создать список размеров шрифта
    size_label = tk.Label(font_dialog, text="Размер:")
    size_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")
    size_listbox = tk.Listbox(font_dialog, selectmode=tk.SINGLE)
    for size in range(8, 41):
        size_listbox.insert(tk.END, size)
    size_listbox.grid(row=1, column=3, padx=5, pady=5)

    # Функция для обновления списка шрифтов при вводе текста в поле поиска
    def update_font_list(event):
        search_text = font_search_entry.get().lower()
        font_listbox.delete(0, tk.END)
        for font in font_families:
            if search_text in font.lower():
                font_listbox.insert(tk.END, font)

    # Привязать событие "KeyPress" к обновлению списка шрифтов
    font_search_entry.bind("<KeyRelease>", update_font_list)

    # Функция для обновления списка размеров шрифта при вводе текста в поле поиска
    def update_size_list(event):
        search_text = size_search_entry.get().lower()
        size_listbox.delete(0, tk.END)
        for size in range(8, 41):
            if search_text in str(size):
                size_listbox.insert(tk.END, size)

    # Привязать событие "KeyPress" к обновлению списка размеров шрифта
    size_search_entry.bind("<KeyRelease>", update_size_list)

    # Функция для установки выбранного шрифта
    def set_selected_font(event):
        selected_font = font_listbox.get(font_listbox.curselection())
        font_search_entry.delete(0, tk.END)
        font_search_entry.insert(0, selected_font)

    # Привязать событие клика к установке выбранного шрифта
    font_listbox.bind("<ButtonRelease-1>", set_selected_font)

    # Функция для установки выбранного размера шрифта
    def set_selected_size(event):
        selected_size = size_listbox.get(size_listbox.curselection())
        size_search_entry.delete(0, tk.END)
        size_search_entry.insert(0, selected_size)

    # Привязать событие клика к установке выбранного размера шрифта
    size_listbox.bind("<ButtonRelease-1>", set_selected_size)

    # Функция для установки выбранного шрифта и размера
    # Функция для установки выбранного шрифта и размера
    def set_font():
        selected_font = font_search_entry.get()  # Получить значение из текстового поля для поиска шрифта
        selected_size = size_search_entry.get()  # Получить значение из текстового поля для поиска размера шрифта
        if selected_font == "":
            selected_font = "Courier New"
        if selected_size == "":
            selected_size = 10
        text_input.config(font=(selected_font, selected_size))
        print(selected_font, selected_size)

    # Кнопка для установки выбранного шрифта и размера
    set_button = tk.Button(font_dialog, text="Установить", command=set_font)
    set_button.grid(row=2, columnspan=2, padx=5, pady=10)
