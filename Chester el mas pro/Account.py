class Account:
    #Atributos
    OwnerName = None
    AccountID = None
    Balance = None
    AccountType = None
    
    #Constructor
    def __init__(self, OwnerName, AccountID, Balance, AccountType):
        self.OwnerName = OwnerName
        self.AccountID = AccountID
        self.Balance = Balance
        self.AccountType = AccountType
        
    #Metodos
    def Transferir (self, Monto):
        self.Balance = self.Balance - Monto
        
    def consultar (self, OwnerName):
        if OwnerName == self.OwnerName:
            print (self.Balance)
                
        else:
            print ("Wrong Account")