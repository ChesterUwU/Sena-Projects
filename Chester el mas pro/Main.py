from Account import *

ChesterAccount = Account ("Chester", "7575", 8000 , "Ahorros")
#print (ChesterAccount.OwnerName)
#print (ChesterAccount.AccountID)
#print (ChesterAccount.Balance)
#print (ChesterAccount.AccountType)
#ChesterAccount.Transferir(1200)
#print (ChesterAccount.Balance)

print ("Transferencia")
print ("Bienvenido", ChesterAccount.OwnerName)
print ("Numero de Cuenta:", ChesterAccount.AccountID)
print ("Balance:", ChesterAccount.Balance)
print ("Ingrese monto a transferir")
print ("Monto: 1.200")
ChesterAccount.Transferir(1200)
print ("Ahora tu balance es de:")

ChesterAccount.consultar("Chester")
