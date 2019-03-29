#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
    def addCLient(self, client):
        if isinstance(client,Client):
            self.clients.append(client)
    def create_bank_account(self, client_id):
        for client in self.clients:
            if client.id == client_id:
                client.bank_account = BankAccount

    def input_money(self, money, client_id):
          for client in self.clients:
                if client.id == client_id:
                    pass
                    #if client.is_bank_account():   
                    #client.bank_account.input_money(money)
                    #print(client.id)
    def __str__(self):
        return "Bank details:\n\tBank name:{}\n\tNumber of clients:{} ".format(self.name, len(self.clients))

    def removeClient(self, client):
        pass
class BankAccount:
    def __init__(self, money):
        self.money = 0
        self.limit = 0
        
    def input_money(self, money):
        self.money += money

    def withdraw_money(self, withdraw):
        if self.money >= withdraw:
            self.money -= withdraw
            return withdraw

    def __str__(self):
        return "Money:{}".format(self.money)


class Client:
    def __init__(self,ID, name, surname, address, phone_number):
        self.id = ID
        self.name = name
        self.surname = surname
        self.address = address
        self.phone_number = phone_number
        self.bank_account = None

    def is_bank_account(self):
        return isinstance(self.bank_account, BankAccount)

if __name__ == "__main__":
    bank = Bank('ING')
 
    client_1 = Client(1,'Caro', 'McMizera', 'Krakow', '570320')
    bank.addCLient(client_1)
    bank.create_bank_account(1)
    bank.input_money(100, 1)
    print(bank)