from functools import reduce

def parity_check(bits):
    return reduce(
        lambda x,y: x^y,
        [i for (i,b) in enumerate(bits) if int(b)]
    )
if __name__ == "__main__":
    print(parity_check("11101111110"))