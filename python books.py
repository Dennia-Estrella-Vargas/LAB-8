#Aaradhya Sharma CS 135
#Dennia Estrella-Vargas CS 135
#Importing math library for calculations.
import math

#Total function to calculte the total cost of the books.
def total(bookQuantity, bookPrice):
  #calculate the actual base price for the total number of books
  actualPrice=bookQuantity*bookPrice
  #caculate the total sales tax (9.5%)
  totalTax=bookQuantity*bookPrice*0.095
  #calculate the shipping cost ($3 per book)
  shippingCost=bookQuantity*3
  #calculate the total cost by adding the total tax and shipping cost to the actual price.
  totalCost=actualPrice + totalTax + shippingCost
  return totalCost;

ans='y'
#run while until no
while(ans=='y'or ans=='Y'):
  #take user input
  price=float(input("What is the price of the book?"))
  quantity=int(input("How many books will be ordered?"))
  #function calling and storing the returned value
  totalCost=round(total(quantity, price),2)
  #print the returned value 
  print(f"Total is ${totalCost}")
  ans=input("Any more books (y/n)?")
print("Have a nice day.")