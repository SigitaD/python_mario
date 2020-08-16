from cs50 import get_int

# apibreziama pagindine funkcija, kuri yra piesti piramide


def main():
    # paimamas piramides ausktis is f-cijos get_height
    n = get_height()
    for i in range(n):
        print(" " * (n-i-1), end="")
        print("#" * (i+1), end="")
        print("  ", end="")
        print("#" * (i+1))

# aprasoma f-cija, kuria is userio gaunamas piramides aukstis, kuris yra skaicius, ne daugiau 8 ir ne maziau 1


def get_height():
    while True:
        k = get_int("What is the height of the pyramid?\n")
        if k < 9 and k > 0:
            break
    return k


main()