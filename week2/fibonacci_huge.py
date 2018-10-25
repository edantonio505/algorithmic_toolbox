# Uses python3
import sys


def calc_fib(n):
    if (n <= 1):
        return n
    f = [x for x in range(n+1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1]+f[i-2]                
    return f[-1]



def get_fibonacci_huge(n, m):
    if (n <= 1):
        return n
    fibmod = []
    searching = True    
    stop = 3 
    if m > 3:
        stop = 5
    sequence = "".join([str(calc_fib(i)) for i in range(m)])[:stop]    
    i = len(sequence)
    while searching:
        fibmod.append(str(calc_fib(i)%m))
        if sequence in "".join(fibmod):
            searching = False
        i += 1
    return calc_fib(n%len(fibmod))%m
  










if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
