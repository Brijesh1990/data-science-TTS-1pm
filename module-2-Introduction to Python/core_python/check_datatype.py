# type casting float, int, str
totalamm=50000
account=int(input('Enter your bank account :'))
pin=int(input('Enter your pincode  :'))
withdrawl=int(input('Enter your withdrawl ammount :'))
res=totalamm-withdrawl
print('you have an remaining ammount of :',res,'in your account')
# print(type(res))
# type is an inbuild method
print(type(res))