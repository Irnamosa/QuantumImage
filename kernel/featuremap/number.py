import math

def coprimes(n):
    cps = []
    for i in range(n):
        if(np.gcd(i,n)==1):
            cps.append(i)
    return cps


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

# def order(x,N):
#     assert(N>x)
#     if(math.gcd(x,N)!=1):
#         return -1
#     for i in range(1,N+1):
#         if((x**i % N) == 1):
#             return i
    
def order(x,N):
    assert(N>x)
    if(math.gcd(x,N)!=1):
        return -1
    for i in range(1,N+1):
        a = x
        for j in range(1,i):
            a = x*a % N
        if(a==1):
            return i

primes = [i for i in range(0,10**3) if is_prime(i)]
