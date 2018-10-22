# Uses python3
import sys

def gcd_naive(a, b):
    while b:
        a, b = b, a%b
    return a

if __name__ == "__main__":
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(gcd_naive(a, b))