import math
c = (input("Enter The operation: "))
if c in  ['+' , '-' , '*' , '/' , '**']:
    a = int(input("Enter The first number: "))
    b = int(input( "Enter The second number: "))
    print((a // b)) if c == '/' and b != 0 else print("The given value is \"ILLEGAL\"") if b == 0 else None
    print(a + b) if c == '+' else  print(a - b) if c == '-' else print(a * b) if c == '*'  else print(a ** b) if c == '**' else None
elif c in ['round up' , 'round down']:
    a = float(input("Enter a float Num:"))
    print(math.ceil(a)) if c == 'round up' else print(math.floor(a)) if c == 'round down' else print(" \"INVALID INPUT\"check your spelling or select round up or round down ")