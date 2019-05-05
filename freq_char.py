"""частота встречаемости символов в строке"""

def count_char(string, char):
    count = 0
    for k in string:
        if k is char:
            count += 1
    return count
a = 'ffasdadas  tse'
print(count_char(a, 'f'))