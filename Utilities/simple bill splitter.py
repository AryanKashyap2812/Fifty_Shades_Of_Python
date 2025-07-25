"""
Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

no_of_people = int(input("How many people are there in the group: ").strip())
names = []

for i in range(no_of_people):
  name = input(f"{i+1}. Enter name: ")
  names.append(name)
  
bill = int(input("Enter total bill amount: ").strip())  
bill_split = round(bill/no_of_people,2)

print("*"*50)
print("Each person owes: ",bill_split)
for i in range(no_of_people):
  print(f" {i+1}. {names[i]} owes {bill_split} rupees")

print("*"*50)