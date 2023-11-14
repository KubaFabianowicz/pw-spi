from math import sqrt 
# print(sqrt(10))

import random 
# #generowanie losowej liczby calkowiteje z akresu 1-100
# print(random.randint(1,100))

# #wybor losowego elementu z listy 
# fruits = ["apple", "banana", "ziemniak"]
# print(random.choice(fruits))

# #mieszanie listy 
# numbers = [1,2,3,4,5]
# random.shuffle(numbers)
# print(numbers)

# #zwrocenie biezacego czasu w sekundach 
import time 
# print(time.time())

# #zwrocenie biezacej daty i godizny
import datetime
# now = datetime.datetime.now()
# print(now)

# #napisz kod ktory wypisze liste wszystkich plikow w obencym katalogu 
import os 
# for file in os.listdir():
#     print(file)
# #os.mknod("nowy_plik.txt")

# file_path = "repo.py"
# if os.path.exists(file_path):
#         print('file already exists')

# print(os.path.isfile(file_path))

# #print(os.listdir('test'))

# os.rename(file_path, file_path+"nowy_plik.txt")

# os.mkdir("nowy_katalog")

# with open("nowy_plik.txt", "w") as f:
#       f.write("To jest nowy plik")

#napisz program ktory sprawdza czy format daty jest prawdilowy

# todays_date = datetime.date.today()
# print(todays_date)

# date = "2023-10-12"
# print(datetime.date.fromtimestamp(10000000).year)
# a = datetime.time(11,34,56)
# a = datetime.time(2022, 12, 28, 23, 55, 59, 34290)
# s1 = now.strftime("%m/%d/&Y", %H:%M:%S")

#Pobierz aktualna date i godzine
from datetime import datetime 
now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%Y"))

#aktualny miesiac
print(now.strftime("%b"))

#aktualny dzien nazwa
print(now.strftime("%A"))

#konwersja napis na obiekt
date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
print(date_object)

date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
print(date_object)

from datetime import timedelta

#dodaj 5 dni 
date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
print(date_object)
new_date = date_object + timedelta(days=5)
print(new_date)

print(now+timedelta(weeks=2))

#wyswietl roznice w dniahc od 1 styczna 2023
past_date = datetime(2023,1,1)
day = now - past_date
print(day.days)

import calendar   
#sprawdz czy rok 2024 jest przestepczy
new_year = calendar.isleap(2024)
print(new_year)

#wyswietl numer bieacego tygodnia roku 
print(now.strftime("%u"))

rfc_date = datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a, %d, %b %Y %H:%M:%S +0000")
print(rfc_date)

#znajdz dizen tygodnia dla 4 lipca 
date2 = datetime(now.year, 7, 4)
print(date2.strftime("%A"))