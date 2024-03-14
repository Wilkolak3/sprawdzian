def licz():
    plik = open("napisy.txt", "r")
    str = plik.readline()

    parzyste = 0

    for string in str:
        string = string.strip()
        dlugosc = len(string)

        if dlugosc % 2 == 0:
            parzyste += 1
    print(parzyste)







