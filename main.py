print('+ = Addition')
print('- = Subtraction')
print('* = Multiplication')
print('/ = Division')
print('% = Remainder')
print('** = Exponents')

x = str(input('Choose ur calculation sign (-, +, /, *, %, **): '))

if x == '-':
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))
  print(a-b)
  
elif x == '+':
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: ')) 
  print(a+b)

elif x == '*':
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))
  print(a*b)

elif x == '/':
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))
  print(a/b)

elif x == '%': 
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))
  print(a%b)

elif x == '**':
  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))
  print(a**b)

else:
  print('Invalid mathematic operator')