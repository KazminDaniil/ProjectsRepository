import hmac
import hashlib
from preview import Creation
import secrets
import time

big_map = {
    "Окно": ["Высота", "Горизонтальный отступ", "Цвет фона", "Изменять размер", "Курсор", "Стиль границы",
             "Ширина", "Ширина границы", "Цвет границы", "Цвет границы вне фокуса", "Ширина границы вне фокуса",
             "Вертикальный отступ", "Заголовок", "Принимать фокус"],
    "Кнопка": ["Текст", "Ширина", "Высота", "Цвет фона", "Ширина границы", "Цвет границы вне фокуса", "Изображение",
               "Стиль границы", "Курсор", "Горизонтальный отступ", "Вертикальный отступ", "Состояние", "По умолчанию",
               "Фон текста при отключенном состоянии", "Цвет текста", "Шрифт", "Цвет фона при активном состоянии",
               "Активный текст", "Якорь", "Длина переноса", "Принять фокус", "Подчеркивание", "Выравнивание",
               "Задержка повтора", "Интервал повтора", "Компоновка", "Разместить", "Позиция по горизонтали", "Позиция по вертикали"],
    "Метка": ["Цвет активного фона", "Цвет активного текста", "Выравнивание", "Высота", "Вертикальный отступ",
              "Горизонтальный отступ", "Длина переноса", "Изображение", "Имя", "Имя битмапа", "Компоновка", "Курсор",
              "Переменная текста", "Подчеркивание", "Принимать фокус", "Состояние", "Стиль границы", "Текст",
              "Цвет фона", "Цвет границы", "Цвет границы вне фокуса",
              "Цвет текста", "Цвет текста в отключенном состоянии", "Ширина", "Ширина границы",
              "Ширина границы вне фокуса", "Шрифт", "Якорь", "Разместить", "Позиция по горизонтали", "Позиция по вертикали"],
    "Меню": [],
    "Каскад": ["Текст", "Отрыв"],
    "Пункт каскада": ["Текст", "Горячая клавиша"],
    "Текстовое поле": ["Горизонтальный отступ", "Вертикальный отступ", "Относительная ширина", "Относительная высота"]
}
translation_dict = {
    'Цвет':
        {'красный': 'red', 'синий': 'blue', 'зелёный': 'green', 'жёлтый': 'yellow', 'оранжевый': 'orange',
         'фиолетовый': 'purple', 'розовый': 'pink', 'чёрный': 'black', 'белый': 'white', 'серый': 'gray',
         'коричневый': 'brown', 'голубой': 'cyan', 'бирюзовый': 'turquoise', 'золотой': 'gold', 'серебряный': 'silver'},
    'Стиль границы':
        {'приподнятый': 'raised', 'вдавленный': 'sunken', 'плоский': 'flat', 'ребристый': 'ridge', 'сплошной': 'solid',
         'борозда': 'groove'},
    'Цвет границы вне фокуса':
        {'красный': 'red', 'синий': 'blue', 'зелёный': 'green', 'жёлтый': 'yellow', 'оранжевый': 'orange',
         'фиолетовый': 'purple', 'розовый': 'pink', 'чёрный': 'black', 'белый': 'white', 'серый': 'gray',
         'коричневый': 'brown', 'голубой': 'cyan', 'бирюзовый': 'turquoise', 'золотой': 'gold', 'серебряный': 'silver'},
    'Курсор':
        {'Х-курсор': 'X_cursor', 'рука2': 'hand2', 'левый указатель': 'left_ptr'},
    'Изменять размер':
        {'да': True, 'нет': False},
    'Принимать фокус':
        {'да': True, 'нет': False},
    'Выравнивание':
        {'лево': 'left', 'центр': 'center', 'право': 'right'},
    'Якорь':
        {'центр': 'center', 'север': 'n', 'северо-восток': 'ne', 'восток': 'e', 'юго-восток': 'se', 'юг': 's',
         'юго-запад': 'sw', 'запад': 'w', 'северо-запад': 'nw'},
    'Состояние':
        {'активно': 'active', 'отключено': 'disabled', 'нормальное': 'normal'},
    'По умолчанию':
        {'активно': 'active', 'отключено': 'disabled', 'нормальное': 'normal'},
    'Подчеркивание':
        {'нет': -1}

}
code_operations = {
    'Цвет фона': lambda value: f'bg="{value}"',
    'Ширина границы': lambda value: f'bd={value}',
    'Стиль границы': lambda value: f'relief="{value}"',
    'Цвет границы': lambda value: f'highlightcolor="{value}"',
    'Цвет границы вне фокуса': lambda value: f'highlightbackground="{value}"',
    'Ширина границы вне фокуса': lambda value: f'highlightthickness={value}',
    'Курсор': lambda value: f'cursor="{value}"',
    'Текст': lambda value: f'text="{value}"',
    'Состояние': lambda value: f'state="{value}"',
    'Принимать фокус': lambda value: f'takefocus={value}',
    'Подчеркивание': lambda value: f'underline={value}',
    'Шрифт': lambda value: f'font="{value}"',
    'Цвет текста': lambda value: f'fg="{value}"',
    'Выравнивание': lambda value: f'justify="{value}"',
    'Длина переноса': lambda value: f'wraplength={value}'
}
extra_code_operations = {
    'Заголовок': lambda value: f'root.title("{value}")',
    'Изменять размер': lambda value: f'root.resizable{value, value}'
}
place_operations = {
    'Ширина': lambda value: f'width={value}',
    'Высота': lambda value: f'height={value}',
    'Позиция по горизонтали': lambda value: f'x={value}',
    'Позиция по вертикали': lambda value: f'y={value}',
    'Горизонтальный отступ': lambda value: f'relx={value}',
    'Вертикальный отступ': lambda value: f'rely={value}',
    'Относительная ширина': lambda value: f'relwidth={value}',
    'Относительная высота': lambda value: f'relheight={value}',
    'Якорь': lambda value: f'anchor="{value}"'
}
add_cascade_operations = {
    'Отрыв': lambda value: f'tearoff={value}'
}
cascade_operations = {
    'Текст': lambda value: f'label="{value}"',
    'Горячая клавиша': lambda value: f'accelerator="{value}"'
}



