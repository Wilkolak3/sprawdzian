def licz():
    plik = open("napisy.txt", "r")
    str = plik.readline()

    parzyste = 0

    for str in str:
        str = str.strip()
        dlugosc = len(str)

        if dlugosc % 2 == 0:
            parzyste += 1
    print(parzyste)







