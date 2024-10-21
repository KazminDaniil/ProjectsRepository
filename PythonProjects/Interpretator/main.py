# Цикл ввода переменных и меток
from tkinter import *
from tkinter.messagebox import showerror

start_text = ("Начало\n"
              "Переменные: п123 п212 п333 п477 п51 п6 п7 п41\n"   #9
              "Метки: 1 2 3 4 5 Конец меток\n"                    #17
              "4 1 :п333 = 0 и 1 , \n"                            #26
              "1 2:п123=(21+-3)*3, \n"                            #40
              "3 1:п212=((п123+4)*2)*3,\n"                        #57
              "5 : п477 = ( ( 0 и 1 ) или ( п333 и 0 ) ) или 0,\n"
              "2 1  : п51 = ( ( 0 и 1 ) или ( п333 и 0 ) ) или 0\n"#76
              "Конец\n")

# Начальное положение 1.0
global_i_in_file = int(0)
global_j_in_file = int(1)
# Начальное положение 0
global_i_in_splited_str = int(0)
# Массив меток
global_metki_spisok = []
# Массив переменных
global_perem_spisok = []
# На всяк случай
my_str = ""
# Номер переменнаой в списке
global_perem_num = int(0)
global_tmp_str = []


class Perem(object):
    name = {}
    first = int(0)
    last = int(0)
    example = []
    value = int(0)
    i_s = int(0)
    i_e = int(0)
    j_s = int(0)
    j_e = int(0)

    def set_defolt(self):
        self.name = {}
        self.first = int(0)
        self.last = int(0)
        self.example = []
        self.value = int(-123123123123123123123123123)

    def __init__(self, ime):
        self.name = ime

    def get_name(self):
        return str(self.name)

    def get_value(self):
        return self.value

    def get_first(self):
        return (self.first)

    def get_last(self):
        return (self.last)

    def set_first(self, num):
        self.first = num

    def set_last(self, num):
        self.last = num

    def set_i_s(self, num):
        self.i_s = num

    def set_i_e(self, num):
        self.i_e = num

    def set_j_s(self, num):
        self.j_s = num

    def set_j_e(self, num):
        self.j_e = num

    def set_example(self):
        global my_str
        global global_perem_spisok
        show_file_position()
        answ = ""

        print(
            f"-----Запись строки c {self.first} по {self.last} start {self.j_s}.{self.i_s} end {self.j_e}.{self.i_e}------")
        local_str = global_tmp_str
        for n in range(self.first, self.last + 1):
            print(f"Элемент строки n = {n} str = {local_str[n]}")
            if local_str[n] == "и":
                answ += str(" and ")
            elif is_perem(local_str[n], 0):
                indicator = -1
                for i in range(len(global_perem_spisok)):
                    print(str(local_str[n]) + str(global_perem_spisok[i].get_name()))
                    if str(local_str[n]) == str(global_perem_spisok[i].get_name()):
                        indicator = i
                if indicator != -1:
                    if global_perem_spisok[indicator].get_value() != -123123123123123123123123123:
                        if global_perem_spisok[indicator].get_value() != 0:
                            answ += str(convert_base(global_perem_spisok[indicator].get_value(), 8, 10) + " ")
                        else:
                            answ += "0 "
                    else:
                        text.tag_add("highlightline", str(self.j_s) + "." + str(self.i_s),
                                     str(self.j_e) + "." + str(self.i_e))
                        showerror("Ошибка 7.1", "Переменная не имеет значения: " + str(local_str[n]))
                        return False
                else:
                    text.tag_add("highlightline", str(self.j_s) + "." + str(self.i_s),
                                 str(self.j_e) + "." + str(self.i_e))
                    showerror("Ошибка 7.2", "Переменная не объявлена: " + str(local_str[n]))
                    return False
            elif is_integer(local_str[n]):
                if local_str[n] != str("0"):
                    answ += str(convert_base(local_str[n], 8, 10) + " ")
                else:
                    answ += "0 "
            elif local_str[n] == "или":
                answ += str(" or ")
            elif (local_str[n] == '+' or local_str[n] == '-' or local_str[n] == '*' or local_str[n] == '/' or local_str[
                n] == '&' or local_str[n] == '|' or local_str[n] == ')' or local_str[n] == '(' or
                  local_str[n] == ',' or local_str[n] == '.'):
                if local_str[n] == '/':
                    answ += '//'
                else:
                    answ += str(local_str[n] + ' ')

            else:
                text.tag_add("highlightline", str(self.j_s) + "." + str(self.i_s), str(self.j_e) + "." + str(self.i_e))
                showerror("Ошибка 7.3", "Встречен неизвестный символ: " + str(local_str[n]))
                return False
            print(answ)

        try:
            eval(answ)
            if eval(answ) == 0:
                self.value = 0
                print(f"Получилось {self.name}")
                return True
            self.value = convert_base(eval(answ), 10, 8)
            print(f"Получилось {self.name}")
            return True
        except:
            if self.i_e == 0:
                text.tag_add("highlightline", str(self.j_s) + "." + str(self.i_s), str(self.j_e - 1) + "." + str("end"))
                return False
            text.tag_add("highlightline", str(self.j_s) + "." + str(self.i_s), str(self.j_e) + "." + str(self.i_e))
            return False


