#!/bin/python3

import os
import json

def log(stuff): print(stuff)

class person:
    def __init__(self, name, age):
            self.name = name
            self.age = age

def main():
    name = input("What is you NAME: ")
    age = input("What is your AGE: ")
    p = person(name, age)
    pjson = json.dumps(p.__dict__)
    with open(name + '.json', 'w') as fp:
        fp.write(pjson)

main()