import sys
from sys import argv
def check_if_prime(num):
    factors = []
    x = 0
    for i in range(1, int(num ** 3 / 4), 2):
        if num % i == 0:
            factors.append(i)
            for i in factors:
                x += 1
                if x > 3:
                    factors.pop(0)
                    p = factors[0]
                    q = factors[1]
                    n = (p - 1) * (q - 1)
                    return n


def rsa(e, n):
    x = check_if_prime(n)
    var = 1
    lol = ((x * var) + 1)
    while lol % e != 0:
        var += 1
        lol = ((x * var) + 1)
    raw_answer = lol
    answer = raw_answer // e
    return answer


def rsa_encryption(d, n, msg):
    cipher = pow(msg, d, n)
    return cipher


def main(e, n, msg = 256):
    d = rsa(e, n)
    enc = rsa_encryption(d, n, msg)
    return d

def main2(e, n, msg = 256):
    d = rsa(e, n)
    enc = rsa_encryption(d, n, msg)
    return enc

print(main(int(sys.argv[1]), int(sys.argv[2])),end = " ")
print(main2(int(sys.argv[1]), int(sys.argv[2])))





