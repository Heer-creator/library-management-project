import json 
import string
import random
from pathlib import Path

class Library:
    database1='books.json'
    database2='members.json'

    @classmethod
    def books_data(cls):
        if Path(cls.database1).exists():
            with open(cls.database1,'r') as fs:
                data=json.load(fs)
                return data
        return[]
    
    @classmethod
    def members_data(cls):
        if Path(cls.database2).exists():
            with open(cls.database2) as fs:
                data=json.load(fs)
                return data
        return []
    
    @classmethod
    def generate_ide(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        ide=alpha+num
        return "".join(ide)
    
    @classmethod
    def save_member_data(cls,data):
        with open(cls.database2,'w') as fs:
            json.dump(data,fs,indent=4)


    @classmethod
    def Add_member(cls,name,email,age,password):
        data2=cls.members_data()
        if age<18:
            return None,"Age must be 18 or above"
        else:
            ide=cls.generate_ide()
            user={
                "name":name,
                "email":email,
                "age":age,
                "password":password,
                "ide":ide,
            }
        data2.append(user)
        cls.save_member_data(user)
        return user,"Account created successfully"
        



