"""Алгоритм евклида через рекурсию"""
a = 30
b = 18
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
print (gcd(a,b))