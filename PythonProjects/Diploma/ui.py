import tkinter as tk
import myparser
import command

dictionary = {"Окно:", "Ширина", "Высота", "Кнопка:", "=", "200", "500"}

def delayed_check():
    text_input.tag_remove("highlight", "1.0", "end")
    input_text = text_input.get("1.0", "end-1c").strip()
    words = input_text.split()

    for word in words:
        start_idx = input_text.find(word)
        if word not in dictionary:
            start_pos = f"1.0 + {start_idx} chars"
            end_pos = f"{start_pos} + {len(word)} chars"
            highlight_word(start_pos, end_pos)

def highlight_word(start, end):
    text_input.tag_add("highlight", start, end)
    text_input.tag_configure("highlight", underline=True, underlinefg="red")

def on_key_release(event):
    text_input.after(2000, delayed_check)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
root = tk.Tk()
root.title("Главное окно")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Настройки", menu=settings_menu)
settings_menu.add_command(label="Шрифт", command=lambda: command.show_font_dialog(root, text_input))

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Создать", command=command.create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Открыть", command=lambda: command.open_file(text_input), accelerator="Ctrl+O")
file_menu.add_command(label="Сохранить", command=lambda: command.save_file(text_input), accelerator="Ctrl+S")
file_menu.add_command(label="Сохранить как", command=lambda: command.save_file_as(text_input),
                      accelerator="Ctrl+Shift+S")


help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="О программе", command=command.show_documentation)

text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)


text_input = tk.Text(text_frame, wrap=tk.WORD)
text_input.pack(fill=tk.BOTH, expand=True)

tab_size = 32
text_input.configure(tabs=(tab_size,))
text_input.bind("<Return>", lambda event: command.handle_return(event, text_input))

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

preview_button = tk.Button(button_frame, text="Предпросмотр", command=lambda: myparser.parse_input(text_input.get("1.0", tk.END), 1))
preview_button.pack(side=tk.LEFT)

code_button = tk.Button(button_frame, text="Получить код", command=lambda: myparser.parse_input(text_input.get("1.0", tk.END), 2))
code_button.pack(side=tk.LEFT, padx=10)

root.geometry("900x600")
root.resizable(False, False)
#text_input.bind("<KeyRelease>", on_key_release)
text_input.bind("<Control-n>", command.create_file)
root.mainloop()
