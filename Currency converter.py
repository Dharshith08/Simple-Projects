# CONVERT INR,USD,EUR,MYR
print("THIS CONVERTER CAN CONVERT THE FOLLOWING CURRENCIES [INR,USD,EUR,MYR]")
a =float(input("Enter the amount:"))
b = input("From Currency[USE LOWER CASE]:")
c = input("To Currency[USE LOWER CASE]:")
print(a * 85.68) if b == 'inr' and c == 'usd' else print(a * 0.012) if b == 'usd' and c == 'inr' else print( a * 97) if b == 'inr' and c == 'eur' else print(a * 0.010) if b == 'eur' and c == 'inr' else print(a * 20.19) if b == 'inr' and c == 'myr' else print(a * 0.050) if b == 'myr' and c == 'inr' else print(a * 0.88) if b == 'usd' and c == 'eur' else print(a * 1.14) if b == 'eur' and c == 'usd' else print(a * 4.24) if b == 'usd' and c == 'myr' else print(a * 0.24) if b == 'myr' and c == 'usd' else print(a * 4.79) if b == 'eur' and c == 'myr' else print(a * 0.21) if b == 'myr' and c == 'eur' else None 
