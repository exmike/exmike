def stat(string):
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = 1
        elif letter in dictionary:
            dictionary[letter] += 1
        else:
            print('Ошибка\n')
    k = 0
    s = ''
    for key in dictionary.keys():
        s += str(key) + ' : ' + str(dictionary[key]) + ',  '
        if k == 5:
            k = 0
            print(s, '\n')
            s = ''
        else:
            k += 1
    print('Число различных символов в строке: ', len(dictionary))

def podstroka(string):
    sub = input('Регистрозависимая подстрока: ')
    position = string.find(sub)
    if position == -1:
        print('Подстрока в строке отсутствует')
    else:
        print('Подстрока в строке присутствует, начиная с позиции ', position)

def alfavit(string):
    words = string.split(' ')
    for i in range(len(words) - 1):
        flag = True
        for j in range(len(words) - i - 1):
            if words[j] > words[j + 1]:
                buff = words[j]
                words[j] = words[j + 1]
                words[j + 1] = buff
                flag = False
        if flag:
            break
    print('Слова в алфавитном порядке:\n')
    for word in words:
        print(word)

def main():
    stroka = input('Введите строку: ')
    print(stroka, '\n')
    stat(stroka)
    stroka = stroka.strip()
    podstroka(stroka)
    alfavit(stroka)

if __name__ == '__main__':
    main()