def find_end_metok(splited_str):
    global global_i_in_splited_str
    i = global_i_in_splited_str
    print(f"len = {len(splited_str)}")
    while i + 1 < len(splited_str) and splited_str[i] != "Конец":
        print(f"i = {i} word = {splited_str[i]}")
        i += 1
    print(str(global_i_in_splited_str) + ' ' + str(i))
    if splited_str[i] == "Конец" and splited_str[i + 1] == "меток" and splited_str[
        global_i_in_splited_str + 1] != "Конец" and i != len(splited_str) - 2:
        return True
    else:
        return False
def add_spaces_around_operators(input_string):
    operators = ['+', '-', '(', ')', '*', '/', ':', ',', '=']
    for operator in operators:
        input_string = input_string.replace(operator, f' {operator} ')
    return input_string
def find_end_papam(splited_str):
    global global_i_in_splited_str
    for i in range(global_i_in_splited_str + 1, len(splited_str)):
        if is_integer(splited_str[i]):
            return True
        elif splited_str[i] == "Переменные:" or splited_str[i] == "Метки:" and global_i_in_splited_str + 1 != i:
            return True
    return False


def convert_base(number, from_base, to_base):
    # Переводим число из исходной системы счисления в десятичную
    decimal_number = int(str(number), from_base)

    # Переводим десятичное число в целевую систему счисления
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = str(remainder) + result
        decimal_number //= to_base

    return result


def show_file_position():
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok

    print(f"file pos = {global_j_in_file}.{global_i_in_file} i = {global_i_in_splited_str}")


def reset_to_defolt():
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global global_metki_spisok
    global global_perem_spisok
    global my_str
    global global_perem_num

    global_j_in_file = int(1)
    global_i_in_file = int(0)
    global_i_in_splited_str = int(0)
    for i in range(len(global_perem_spisok)):
        global_perem_spisok[i].set_defolt()
    global_metki_spisok = []
    global_perem_spisok = []
    my_str = ""
    global_perem_num = int(0)
    print("------------------------------------------------------------")
    print(f"global_j_in_file = {global_j_in_file} '\n' global_i_in_file = {global_i_in_file} '\n'"
          f"global_i_in_splited_str = {global_i_in_splited_str} '\n' global_metki_spisok = {global_metki_spisok} '\n'"
          f"global_perem_spisok = {global_perem_spisok} '\n' my_str = {my_str} '\n'"
          f"global_perem_num = {global_perem_num}")
    print("------------------------------------------------------------")


