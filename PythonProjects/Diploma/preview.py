import tkinter as tk
import myparser


class Creation:
    def __init__(self):
        self.preview_window = None

    def create_preview_tk(self, parsed_data):
        default_values = {
            key: None for key in myparser.big_map['Окно']
        }
        for window_data in parsed_data.get('Окно', []):
            for key, value in window_data.items():
                value = myparser.translate_values(key, value)
                if key in default_values:
                    default_values[key] = value

            self.preview_window = tk.Toplevel(bg=default_values['Цвет фона'],
                                              bd=default_values['Ширина границы'],
                                              relief=default_values['Стиль границы'],
                                              highlightcolor=default_values['Цвет границы'],
                                              highlightbackground=default_values['Цвет границы вне фокуса'],
                                              highlightthickness=default_values['Ширина границы вне фокуса'],
                                              cursor=default_values['Курсор'],
                                              padx=default_values['Горизонтальный отступ'],
                                              pady=default_values['Вертикальный отступ'],
                                              takefocus=default_values['Принимать фокус'])

            geometry_str = f"{default_values['Ширина']}x{default_values['Высота']}"
            self.preview_window.geometry(geometry_str)
            self.preview_window.resizable(default_values['Изменять размер'], default_values['Изменять размер'])
            self.preview_window.title(default_values['Заголовок'])

    def create_preview_label(self, parsed_data):
        default_values = {
            key: None for key in myparser.big_map['Метка']
        }
        for i, label_data in enumerate(parsed_data.get('Метка', [])):
            for key, value in label_data.items():
                value = myparser.translate_values(key, value)
                if key in default_values:
                    default_values[key] = value
            preview_label = tk.Label(self.preview_window,
                                     text=default_values['Текст'],
                                     bg=default_values["Цвет фона"],
                                     bd=default_values["Ширина границы"],
                                     relief=default_values["Стиль границы"],
                                     highlightcolor=default_values["Цвет границы"],
                                     highlightbackground=default_values["Цвет границы вне фокуса"],
                                     highlightthickness=default_values["Ширина границы вне фокуса"],
                                     cursor=default_values["Курсор"],
                                     padx=default_values["Горизонтальный отступ"],
                                     pady=default_values["Вертикальный отступ"],
                                     font=default_values["Шрифт"],
                                     fg=default_values["Цвет текста"],
                                     justify=default_values["Выравнивание"],
                                     wraplength=default_values["Длина переноса"],
                                     anchor=default_values["Якорь"],
                                     state=default_values["Состояние"],
                                     takefocus=default_values["Принимать фокус"],
                                     underline=default_values["Подчеркивание"],
                                     activebackground=default_values["Цвет активного фона"],
                                     activeforeground=default_values["Цвет активного текста"],
                                     bitmap=default_values["Имя битмапа"],
                                     disabledforeground=default_values["Цвет текста в отключенном состоянии"],
                                     image=default_values["Изображение"],
                                     textvariable=default_values["Переменная текста"])

            preview_label.place(width=default_values['Ширина'],
                                height=default_values['Высота'],
                                x=default_values['Позиция по горизонтали'],
                                y=default_values['Позиция по вертикали']
                                )

    def create_preview_button(self, parsed_data):
        default_values = {
            key: None for key in myparser.big_map['Кнопка']
        }
        for i, button_data in enumerate(parsed_data.get('Кнопка', [])):
            for key, value in button_data.items():
                value = myparser.translate_values(key, value)
                if key in default_values:
                    default_values[key] = value

            preview_button = tk.Button(self.preview_window,
                                       text=default_values['Текст'],
                                       bg=default_values['Цвет фона'],
                                       bd=default_values['Ширина границы'],
                                       highlightbackground=default_values['Цвет границы вне фокуса'],
                                       image=default_values['Изображение'],
                                       relief=default_values['Стиль границы'],
                                       cursor=default_values['Курсор'],
                                       state=default_values['Состояние'],
                                       default=default_values['По умолчанию'],
                                       disabledforeground=default_values['Фон текста при отключенном состоянии'],
                                       fg=default_values['Цвет текста'],
                                       font=default_values['Шрифт'],
                                       activebackground=default_values['Цвет фона при активном состоянии'],
                                       activeforeground=default_values['Активный текст'],
                                       wraplength=default_values['Длина переноса'],
                                       takefocus=default_values['Принять фокус'],
                                       underline=default_values['Подчеркивание'],
                                       justify=default_values['Выравнивание'],
                                       repeatdelay=default_values['Задержка повтора'],
                                       repeatinterval=default_values['Интервал повтора'],
                                       compound=default_values['Компоновка'])

            preview_button.place(width=default_values['Ширина'],
                                 height=default_values['Высота'],
                                 relx=default_values['Горизонтальный отступ'],
                                 rely=default_values['Вертикальный отступ'],
                                 anchor=default_values['Якорь'],
                                 )

    def create_preview_menu(self, parsed_data):
        preview_menu = tk.Menu(self.preview_window)
        self.preview_window.config(menu=preview_menu)

        for menu_data in parsed_data.get('Меню', []):
            for cascade_data in menu_data['Каскад']:
                cascade_menu = tk.Menu(preview_menu, tearoff=int(cascade_data['Отрыв']))
                preview_menu.add_cascade(label=cascade_data['Текст'], menu=cascade_menu)

                for cascade_item in cascade_data.get("Пункт каскада", []):
                    cascade_menu.add_command(
                        label=cascade_item['Текст'],
                        accelerator=cascade_item.get('Горячая клавиша', '')
                    )

    def create_preview_text(self, parsed_data):
        default_values = {
            key: None for key in myparser.big_map['Текстовое поле']
        }
        for i, text_data in enumerate(parsed_data.get('Текстовое поле', [])):
            for key, value in text_data.items():
                value = myparser.translate_values(key, value)
                if key in default_values:
                    default_values[key] = value

        preview_text = tk.Text(self.preview_window)
        preview_text.place(relx=default_values['Горизонтальный отступ'],
                           rely=default_values['Вертикальный отступ'],
                           relwidth=default_values['Относительная ширина'],
                           relheight=default_values['Относительная высота'])