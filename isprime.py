

def isPrime(num):
    for i in range(2, n):
        if n%i == 0:
            return "false"
    else:
        return "true"
    
if __name__ == "__main__":
    n= int(input())
    print(isPrime(n))