def is_integer(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False


def is_perem(input_string, perem):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global global_perem_spisok

    if 'А' <= input_string[0] <= 'я':
        if 1 <= len(input_string) <= 4:
            for i in range(1, len(input_string)):
                print(input_string[i], i)
                if not '0' <= input_string[i] <= '9':
                    return False
        else:
            return False
    else:
        return False

    if perem == 1:
        for n in range(len(global_perem_spisok)):
            if global_perem_spisok[n].get_name() == input_string:
                return True

        obj = Perem(input_string)
        global_perem_spisok.append(obj)

    # print(str(global_perem_spisok[len(global_perem_spisok)-1].get_name()))

    return True


def get_position_of_previous_word_start(text_widget):
    global global_j_in_file
    global global_i_in_file
    text_widget.mark_set(INSERT, f'{global_j_in_file}.{global_i_in_file}')

    current_position = text_widget.index(INSERT)
    line, position_in_line = map(int, current_position.split('.'))

    if position_in_line == 0:
        if line > 1:
            # Переместить курсор в конец предыдущей строки
            line -= 1
            text_widget.mark_set(INSERT, f'{line}.end')
            current_position = text_widget.index(INSERT)
            line, position_in_line = map(int, current_position.split('.'))
        else:
            # Курсор уже в начале текста
            return '1.0'

    # Идти назад до первой буквы предыдущего слова
    search_position = f'{line}.{position_in_line - 1}'
    word_start_position = text_widget.search(r'\S+', search_position, stopindex='1.0', regexp=True, backwards=True)

    if word_start_position:
        return word_start_position
    else:
        # Курсор находится в начале текста
        return '1.0'


def update_global_i_j_in_file(string_lenght):
    global global_j_in_file
    global global_i_in_file

    if string_lenght >= 0:
        global_i_in_file += string_lenght
        # Пропуск всех ' ' и \n до следующего слова
        while True:
            # Если следующий пробел
            if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) == ' ':
                # print("Заход в пробелы")
                global_i_in_file += 1
                # Убрать повторяющиеся пробелы
                while True:
                    if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) == ' ':
                        global_i_in_file += 1
                    if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) != ' ':
                        break
            # Если следующий перенос
            if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) == '\n':
                # print("Заход в переносы")
                global_i_in_file = 0
                global_j_in_file += 1
                while True:
                    # Убрать повторяющиеся символы переноса
                    if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) == '\n':
                        global_j_in_file += 1
                    if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) != '\n':
                        # print("break в переносе")
                        break
            # Если дошел до символа
            if text.get(str(global_j_in_file) + "." + str(global_i_in_file)) != '\n' \
                    and text.get(str(global_j_in_file) + "." + str(global_i_in_file)) != ' ':
                print("Break:" + text.get(str(global_j_in_file) + "." + str(global_i_in_file)))
                show_file_position()
                break
    else:
        tmp_j, tmp_i = get_position_of_previous_word_start(text).split('.')
        global_i_in_file = int(tmp_i)
        global_j_in_file = int(tmp_j)


