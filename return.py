print("/************************/")
print("/**                    **/")
print("/**                    **/")
print("/* Return on Investment */")
print("/*      Calculator      */")
print("/*                     */")
print("/***********************/\n")

cost=int(input("Enter amount spent i.e Cost: "))
sales=int(input("Enter amount accumulated i.e Sales: "))

def profit_or_loss():
    returns=sales-cost
    if sales>cost:
        print(f"You made a profit of {returns}\n")
    elif sales<cost:
        returns=returns* -1
        print(f"You made a loss of {returns}\n")

def return_on_invest():
    roi=((sales-cost)/cost)*(100)
    print(f"Your Return On Investment is: {roi}\n")
        
profit_or_loss()
return_on_invest()