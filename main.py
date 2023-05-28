countries = {
    "Россия": "Москва",
    "Китай": "Пекин",
    "США": "Вашингтон",
    "Канада": "Оттава",
    "Япония": "Токио",
    "Южная Корея": "Сеул",
    "Великобритания": "Лондон",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Норвегия": "Осло",
    "ОАЭ": "Дубай",
    "Испания": "Мадрид",
    "Италия": "Рим"
}

erudit = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ",
}

languages = {
    "Данил": ["Русский язык", "Английский язык", "Китайский язык"],
    "Андрей": ["Русский язык", "Английский язык", "Итальянский язык"],
    "Марат": ["Русский язык", "Японский язык"],
    "Алексей": ["Английский язык","Арабский язык"],
    "Петр": ["Китайский язык", "Корейский язык", "Французский язык"]
}



def one_a():
    for key, value in countries.items():
        print(f'{key} : {value}')
one_a()
def one_b(country):
    if country in countries.keys():
        print(countries.get(country))
    else:
        print("Такой страны не существует")

# one_b(input('country: '))
def one_c():
    sorted_list = sorted(countries.items())
    for i in sorted_list:
        print(i)



def two(text):
    print(sum(
        [k for i in text for k, v in erudit.items() if i in v]
    ))



def all():
    lang_set = set()
    for i in languages.values():
        if type(i) is not list:
            lang_set.add(i)
        else:
            for j in i:
                lang_set.add(j)

    return lang_set


def langs():
    print("Количество языков, которые знают студенты: ", len(all()))


def sorte():

    print(sorted(all()))


def Chinese():
    print("Студенты, которые знают Китайский язык: ")
    for i in languages.values():
        if "Китайский язык" in i:
            print(" ", get_key(languages, i))


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

# 1 zadanie
# one_a()
# one_b(input('Введите страну: '))
# one_c()

# 2 zadanie
# two(input("Введите слово: ").upper())

# 3 zadanie
# langs()
# sorte()
# Chinese()