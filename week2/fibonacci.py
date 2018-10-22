# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    f = [x for x in range(n+1)]
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1]+f[i-2]        
        
    return f[-1]

    
n = int(input())
print(calc_fib(n))