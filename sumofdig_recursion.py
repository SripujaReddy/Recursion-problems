def sumOfDigits(n):
    if n==0 or n==1:
        return n
    return (n % 10) + sumOfDigits(n // 10)
n=int(input())
print(sumOfDigits(n))