# Python program to check if the input number is odd or even with bitwise and(&) operator.
num = int(input("Enter a number: "))
if(num&1)== 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))