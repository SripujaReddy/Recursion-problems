def fun(n):    
    if n==0:
        return
    if n%2!=0:
        print(n, end=' ')
    fun(n-1)
    if n!=1 and n%2!=0:
        print(n,end=' ')
n=5
fun(n)