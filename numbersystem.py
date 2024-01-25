#write  python script to print any number and its binary equivalent
x=25
print(bin(x))
x=16
print(bin(x))
print(bin(9))
print(bin(5))
print(bin(6))
#using while methhod
print("Welcome to Calculate Binary Equivalent")
x=int(input("Please Enter you Number:"))
tem=x
rem=0
y=""
while tem>0:
    rem=tem%2
    y=str(rem)+y
    tem=tem//2
print("The Binary Representation of {} is {}".format(x,y))
#Binary number to decimal format
z=0b1100101
print("The binary represtation to deciaml is {}".format(z))
#add pf two numbers 25 (octal) and 39(hexadeciaml)
x=0x39
y=0o31
z=bin(x+y)
print("Adding of two numbers octal and hex in binary is {}".format(z))
#problem 4
x=0x3f
z=oct(x)
print("Conversion of hex to oct is {}".format(z))
#problem 4
x=0o125
z=bin(x)
print("Conversion of oct to binary is {}".format(z))