import json 
import string
import random
from pathlib import Path

class Library:
    database1='books.json'
    database2='members.json'

    
    @classmethod
    def members_data(cls):
        if Path(cls.database2).exists():
            with open(cls.database2) as fs:
                data=json.load(fs)
                return data
        return []
    
    @classmethod
    def books_data(cls):
        if Path(cls.database1).exists():
            with open(cls.database1,'r') as fs:
                data=json.load(fs)
                return data
        return[]
    
    @classmethod
    def generate_member_ide(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        ide=alpha+num
        return "".join(ide)
    @classmethod
    def generate_book_ide(cls):
        alpha=random.choices(string.ascii_letters,k=2)
        num=random.choices(string.digits,k=2)
        ide=alpha+num
        return "".join(ide)
    
    @classmethod
    def save_member_data(cls,data):
        with open(cls.database2,'w') as fs:
            json.dump(data,fs,indent=4)

    @classmethod
    def save_book_data(cls,data):
        with open(cls.database1,'w') as fs:
            json.dump(data,fs,indent=4)


    @classmethod
    def Add_member(cls,name,email,age,password):
        data2=cls.members_data()
        if age<10:
            return None,"Age must be 10 or above"
        else:
            ide=cls.generate_member_ide()
            user={
                "name":name,
                "email":email,
                "age":age,
                "password":password,
                "ide":ide,
            }
        data2.append(user)
        cls.save_member_data(data2)
        return user,"Account created successfully"
    
    @classmethod
    def delete_account(cls,ide,password):
        data2=cls.members_data()
        for i,user in enumerate(data2):
            if user['ide']==ide and user['password']==password:
                data2.pop(i)
                cls.save_member_data(data2)
                return "Account deleted successfully"
        return "User not found or password is incorrect"
    
    @classmethod
    def update_password(cls,ide,password,new_password=None):
        data2=cls.members_data()
        for user in data2:
            if user["ide"]==ide and user["password"]==password:
                user["password"]=new_password
                cls.save_member_data(data2)
                return "Password updated successfully"
        return "User id not found or incorrect password"


    @classmethod
    def Add_book(cls,name,author,genre):
        data1=cls.books_data()
        ide=cls.generate_book_ide()
        book={
            "name":name,
            "author":author,
            "genre":genre, 
            "ide":ide,          
        }
        data1.append(book)
        cls.save_book_data(data1)
        return book,"Book added successfully."
    
    @classmethod
    def delete_book(cls,name,ide):
        data1=cls.books_data()
        for i,book in enumerate(data1):
            if book['name']==name and book['ide']==ide:
                data1.pop(i)
                cls.save_book_data(data1)
                return "Book deleted successfully"
        return book['ide'],ide

                

        



