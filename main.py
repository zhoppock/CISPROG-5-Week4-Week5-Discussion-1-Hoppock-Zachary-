"""
-print the message "== Welcome to the food store! =="

-budgetString will be inputted as an float of "Enter budget for picnic lunch: $" Enter a number

-applePrice is 0.29
-cheesePrice is 7.00
-breadPrice is 2.49

-print the message ">>The price per apple is $ string(applePrice)"
-print the message ">>The price per pound of cheese is $ string(cheesePrice)"
-print the message ">>The price per loaf of bread is $string(breadPrice)"

-option will be initialized as "y"
-numItems will be initialized as 0
-total will be initialized as 0.00

-while option is still "y":
  -item will be inputted as "Enter what type of item you would like to order (apple; bread; cheese): " Enter the type of food
  -if item is "apple":
    -apples will be inputted as an integer of "How many apples would you like? " Enter a number
    -numItems will be numItems plus apples
    -appleCost will be apples multiplied by applePrice
    -total will be total plus appleCost
    -print the message "string(apples) apple(s) will cost $ string(appleCost)"
  -else if item is "cheese":
    -cheese will be inputted as an integer of "How many pounds of cheese would you like? " Enter a number
    -numItems will be numItems plus cheese
    -cheeseCost will be cheese multiplied by cheesePrice
    -total will be total plus cheeseCost
    -print the message "string(cheese) pound(s) of cheese will cost $ string(cheeseCost)"
  -else if item is "bread":
    -bread will be inputted as an integer of "How many loaves of bread would you like? " Enter a number
    -numItems will be numItems plus bread
    -breadCost will be bread multiplied by breadPrice
    -total will be total plus breadCost
    -print the message "string(bread) loaf/loaves of bread will cost $ string(breadCost)"
  -else:
    -print the message "Invalid selection.  Please try again."
  -if item is either "apple", "cheese", or "bread":
    -print the message "You have ordered string(numItems) items so far.  Current total is $ string(total)"
    -option will be inputted as "Would you like to order more? (y/n): " Enter either y or n
  -if total is greater than budget:
    -print the message "Budget has been exceeded.  Proceeding to checkout."
    -option will now be "n"
-print the message "You have ordered string(numItems) items.  Final total is $ string(total)"
-if total is greater than budget:
  -overBudget will be total minus budget
  -print the message "However, you are $ string(overBudget) over your budget.")
-else:
  -underBudget will be budget minus total
  -print the message "Your change is $ string(underBudget)"
"""

print("== Welcome to the food store! ==")

budget = float(input("\nEnter budget for picnic lunch: $"))

applePrice = 0.29
cheesePrice = 7.00
breadPrice = 2.49

print("\n >>The price per apple is $%0.2f" % (applePrice))
print(" >>The price per pound of cheese is $%0.2f" % (cheesePrice))
print(" >>The price per loaf of bread is $%0.2f" % (breadPrice))

option = "y"
numItems = 0
total = 0.00

while option == "y":
  item = input("\nEnter what type of item you would like to order (apple; bread; cheese): ")
  if item == "apple":
    apples = int(input("\nHow many apples would you like? "))
    numItems += apples
    appleCost = apples * applePrice
    total += appleCost
    print(str(apples), "apple(s) will cost $%0.2f" % (appleCost))
  elif item == "cheese":
    cheese = int(input("\nHow many pounds of cheese would you like? "))
    numItems += cheese
    cheeseCost = cheese * cheesePrice
    total += cheeseCost
    print(str(cheese), "pound(s) of cheese will cost $%0.2f" % (cheeseCost))
  elif item == "bread":
    bread = int(input("\nHow many loaves of bread would you like? "))
    numItems += bread
    breadCost = bread * breadPrice
    total += breadCost
    print(str(bread), "loaf/loaves of bread will cost $%0.2f" % (breadCost))
  else:
    print("\nInvalid selection.  Please try again.")
  if item == "apple" or item == "cheese" or item == "bread":
    print("\nYou have ordered", str(numItems),"items so far.  Current total is $%0.2f" % (total))
    option = input("Would you like to order more? (y/n): ")
  if total > budget:
    print("\nBudget has been exceeded.  Proceeding to checkout.")
    option = "n"
print("\nYou have ordered", str(numItems),"items.  Final total is $%0.2f" % (total))
if total > budget:
  overBudget = total - budget
  print("However, you are $%0.2f over your budget." % (overBudget))
else:
  underBudget = budget - total
  print("Your change is $%0.2f" % (underBudget))