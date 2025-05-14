def reverseOfNum(n,rev=0):
    if n==0:
        return rev
    else:
        d=n%10
        rev=(rev*10)+d
        return reverseOfNum(n//10,rev)
n=int(input())
print(reverseOfNum(n))
        
