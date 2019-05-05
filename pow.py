"""наивное возведение в степень"""

def pow(b, n):
    if n==0:
        return 1
    return b*pow(b, n-1)

a = int(input())
n = int(input())
print (pow(a,n))