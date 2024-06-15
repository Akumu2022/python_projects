print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+      The Ice Cream Shop       +")
print("+            Welcome            +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")


def total_cost(container_price,scoop_price,topping_price=0):
    total_price=container_price+scoop_price+topping_price
    print(f"Your total cost is {total_price}")

container = int(input("Choose a container for your ice cream.\nEnter 1 for cup 2 for cone: "))

if container==1:
    container_price=50
    print(f"You choose a cup that will cost you: {container_price}\n")
elif container==2:
    container_price=80
    print(f"You choose a cone that will cost you: {container_price}\n")
else:
    print("Invalid input")
    
print("How many scoops would you like to put (1,2,3 or 4)?")
scoops=int(input("Input here: \n"))
if scoops==1:
    scoop_price=1
    print(f"This will cost you: {scoop_price}\n")
elif scoops == 2:
    scoop_price=2
    print(f"This will cost you: {scoop_price}\n")
elif scoops == 3:
    scoop_price=3
    print(f"This will cost you: {scoop_price}\n")
elif scoops == 4:
    scoop_price=4
    print(f"This will cost you: {scoop_price}\n")
else:
    print("Invalid Input")
    

total_cost(container_price,scoop_price)

    
    

    
print("You can add toppings of your choice if you wish")
print("1. Flake(ksh 40)\n2. Chocolate Sprinkle(ksh 30)\n3. Strawberry Coulis(ksh 60)\n")

toppings=int(input("Enter a number to choose toppings\n"))
if toppings==1:
    topping_price=40
    # print(f"This will cost you: {topping_price}\n")
    
elif toppings==2:
    topping_price=30
    # print(f"This will cost you: {topping_price}\n")
    
elif toppings==3:
    topping_price=60
    # print(f"This will cost you: {topping_price}\n")
else:
    print("Invalid Input")

total_cost(container_price,scoop_price,topping_price)    
    

    
    


    

  