def btn_clicked():
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok
    global start_text

    text.tag_remove("highlightline", "1.0", "end")
    reset_to_defolt()
    my_str = text.get("1.0", "end")
    splited_str = my_str.split()

    if check_string(my_str):  # 1 Проверка на неверные символы
        update_global_i_j_in_file(0)
        if splited_str[global_i_in_splited_str] == "Начало":  # 2 Начало
            update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
            if perem_and_metki(splited_str):  # 3 Переменные и метки
                print("Переменные: ")
                for i in range(len(global_perem_spisok)):
                    print(str(global_perem_spisok[i].get_name()))
                print("Конец переменных")
                print("Метки: ")
                for i in range(len(global_metki_spisok)):
                    print(str(global_metki_spisok[i]))
                print("Конец Меток")
                print(global_i_in_splited_str)
                print("Начало операторов")
                if operator(splited_str):
                    print("-----Вывод переменных-----")
                    for i in range(len(global_perem_spisok)):
                        if (global_perem_spisok[i].get_first() != 0 and global_perem_spisok[i].get_last() != 0):
                            print(str(global_perem_spisok[i].get_name()) + " = " + str(
                                global_perem_spisok[i].get_value()))
                        else:
                            print(f" Переменная: {str(global_perem_spisok[i].get_name())} не используется")
                else:
                    text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),str(global_j_in_file) + "." + str(global_i_in_file + len(splited_str[global_i_in_splited_str])-1))
                    print(splited_str[global_i_in_splited_str])
                    showerror("Ошибка 3.0", "Нарушение синтаксиса <<Оператор>>")
            else:
                text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),str(global_j_in_file) + "." + str(global_i_in_file + len(splited_str[global_i_in_splited_str])))
                print(splited_str[global_i_in_splited_str])
                showerror("Ошибка 3.0", "Нарушение синтаксиса <<Переменные>> или <<Метки>>")
        else:  # 2
            text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                         str(global_j_in_file) + "." + str(
                             global_i_in_file + len(splited_str[global_i_in_splited_str])))
            showerror("Ошибка 2.0", "Ожидалось: <<Начало>>, Получено: " + splited_str[global_i_in_splited_str])
            reset_to_defolt()
            return False

    # Возвращение к началу после по окончании выполнения программы


def check_string(my_str):  # Проверка на неправильные символы
    i = int(0)
    j = int(1)
    for char in my_str:
        if char == ' ':
            i += 1
        if char == '\n':
            j += 1
            i = 0
        if not char.isspace():
            if char.isdigit():  # Символ является числом
                if not '0' <= char <= '7':
                    text.tag_add("highlightline", str(j) + "." + str(i), str(j) + "." + str(i + 1))
                    showerror('Ошибка_1',
                              'Встречен неверный символ: ' + char + ' ! ' + str(j) + "." + str(i) + ' ' + str(
                                  j) + "." + str(i + 1))
                    reset_to_defolt()
                    return False
            elif char.isalpha():  # Символ является буквой
                if not 'А' <= char <= 'я':
                    text.tag_add("highlightline", str(j) + "." + str(i), str(j) + "." + str(i + 1))
                    showerror('Ошибка_2',
                              'Встречен неверный символ: ' + char + ' ! ' + str(j) + "." + str(i) + ' ' + str(
                                  j) + "." + str(i + 1))
                    reset_to_defolt()
                    return False

            else:  # Символ не является операндом
                if not (
                        char == '+' or char == '-' or char == '*' or char == '/' or char == '&' or char == '|' or char == ')' or char == '(' or char == ':' or char == ',' or char == '.' or char == '='):
                    text.tag_add("highlightline", str(j) + "." + str(i), str(j) + "." + str(i + 1))
                    showerror('Ошибка_3',
                              'Встречен неверный символ: ' + char + ' ! ' + str(j) + "." + str(i) + ' ' + str(
                                  j) + "." + str(i + 1))
                    reset_to_defolt()
                    return False
            i += 1
    return True


