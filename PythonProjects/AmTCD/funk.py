spravka_text = "Приложение с графическим интерфейсом «Блокнот AmTCD» (файл приложения: AmTCD)" \
               "Позволять: создавать / открывать / сохранять зашифрованный тестовый " \
               "файл, должно быть предусмотрено " \
               "ввод и сохранение личного ключа, вывод не модальной формы «Справка» , " \
               "вывод модальной формы «О программе»."

def codeText(S, Key):
    SS = ""
    for i in range(len(S)):
        SS += chr(ord(S[i]) ^ Key)
    return SS

def _get_KeyU_():
    F = open("AmTCD.ini", 'r')
    F.readline()
    F.readline(10)
    SS = F.readline()
    F.close()
    return SS

def _save_keyU_(KeyU):
    F = open("AmTCD.ini", 'w')
    F.write("[main]" + '\n'
            "keyuser = " + KeyU)
    F.close()




# default settings
def _get_family_():
    F = open("AmTCD.ini", 'r')
    for i in range(3):
        F.readline()
    F.readline(8)
    ansv = F.readline()
    F.close()
    print(ansv)

