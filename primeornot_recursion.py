def is_prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime(n,i+1)
n=int(input())
print(is_prime(n))
