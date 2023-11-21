def suma(liczba):

    sum = 0

    while (liczba!=0):

        sum = sum + (liczba % 10)
        liczba = liczba//10 

    return sum

liczba = 1234
 

print(suma(liczba))  