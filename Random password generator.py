# from random import randint

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "1234567890"
# symbols = "{ } [ ] ( ) ! @ # $ % ^ & * _ - + = / ? < > . , ` ~ "
# combine = lower + upper + number + symbols
# length = 20
# password = random(combine, length)
# # password = random
# print(password)




import random
import time
import shutil
from playsound import playsound


password = ""

def getdate():
    import datetime
    return datetime.datetime.now()

present_time = getdate()

def random_password_generator(length, number):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}[]()!@#$%^&*_-+=/?<>.,`~"
    global password
    for p in range(number):
        pass
        for c in range(length):
            password += random.choice(chars)
    print("\nYour password is :\t", password)

def store_password_in_file(user__name, info__pourpose, pass_word):
    password_stored_file = open("E:\ADMIN\personal file\Abhinav\Passwords.txt", "a")
    file_write = str(present_time) + "\t:" + user__name + "\t:" + info__pourpose + "\n& the password was :\t" + pass_word + "\n\n"
    password_stored_file.write(file_write)
    password_stored_file.close()

def read_password_file():
    read_file = open("E:\ADMIN\personal file\Abhinav\Passwords.txt", "rt")
    print(read_file.read())
    read_file.close()
    
def copy_files_for_reference():
    original_file = r'E:\ADMIN\personal file\Abhinav\Passwords.txt'
    target_copied_file = r'E:\ADMIN\personal file\aux\Password_copy.txt'

    shutil.copyfile(original_file, target_copied_file)
print("\n\t\t\tThis is a program to generate the random passwords and to stored those password\n\n")           


read_or_write = int(input("Enter 1 to generate the password or Enter 2 to See the your password file history:\t"))
if read_or_write == 1:
    user_name = input("Please Enter the username of your account: \t")
    info_pourpose = input("Please enter the purpose for which thing generating the password :\t")

    try:
        length = int(input("Just Enter a password length or just enter to use default length: \t"))
    except Exception as error:
        print("You choiced the default length ")
        length = 16
    random_password_generator(length, 1)
    store_password_in_file(user_name, info_pourpose, password)
    copy_files_for_reference()
else:
    read_password_file()
    
playsound('E:\\ADMIN\\VS Code\\Scam1992Ringtone1144418968.mp3')

print("\n\n\t\t\t\t\t\tThank you for choosing us ", "\U0001F607")