def translate_values(key, value):
    if key in ['Цвет фона', 'Цвет границы', 'Цвет границы вне фокуса', 'Цвет текста', 'Цвет активного фона',
               'Цвет активного текста', 'Фон текста при отключенном состоянии']:
        return translation_dict.get('Цвет', {}).get(value, value)
    else:
        return translation_dict.get(key, {}).get(value, value)



SECRET_KEY = secrets.token_bytes(32)  # секретный ключ для подписи


def create_signature(data, key):
    serialized_data = str(sorted(data.items())).encode()  # сериализация и сортировка данных
    return hmac.new(key, serialized_data, hashlib.sha256).hexdigest()


def verify_signature(data, key, signature):
    expected_signature = create_signature(data, key)
    return hmac.compare_digest(expected_signature, signature)


def create_preview_window(parsed_data, start_time):
    instance = Creation()
    signature = parsed_data.pop('signature', None)
    if not signature or not verify_signature(parsed_data, SECRET_KEY, signature):
        print("Ошибка: данные окна были изменены или подпись неверна!")
        return

    if 'Окно' in parsed_data:
        instance.create_preview_tk(parsed_data)
    if 'Метка' in parsed_data:
        instance.create_preview_label(parsed_data)
    if 'Кнопка' in parsed_data:
        instance.create_preview_button(parsed_data)
    if 'Меню' in parsed_data:
        instance.create_preview_menu(parsed_data)
    if 'Текстовое поле' in parsed_data:
        instance.create_preview_text(parsed_data)

    end_time = time.time()
    initialization_time = end_time - start_time
    print(f"Время инициализации: {initialization_time:} секунд")

def parse_input(input_text, button_value):
    start_time = time.time()
    lines = input_text.expandtabs(4).strip().split('\n')
    parsed_data = {}
    stack = [parsed_data]
    indent_levels = [0]
    current_section = None

    for i, line in enumerate(lines, start=1):
        indent_level = len(line) - len(line.lstrip(' '))

        if indent_level > indent_levels[-1]:
            indent_levels.append(indent_level)
        elif indent_level < indent_levels[-1]:
            while indent_levels and indent_level < indent_levels[-1]:
                indent_levels.pop()
                stack.pop()

        if ':' in line:
            current_section = line.replace(':', '').strip()
            new_section = {}
            if current_section not in stack[-1]:
                stack[-1][current_section] = []
            stack[-1][current_section].append(new_section)
            stack.append(new_section)
        else:
            key, value = map(lambda x: x.strip().strip('"'), line.split('='))
            if isinstance(stack[-1], dict):
                stack[-1][key] = value

    signature = create_signature(parsed_data, SECRET_KEY)
    parsed_data['signature'] = signature  # добавление подписи в parsed_data
    if button_value == 1:
        create_preview_window(parsed_data, start_time)
    else:
        generate_tkinter_code(parsed_data)

