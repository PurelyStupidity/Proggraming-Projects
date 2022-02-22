"""
Programming Project #1

MGS Childcare

Introduction

You are to design and write a program that will be used by a child day-care centre. It will keep track of children throughout the day. There will be many features in the program, but we will take it a step at a time and build each one in turn.

Specifications

The program should do the following:

1. Ask the user to either check a child in or out of the day care.

2. If the user wants to check a child in, it should ask for the name of the child and keep track of it.

3. If the user wants to check out a child, it should ask for the name of the child and find it and remove it from the list. If there is no child by that name, it should display an error.

4. Calculate and print the charge for looking after the current number of children for a given number of hours ($12 per hour per child).

5. There should also be an ability for the user to print out a list of all children checked into the day-care.

6. There should be a menu asking the user what to do next, and allow the user to stop the program at the end of the day (ask for help on how to do this).

Modular structure

Decompose the problem into programmable chunks

Each chunk needs to be constructed and thoroughly tested independently, before becoming part of the program. You need to keep a complete record of your testing and development.

● A main function - to have a welcome screen and present user with a menu selection

● The main function also needs to show a “Goodbye” message if the user wants to exit

● A dropoff function - to ask user to input the name of a child and then confirm that the name has been added to the list

● A pickup function - to ask user for name of child, search the list for that name and either tell the user to check name if the name isn’t in the list, or confirm that the name has been removed from the roll

● A calccost function - to ask the user to enter the number of hours to charge

● A printroll function - to enable user to check the roll list

Indexed data structure (list)

Think about how you will structure your list:

(Indexed data structure just means ‘list’)

Storing the names of the child clients will need to be done using a list. It will look something like this:

Possible Menu code

choice=0

while choice != 5:

print("-----------------------------------------------------------------------")

print("Welcome to MGS Childcare")

print("What would you like to do? Please choose one of the items below")

print("-----------------------------------------------------------------------")

print()

print("1 Drop off a child")

print("2 Pick up a child")

print("3 Calculate cost")

print("4 Print roll")

print("5 Exit the system")

print()

choice=int(input("Enter your choice (number between 1 and 5): "))

print()

if choice==1:

dropOff()

elif choice==2:

pickUp()

elif choice==3:

calcCost()

elif choice==4:

printRoll()

else:

print("Goodbye")"""