def perem_and_metki(splited_str):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global global_metki_spisok

    show_file_position()

    while True:
        update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
        global_i_in_splited_str += 1
        show_file_position()
        indikator = int(0)
        if splited_str[global_i_in_splited_str] == "Переменные:":
            print("Переменные:")
            if not find_end_papam(splited_str):
                text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                             str(global_j_in_file) + "." + str(
                                 global_i_in_file + len(splited_str[global_i_in_splited_str])))
                showerror("Ошибка 3.1", "После переменных ожидалось целое число или <<Переменные:>> или <<Метки:>>")
                return False
            # update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
            while True:
                update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                global_i_in_splited_str += 1
                if not is_perem(splited_str[global_i_in_splited_str], 1):
                    if (splited_str[global_i_in_splited_str] == "Переменные:" or splited_str[
                        global_i_in_splited_str] == "Метки:") and indikator != 0:
                        # update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        global_i_in_splited_str -= 1
                        break
                    elif (splited_str[global_i_in_splited_str] == "Переменные:" or splited_str[
                        global_i_in_splited_str] == "Метки:") and indikator == 0:
                        update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        global_i_in_splited_str -= 1
                        text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                     str(global_j_in_file) + "." + str(
                                         global_i_in_file + len(splited_str[global_i_in_splited_str])))
                        showerror("Ошибка 3.12",
                                  "Должна быть хотябы одна переменная" + splited_str[global_i_in_splited_str + 1])
                        return False
                    elif is_integer(splited_str[global_i_in_splited_str]) and indikator != 0:
                        update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        global_i_in_splited_str -= 1
                        break
                    elif is_integer(splited_str[global_i_in_splited_str]) and indikator == 0:
                        update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        global_i_in_splited_str -= 1
                        text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                     str(global_j_in_file) + "." + str(
                                         global_i_in_file + len(splited_str[global_i_in_splited_str])))
                        showerror("Ошибка 3.11", "Должна быть хотябы одна переменная")
                        return False
                    else:
                        print("            afd             ")
                        show_file_position()
                        update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                     str(global_j_in_file) + "." + str(
                                         global_i_in_file + len(splited_str[global_i_in_splited_str])))
                        showerror("Ошибка 3.3",
                                  "Ожидалась переменная. Полученно: " + splited_str[global_i_in_splited_str])
                        return False
                else:
                    indikator += 1

        elif splited_str[global_i_in_splited_str] == "Метки:":
            print("Метки:")
            if not find_end_metok(splited_str):
                update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                             str(global_j_in_file) + "." + str(
                                 global_i_in_file + len(splited_str[global_i_in_splited_str])))
                showerror("Ошибка 3.2", "После <<Метки:>> ожидается хотя бы одно целое число и <<Конец меток>>")
                return False
            while True:
                update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                global_i_in_splited_str += 1
                if not is_integer(splited_str[global_i_in_splited_str]):
                    if splited_str[global_i_in_splited_str] == "Конец" and splited_str[
                        global_i_in_splited_str + 1] == "меток":
                        update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                        global_i_in_splited_str += 1
                        # update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                        print("ТУТ")
                        show_file_position()
                        print(f"i = {global_i_in_splited_str}")
                        break
                    else:
                        update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
                        text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                     str(global_j_in_file) + "." + str(
                                         global_i_in_file + len(splited_str[global_i_in_splited_str])))
                        showerror("Ошибка 3.10",
                                  "Ожидалось целое число: Полученно: " + splited_str[global_i_in_splited_str])
                        return False
                else:
                    w = 0
                    for n in range(len(global_metki_spisok)):
                        if splited_str[global_i_in_splited_str] == global_metki_spisok[n]:
                            w = 1
                    if w == 0:
                        global_metki_spisok.append(splited_str[global_i_in_splited_str])
        else:
            update_global_i_j_in_file(-len(splited_str[global_i_in_splited_str]))
            print("А ТУТ")
            show_file_position()
            print(f"i = {global_i_in_splited_str}")
            text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                         str(global_j_in_file) + "." + str(
                             global_i_in_file + len(splited_str[global_i_in_splited_str])))
            showerror("Ошибка 3.5", "Ожидалось: <<Переменные:>> или <<Метки:>>." + '\n' + "Получено: " + splited_str[
                global_i_in_splited_str])
            return False

        if (splited_str[global_i_in_splited_str + 1] != "Переменные:" and splited_str[
            global_i_in_splited_str + 1] != "Метки:") and (
        is_integer(splited_str[global_i_in_splited_str + 1] and indikator != 0)):
            break
    return True


