class Client:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        outputlist.append(self.balance)
        return self.balance


class Bank:
    def __init__(self):
        self.clients = {}

    def get_client(self, name):
        return self.clients.get(name)

    def deposit(self, name, amount):
        self.clients[name] = Client(name)
        self.clients[name].deposit(amount)

    def withdraw(self, name, amount):
        client = self.get_client(name)
        if client:
            client.withdraw(amount)
        else:
            outputlist.append("ERROR")

    def balance(self, name):
        client = self.get_client(name)
        if client:
            client.get_balance()
        else:
            outputlist.append("ERROR")

    def transfer(self, from_name, to_name, amount):
        from_client = self.get_client(from_name)
        to_client = self.get_client(to_name)
        if from_client and to_client:
            from_client.withdraw(amount)
            to_client.deposit(amount)
        else:
            outputlist.append("ERROR")

    def income(self, percent):
        for client in self.clients.values():
            if client.get_balance() > 0:
                amount = client.get_balance() * percent // 100
                client.deposit(amount)
    def bankoutput(self):
        for item in outputlist:
            print(item)

outputlist = []
bank = Bank()
def inputdata():
    bal = 'BALANCE'
    dep = 'DEPOSIT'
    wit = 'WITHDRAW'
    inc = 'INCOME'
    trans = 'TRANSFER'
    running = True
    while running:
        commandlist = []
        bankrequest = input().split()
        
        for _ in bankrequest:
            commandlist.append(_)
        
        if commandlist[0] == bal:
            bank.balance(commandlist[1])
       
        elif commandlist[0] == dep:
            commandlist[2] = int(commandlist[2])
            bank.deposit(commandlist[1],commandlist[2])
       
        elif commandlist[0] == wit:
            commandlist[2] = int(commandlist[2])
            bank.withdraw(commandlist[1],commandlist[2])
        
        elif commandlist[0] == inc:
            commandlist[1] = int(commandlist[1])
            bank.income(commandlist[1])
        
        elif commandlist[0] == trans:
            commandlist[3] = int(commandlist[3])
            bank.transfer(commandlist[1],commandlist[2],commandlist[3])
        else:
            bank.bankoutput()
            break

inputdata()

    








