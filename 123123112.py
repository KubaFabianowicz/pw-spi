# def powitanie(imie):
#     print(f"witaj, {imie}, w świecie pythona!")

# powitanie("anna")

# def max_min(x, y, z):
#     return max(x,y,z), min(x,y,z)

# print(max_min(32,123,523))

# def dlugosc_ciagu(ciag):
#         return len(ciag)
# print("dlugosc ciagu")
# print(dlugosc_ciagu("pyton"))

# def silnia(n):
#      if n==0:
#           return 1
#      else:
#           return n*silnia(n-1)
# print("sinlnia")
# print(silnia(5))

# #adnotacja typów

# def suma(a: int, b: int) -> int:
#      return a+b
# print(suma(10,20))

# import requests

# response = requests.get('https://www.google.com')
# print(response.status_code)
# #print(response.text)

# #Walidacja adresu e-mail
# #czy istnieje @
# #walidacja pustych znakow
# #user ma 6-30 znakow
# def validate_email(email):
#      if email.count('@') !=1:
#           raise ValueError("to nie jest adres mailowy!")
     
#      param = email.split('@')
#      print(param)
# try:
#     validate_email("jakub.fabianowciz@pw.edu.pl")
# except ValueError as e:
#      print(f"komunikat bledu: {e}") 
# #any
# #len
# #isdigit
# #isupper
# #validate_password
# password = "jdjdjd21"
# def validate_password(password):
#      mam_cyfre = any(char.isdigit() for char in password)
#      mam_wielka = any(char.isupper() for char in password)
#      dlugosc = len(password)>=8
#      return mam_cyfre and mam_wielka and dlugosc

# haslo = input("haselko")
# if validate_password(haslo):
#      print("silne haslo bracie")
# else:
#      print("lipne haslo")


# def validate_username(username):
#     return username.isalnum() and 3<= len(username) <= 16 

# username = input("username")
# if validate_username(username):
#      print("dobry")
# else:
#      print("no niezbyt")

# def validate_ip(ip):
#      parts = ip.split('.')
#      if len(parts) !=4:
#           return False
#      for part in parts:
#           if not parts.isdigit() or not 0 <= int(part) <= 255:
#                return False
#      return True
# #Tes
# print(validate_ip('192.168.1.1'))
# print(validate_ip('192.168.256.256'))
# print(validate_ip('192.168.1'))

# #nip_walidacja
# nip = '2131233123'
# weights = [6,5,6,7,8,9,5,4,5,6]
# #sprawdzamy czy mamy 10 
# #spradzamy czy wszyskite sa cyframi 
# if len(nip) != 10:
#      False

# if nip.isdigit():
#      False

# for i in range(9):
#      suma += int(nip[i] * weights[i])

# if suma%11 != nip
