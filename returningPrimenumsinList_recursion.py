def is_prime(n,i=2):
    if n<2:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
def primeList(li,i=0):
    if i==len(li):
        return 0
    if is_prime(li[i]):
        print(li[i],end=' ')
    primeList(li,i+1)
li=list(map(int,input().split()))
primeList(li)