def skip_metki(splited_str):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok

    print("-----Проверка меток-----")
    # Остановится на последней метке
    while splited_str[global_i_in_splited_str + 1] != ':':
        update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
        global_i_in_splited_str += 1
        ind = False
        i = 0
        while (not ind) and i < len(global_metki_spisok):
            print("for " + str(splited_str[global_i_in_splited_str]) + str(global_metki_spisok[i]))
            show_file_position()
            if str(splited_str[global_i_in_splited_str]) == str(global_metki_spisok[i]):
                ind = True
                print("------True------")
            i += 1
        if not ind:
            print("------FALSE-------")
            return False
    return True


def find_perem(splited_str):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok
    global global_perem_num

    print("-----Проверка переменных-----")
    for i in range(len(global_perem_spisok)):
        print(
            f"Проверка: Perem[{i}].get_name() = {str(global_perem_spisok[i].get_name())} Переменная в проге = {splited_str[global_i_in_splited_str]}")
        if str(global_perem_spisok[i].get_name()) == splited_str[global_i_in_splited_str]:
            global_perem_num = i
            return True  # Нашел переменную
    print("-----FALSE-----")
    return False  # Не нашел переменную


def find_end_operator(splited_str):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok

    if splited_str[global_i_in_splited_str] == "Конец" or splited_str[global_i_in_splited_str] == ',':
        print("Выражение пустое")
        return False
    print("-----Поиск конца или ,------")
    while global_i_in_splited_str + 1 < len(splited_str) and splited_str[global_i_in_splited_str + 1] != "Конец" and \
            splited_str[global_i_in_splited_str + 1] != ',':
        print(
            f"Поиск <<,>> или <<Конец>>: str = {splited_str[global_i_in_splited_str]} global_i_in_splited_str = {global_i_in_splited_str}")
        update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
        global_i_in_splited_str += 1
    print(
        f"Поиск закончен: global_i_in_splited_srt = {global_i_in_splited_str}, len(splited_str) = {len(splited_str)}, слово = {splited_str[global_i_in_splited_str]}")
    if global_i_in_splited_str + 1 < len(splited_str):
        if splited_str[global_i_in_splited_str + 1] == "Конец" or splited_str[global_i_in_splited_str + 1] == ",":
            update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
            print("-----True-----")
            return True
        else:
            print("-----False-----")
            return False
    else:
        print("-----False, конец не найдет-----")
        return False


