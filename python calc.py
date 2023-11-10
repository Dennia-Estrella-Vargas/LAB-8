import math

def addition(a,b):
   return a+b

def substraction(a,b):
   return a-b

def multiplication(a,b):
   return a*b

def division(a,b):
   if b==0:
      print("You can't divide by zero.")
   else:
      return a/b

while True:
  operator = input ("Enter the operation: +, -, *, /, ^, sin, cos, sqrt or 'q' to exit")
  if operator == "q":
      break
  elif operator == "sin":
      x = float(input("Enter a number "))
      value = math.sin(x)
      print(f"{operator} ({x})= {value}")
  elif operator == "cos":
       x = float(input("Enter a number "))
       value = math.cos(x)
       print(f"{operator} ({x})= {value}")
  elif operator == "sqrt":
      x = float(input("Enter a number "))
      value = math.sqrt(x)
      print(f"{operator} ({x})= {value}")
  else:
      x = float(input("Enter the first number"))
      y = float(input("Enter the second number"))
      
      if operator == "+":
         value = addition(x,y)
         print(f"{x} {operator} {y} = {value}")
      elif operator == "-":
         value = substraction(x,y)
         print(f"{x} {operator} {y} = {value}")
      elif operator == "*":
        value = multiplication(x,y)
        print(f"{x} {operator} {y} = {value}")
      elif operator =="/":
        value = division(x,y)
        print(f"{x} {operator} {y} = {value}")
      elif operator =="^":
        value = math.pow(x,y)
        print(f"{x} {operator} {y} = {value}")
      else:
        print("Please enter valid operation")