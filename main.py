import random
import string
import os
from encrypte import encrypt, decrypt, encrypt_dict
import pyperclip


def getdate():
    """Functions to get the present date & time """

    import datetime
    return datetime.datetime.now()


def randome_str(length):
    """ Functions to generate randome passwords """

    password = ""
    charactors = f"{string.ascii_letters}{string.punctuation}{string.digits}"
    for i in range(length):
        password  += random.choice(charactors)
    return password


def write_file(data,  filename):
    """Here we will append in file in the encrypted form and also make the file hidden for the user"""

    with open(filename, "at") as password_stored_file:
        password_stored_file.write(data)
    os.system(f"attrib +h {filename}")


def read_file_by_decrypt(filename):
    """Reading the encyted password containing file and return the decryted data of that file """

    with open(filename, "rt") as password_stored_file:
        return decrypt(password_stored_file.read(), encrypt_dict)


def encrypt_data(username, password, pourpose):
    """This suppose to encryte the data using the functions in encrypt file and return it"""
    return encrypt(f"{getdate()} \tUsername = {username:<15} Password = {password}\nPourpose = {pourpose}\n\n\n", encrypt_dict)


def copy_to_clipboard(str):
    """Functions to copy the password in the clipboard so make easy for the user"""

    pyperclip.copy(str)
    spam = pyperclip.paste()


if __name__ == "__main__":
    while True:
        print("\nWelcome to the advanced password generater python program that just do more than generating random paswwords \n\n")
        try:
            work = int(input("Enter 1 to generate the password or Enter 2 to See the your password file history or Enter 3 to get security info about this python Program : \t"))
        except ValueError:
            print("Enter a leagule input that will be a number :\n")
            continue

        if work == 1:
            user_name = input("Please Enter the username of your account: \t")
            info_pourpose = input("Please enter the purpose for which thing generating the password :\t")
            try:
                length = int(input("Just Enter a password length : \t"))
            except ValueError:
                print("Enter a leagule Input i.e. a number \n")
                continue

            password = randome_str(length)
            print(f"{getdate()} \tUsername = {user_name:<15} Password = {password}\nPourpose = {info_pourpose}\n\n\n")
            print(f"Sir Your password is :\t {password:>20} \nIts also copied to your clipboard You can just go and paste and also saved in the file, So as per your requirements you and read the encryted data of the file.\n")
            copy_to_clipboard(password)            
            password = encrypt_data(user_name, password, info_pourpose)
            write_file(password, "passwords.txt")
        
        elif work == 2:
            try:
                print(read_file_by_decrypt("passwords.txt"))
            except Exception:
                print("Sorry! You had not generated passwords yet.\n")
            
        elif work == 3:
            print("\nWe Matter your privacy and your security of your files, Your passwords containing files are encrypted and also a hidden file. \nIf you wish you can open those file but you will not able to read it as it will be fully encrypted\n"
            "And the passwords are getting auto copied to your clipboard and its totally a difficult password which a hacker will not able to crack easily\nYou are totally safe and don't take tension about the passwords just for suppording us You can follow my GitHub Profile :https://github.com/Brodevil:\n"
            "for more info you can read the README.md file in our repo :https://github.com/Brodevil/advanced-password-generetor:\n\n\t\t\t\t\tThank you for using our Program\n")
        
