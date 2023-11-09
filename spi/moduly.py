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

todays_date = datetime.date.today()
print(todays_date)

date = "2023-10-12"
print(datetime.date.fromtimestamp(10000000).year)
a = datetime.time(11,34,56)
a = datetime.time(2022, 12, 28, 23, 55, 59, 34290)
s1 = now.strftime("%m/%d/&Y", %H:%M:%S")