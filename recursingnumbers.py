def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    if m!=n-1:
        print(m+1,end=" ")
n=int(input())
fun(n)
    