def generate_tkinter_code(parsed_data):
    signature = parsed_data.pop('signature', None)
    try:
        if not signature or not verify_signature(parsed_data, SECRET_KEY, signature):
            print("Ошибка: данные окна были изменены или подпись неверна!")
    except:
        print("error")

    code = []
    code_arguments = []
    code_extra_arguments = []

    code.append("import tkinter as tk")

    if 'Окно' in parsed_data:
        width = None
        height = None
        for window_data in parsed_data['Окно']:
            for key, value in window_data.items():
                value = translate_values(key, value)
                if key == 'Ширина':
                    width = value
                elif key == 'Высота':
                    height = value
                elif key in code_operations:
                    code_arguments.append(code_operations[key](value))
                elif key in extra_code_operations:
                    code_extra_arguments.append(extra_code_operations[key](value))

            code.append("root = tk.Tk()")
            if code_arguments:
                code.append("root.config(" + ", ".join(code_arguments) + ")")
            if width and height:
                code_extra_arguments.append(f'root.geometry("{width}x{height}")')
            code.extend(code_extra_arguments)

    if 'Метка' in parsed_data:
        for i, label_data in enumerate(parsed_data['Метка']):
            code_arguments = []
            code_extra_arguments = []
            place_arguments = []
            if i == 0:
                widget_name = "label"
            else:
                widget_name = f"label{i + 1}"
            for key, value in label_data.items():
                value = translate_values(key, value)
                if key in code_operations:
                    code_arguments.append(code_operations[key](value))
                elif key in extra_code_operations:
                    code_extra_arguments.append(extra_code_operations[key](value))
                elif key in place_operations:
                    place_arguments.append(place_operations[key](value))

            code.append(f"{widget_name} = tk.Label(root, " + ", ".join(code_arguments) + ")")
            code.append(f"{widget_name}.place(" + ", ".join(place_arguments)+")")
            code.extend(code_extra_arguments)

    if 'Кнопка' in parsed_data:
        for i, button_data in enumerate(parsed_data['Кнопка']):
            code_arguments = []
            code_extra_arguments = []
            place_arguments = []
            if i == 0:
                widget_name = "button"
            else:
                widget_name = f"button{i + 1}"

            for key, value in button_data.items():
                value = translate_values(key, value)
                if key in code_operations:
                    code_arguments.append(code_operations[key](value))
                elif key in extra_code_operations:
                    code_extra_arguments.append(extra_code_operations[key](value))
                elif key in place_operations:
                    place_arguments.append(place_operations[key](value))

            code.append(f"{widget_name} = tk.Button(root, " + ", ".join(code_arguments) + ")")
            code.append(f"{widget_name}.place(" + ", ".join(place_arguments)+")")
            code.extend(code_extra_arguments)

    if 'Меню' in parsed_data:
        for i, menu_data in enumerate(parsed_data['Меню']):
            menu_arguments = []
            cascade_definitions = []
            widget_name = "menu" if i == 0 else f"menu{i + 1}"

            code.append(f"{widget_name} = tk.Menu(root)")
            code.append(f"root.config(menu={widget_name})")

            for key, value in menu_data.items():
                if key == "Каскад":
                    for j, cascade_data in enumerate(value):
                        cascade_arguments = []
                        add_cascade_arguments = []
                        cascade_name = "cascade" if j == 0 else f"cascade{j + 1}"
                        for key2, value2 in cascade_data.items():
                            if key2 == "Пункт каскада":
                                for cascade_command in value2:
                                    command_arguments = []
                                    for key3, value3 in cascade_command.items():
                                        if key3 in cascade_operations:
                                            command_arguments.append(cascade_operations[key3](value3))
                                    cascade_definitions.append((cascade_name, command_arguments))
                            elif key2 in cascade_operations:
                                cascade_arguments.append(cascade_operations[key2](value2))
                            elif key2 in add_cascade_operations:
                                add_cascade_arguments.append(add_cascade_operations[key2](value2))

                        code.append(f"{cascade_name} = tk.Menu({widget_name}, " + ", ".join(add_cascade_arguments) + ")")

                        code.append(
                            f"{widget_name}.add_cascade(" + ", ".join(cascade_arguments) + f", menu={cascade_name})")

            for cascade_name, command_args in cascade_definitions:
                code.append(f"{cascade_name}.add_command(" + ", ".join(command_args) + ")")

    if 'Текстовое поле' in parsed_data:
        for i, text_data in enumerate(parsed_data['Текстовое поле']):
            code_arguments = []
            code_extra_arguments = []
            place_arguments = []
            if i == 0:
                widget_name = "text"
            else:
                widget_name = f"text{i + 1}"

            for key, value in text_data.items():
                value = translate_values(key, value)
                if key in code_operations:
                    code_arguments.append(code_operations[key](value))
                elif key in extra_code_operations:
                    code_extra_arguments.append(extra_code_operations[key](value))
                elif key in place_operations:
                    place_arguments.append(place_operations[key](value))

            code.append(f"{widget_name} = tk.Text(root" + ", ".join(code_arguments) + ")")
            code.append(f"{widget_name}.place(" + ", ".join(place_arguments) + ")")
            code.extend(code_extra_arguments)

    code.append("root.mainloop()")
    print("########################")
    print("\n".join(code))
