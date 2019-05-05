"""быстрое возведение в степень"""


def pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(a, n / 2) ** 2
    else:
        return a * pow(a, n - 1)


a = int(input())
n = int(input())
print(pow(a, n))