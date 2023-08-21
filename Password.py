# rework with tkinter now just probe 
import random

characters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*_"

pass_lenght = int(input("Enter lenght of password:"))
count_pass = int(input('Write number of needed passwords:'))

for i in range (0, count_pass):
    password = " "
    for j in range (0, pass_lenght):
        pass_char = random.choice(characters)
        password = password + pass_char
    print("Your password is:", password)    
