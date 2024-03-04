num = 30

if num % 2 == 0:
    print("Number is divisible by 2.")
else: 
    print("Number is not divisible by 2.")    
    
print('End'.center(30,'-'))

if num % 2 == 0:
     print("Number is divisible by 2.")
elif num % 3 == 0:
    print("Number is divisible by 3.")
else:
    print("Number is divisible by neither 2 or 3.")

print('End #2'.center(30,'~'))

if num % 2 == 0 and num % 3 == 0: #or, not
    print("Number is divisible by 6.")
else:
    print("Number is not divisible by 6.")