def operator(splited_str):
    global global_j_in_file
    global global_i_in_file
    global global_i_in_splited_str
    global my_str
    global global_perem_spisok
    global global_metki_spisok
    global global_perem_num
    global global_tmp_str
    tmp_str = ""
    for i in range(global_i_in_splited_str, len(splited_str)):
        tmp_str += splited_str[i] + " "
    print(tmp_str)
    tmp_str = add_spaces_around_operators(tmp_str)
    print(tmp_str)

    new_splited_str = tmp_str.split()

    print(splited_str)

    i = global_i_in_splited_str
    n = 0
    while i < len(splited_str):
        splited_str[i] = new_splited_str[n]
        n += 1
        i += 1
    while n < len(new_splited_str):
        splited_str.append(new_splited_str[n])
        n += 1

    print(splited_str)
    global_tmp_str = splited_str
    show_file_position()
    # update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
    while True:
        if skip_metki(splited_str):  # Остановка на :
            print("------TRUE------")
            update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
            global_i_in_splited_str += 1
            update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))  # Остановка на Perem
            global_i_in_splited_str += 1
            if find_perem(splited_str):  # Переменная объявлена
                print("-----TRUE-----")
                update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                global_i_in_splited_str += 1
                if splited_str[global_i_in_splited_str] == '=':
                    update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                    global_i_in_splited_str += 1
                    if splited_str[global_i_in_splited_str] == "Конец" or splited_str[
                        global_i_in_splited_str] == ',' or len(splited_str) <= global_i_in_splited_str:
                        showerror("Ошибка 4.6", "Выражение не может быть пустым")
                        return False
                    print(f"{len(global_perem_spisok)} {global_perem_num}")
                    global_perem_spisok[global_perem_num].set_first(int(global_i_in_splited_str))  # Начало выражения
                    global_perem_spisok[global_perem_num].set_i_s(global_i_in_file)
                    global_perem_spisok[global_perem_num].set_j_s(global_j_in_file)
                    print("-----Начало выражения-----")
                    show_file_position()
                    if find_end_operator(splited_str):
                        print("-----Конец выражения-----")
                        show_file_position()
                        global_perem_spisok[global_perem_num].set_last(global_i_in_splited_str)  # Конец выражения
                        global_perem_spisok[global_perem_num].set_i_e(global_i_in_file)
                        global_perem_spisok[global_perem_num].set_j_e(global_j_in_file)
                        print(
                            f"first = {global_perem_spisok[global_perem_num].get_first()} last = {global_perem_spisok[global_perem_num].get_last()}")
                        if not global_perem_spisok[global_perem_num].get_first() == global_perem_spisok[
                            global_perem_num].get_last():
                            print("-----Не равны-----")
                            if global_perem_spisok[global_perem_num].set_example():

                                if splited_str[global_i_in_splited_str + 1] == "Конец":
                                    return True
                                elif splited_str[global_i_in_splited_str] == "," and global_i_in_splited_str == len(
                                        splited_str) - 1:
                                    text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                             str(global_j_in_file) + "." + str(
                                                 global_i_in_file + len(splited_str[global_i_in_splited_str])))
                                    showerror("Ошибка 4.5", "Ожидается <<Конец>>")
                                    return False
                                global_i_in_splited_str += 1
                                #update_global_i_j_in_file(len(splited_str[global_i_in_splited_str]))
                            else:
                                return False
                        else:

                            global_i_in_splited_str -= 1
                            text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                         str(global_j_in_file) + "." + str(
                                             global_i_in_file + len(splited_str[global_i_in_splited_str])))
                            showerror("Ошибка 4.4", "Выражение не может быть пустым")
                            return False
                    else:

                        text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                     str(global_j_in_file) + "." + str(
                                         global_i_in_file + len(splited_str[global_i_in_splited_str])))
                        showerror("Ошибка 4.3", "Ожидается <<,>> или <<Конец>> после выражения")
                        return False
                else:

                    text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                                 str(global_j_in_file) + "." + str(
                                     global_i_in_file + len(splited_str[global_i_in_splited_str])))
                    showerror("Ошибка 4.2", "Ожидается << = >> Полученно:" + splited_str[global_i_in_splited_str])
                    return False
            else:

                text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                             str(global_j_in_file) + "." + str(
                                 global_i_in_file + len(splited_str[global_i_in_splited_str])))
                showerror("Ошибка 4.1", "Переменная не объявлена: " + splited_str[global_i_in_splited_str])
                return False
        else:

            text.tag_add("highlightline", str(global_j_in_file) + "." + str(global_i_in_file),
                         str(global_j_in_file) + "." + str(
                             global_i_in_file + len(splited_str[global_i_in_splited_str])))
            showerror("Ошибка 4.0", "Метка не объявлена: " + splited_str[global_i_in_splited_str])
            return False


root = Tk()
root.title("Interpretator")
root.geometry('1000x500')

mainFrame = Frame()
mainFrame.place(relheight=0.75, relwidth=1.0)

text = Text(mainFrame)
text.place(relwidth=1.0, relheight=1.0)

scrollbar_y = Scrollbar(mainFrame, orient="vertical", command=text.yview)
scrollbar_y.pack(side="right", fill="y")
text["yscrollcommand"] = scrollbar_y.set

scrollbar_x = Scrollbar(mainFrame, orient="horizontal", command=text.xview)
scrollbar_x.pack(side="bottom", fill="x")
text["xscrollcommand"] = scrollbar_x.set

btn = Button(root, text='Подсчет', command=btn_clicked)
btn.place(relheight=0.10, relwidth=0.20, relx=0.40, rely=0.80)

text.tag_configure("highlightline", foreground="red", font="TkFixedFont", relief="raised")

text.insert(END, start_text)

root.mainloop()