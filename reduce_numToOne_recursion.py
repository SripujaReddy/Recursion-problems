def reduceToOne(n,steps=0):
    if n==1:
        return steps
    if n%2==0:
        return reduceToOne(n//2,steps+1)
    else:
        return min(reduceToOne(n+1,steps+1),reduceToOne(n-1,steps+1))
n=int(input())
print(reduceToOne(n))
