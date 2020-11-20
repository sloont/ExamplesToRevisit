import math

def prime(n):               #finds the nth prime number
    

    if n == 0:
        return []
    
    primes = [2]
    num = 3

    while len(primes) < n:  #looking for nth prime so this will stop building the list after n primes are added to the list
        
        flag = True

        for i in primes:
            
            if num % i == 0:
                flag = False
                break
        
        if flag:       
            primes.append(num)
        
        num += 1
        

        
    return primes[-1]



print(prime(10001))         #test case



