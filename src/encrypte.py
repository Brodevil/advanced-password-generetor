import json


def encrypt(string, dictionary):
    return '.'.join([dictionary.get(each, each) for each in string])


def decrypt(string, dictionary):
    dictionary = {dictionary[key]: key for key in dictionary}
    decoded = [dictionary.get(each, each) for each in string.split('.')]
    return ''.join(decoded)
