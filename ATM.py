#simple program to demonstrate ATM mechanism

Total_amount = int(25000)

print ("Welcome to SBI ATM, Please instert your card")
print ("Wait while we are processing your card")
PIN = input("Please enter your 4 digit PIN: ")
withdran = int( input("Please enter amount you want to withdraw: "))
AvlBal = (Total_amount - withdran)

print ("Collect your cash {}, your available amount is {}".format(withdran, AvlBal))