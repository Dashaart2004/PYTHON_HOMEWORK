import pytest
from string_util import StringUtils


string_util = StringUtils()


@pytest.mark.parametrize('data,  result', 
[("dasha", "Dasha"), #проверка латиницы
("даша", "Даша"),    #проверка кириллицы
("a", "A"),          #проверка одной буквы
("Dasha12 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Dasha12 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), #проверка большого текста
("123", "123"),      #проверка цифр
("!@#$%", "!@#$%")  #проверка спецсимволов
])


def test_positive_caps(data, result):
    string_util = StringUtils()
    res = string_util.capitilize(data)
    assert res == result


@pytest.mark.parametrize(' data',
[(None),     # проверка пустой объект
([]),      #проверка пустого списка
(123),       #проверка числа
(" "),       #пробелы
("")         #пустая строка
])
def test_negative_caps(data):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.capitilize(data)


@pytest.mark.parametrize('data, result',
[("   Dasha", "Dasha"),                      #проверка латиницы
 ("   Даша   Артюнина", "Даша   Артюнина"),  #проверка кириллицы
 ("   ", ""),                                #проверка пробелов
 ("   !@#$%11   ", "!@#$%11   "),            #проверка спецсимволов
 ("Dashaa", "Dashaa"),                       #проверка при отсутсвии пробелов
 ])
def test_positive_whitespase(data, result):
    string_util = StringUtils()
    res = string_util.trim(data)
    assert res == result


@pytest.mark.parametrize('data',
[(None),  #none
 ([]),    #проверка списка
 ("")     #проверка пустого поля
])
def test_negative_whitesepase(data):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.trim(data)


@pytest.mark.parametrize('data, symbol, result',
[("a,b,c,d", ",", ["a", "b", "c", "d"]),                      #проверка букв
("1:2:3", ":", ["1", "2", "3"]),                              #проверка цифр
("apple,banana,cherry", ",", ["apple", "banana", "cherry"]),  #проверка слов
("hello world",  "",  ["hello", "world"])                     #проверка при отсутствии разделителя
])
def test_positive_separator(data, symbol, result):
    string_util = StringUtils()
    assert string_util.to_list(data, symbol) == result


@pytest.mark.parametrize('data, symbol',
[(None, None),
("a:b:c:d", "a"),  # Некорректный разделитель
("", ","),         # Пустая строка
([], [])           #пустой объект
])        
def test_negative_separator(data, symbol):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.to_list(data, symbol)


@pytest.mark.parametrize('string, symbol, expected',
[('hello world', 'w', True),     # Символ есть в строке
('abcde', 'z', False),           # Символа нет в строке
('12345', '2', True),            #цифра есть в строке
('!@#$%', '#', True),            #Спецсимвол есть в строке
("", "", True)                         #пустая строка
])           
def test_positive_contains(string, symbol, expected):
    string_util = StringUtils()
    result = string_util.contains(string, symbol)
    assert result == expected


@pytest.mark.parametrize('string, symbol',
[(None, None),   # проверка пустой объект
(123, 123)      #проверка числа
])
def test__contains_negative(string, symbol):
    with pytest.raises(Exception):
        string_util.contains(string, symbol)


@pytest.mark.parametrize('string, to_delete, result',
[("DashaR", "R", "Dasha"),               #проверка удаления одного символа
 ("DashaDFGДаша", "Даша", "DashaDFG"),   #проверка удаления нескольких символов
 ("Ghj vbn kkk", "kkk", "Ghj vbn "),     #проверка удаления слова
 ("Dasha", "g", "Dasha")                 #проверка удаления символа,которого нет
])
def test_positive_delete_symbol(string, to_delete, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, to_delete)
    assert res == result


@pytest.mark.parametrize('string, symbol',
[(None, None),   # проверка пустой объект
(123, 123),      #проверка числа
("", "")         #пустая строка
])
def test_negative_symbol_delete(string, symbol):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.delete_symbol(string, symbol)


@pytest.mark.parametrize('data, symbol, expected',
[("Dasha", "D", True),
 ("Lena", "H", False),
 ("", "", True)         #пустая строка
])
def test_positive_starts_with(data, symbol, expected):
    string_util = StringUtils()
    res = string_util.starts_with(data, symbol)
    assert res == expected

@pytest.mark.parametrize('string, symbol',
[(None, None),   # проверка пустой объект
(123, 123)      #проверка числа
])
def test_negative_starts_with(string, symbol):
    string_util = StringUtils()
    with pytest.raises(Exception):
         string_util.starts_with(string, symbol)


@pytest.mark.parametrize('data, symbol, expected',
[("a", "a", True),                  #проверка одного символа
 ("Awertyuiopasdfgn", "n", True),   #проверка большого количества символов
 ("Dasha is a student", "t", True), #проверка текста
 ("Fedya", "f", False),             #проверка на несодержание символа
 ("123456", "6", True),             #проверка цифр
 ("!@#$%", "%", True),               #проверка спецсимволов
("", "", True)                              #пустая строка
])
def test_positive_end_with(data, symbol, expected):
    string_util = StringUtils()
    res = string_util.end_with(data, symbol)
    assert res == expected


@pytest.mark.parametrize('string, symbol',
[(None, None),   # проверка пустой объект
(123, 123)      #проверка числа
])
def test_negative_end_with(string, symbol):
    srting_util = StringUtils()
    with pytest.raises(Exception):
        string_util.end_with(string, symbol)



@pytest.mark.parametrize('data, expected',
[("", True),                                   #проверка пустой строки
 ("  ", True),                                 #проверка пробелов
 ("fgh", False),                               #проверка букв
 ("fgh cvb fghj fghjk cvbnm tyui ", False)     #проверка текста
])
def test_positive_is_empty(data, expected):
    string_util = StringUtils()
    res = string_util.is_empty(data)
    assert res == expected


@pytest.mark.parametrize('string',
[(None),   # проверка пустой объект
(123),      #проверка числа
])
def test_negative_is_empty(string):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.is_empty(string)



@pytest.mark.parametrize('words, deliver, result',
[(["Da", "sha"], ":", "Da:sha"),                          #проверка двух слов
 (["123", "567"], "+", "123+567"),                        #проверка цифр
 (["acc", "ompo", "zit", "ion"], "-", "acc-ompo-zit-ion") #проверка нескольких слов
])
def test_positive_list_to_string(words, deliver, result):
    string_util = StringUtils()
    res = string_util.list_to_string(words, deliver)
    assert res == result


@pytest.mark.parametrize('string, symbol',
[(None, None),   # проверка пустой объект
(123, 123),      #проверка числа
([], [])          #Пустой список
])
def test_negative_list_to_string(string, symbol):
    string_util = StringUtils()
    with pytest.raises(Exception):
        string_util.list_to_string(string, symbol)
