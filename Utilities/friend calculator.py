"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1,name2):
   name1,name2=name1.lower(),name2.lower()
   score=0
   shared_letters=set(name1)&set(name2)
   vowels=set('aeiou')
   score+=len(shared_letters)*50
   score+=len(vowels&shared_letters)*10
   
   return min(100,score)

def run_friendship_calculator():
   print("Friendship Compatibility Calculator")
   name1=input("Enter friend 1 name: ")
   name2=input("Enter friend 2 name: ")
   
   score=friendship_score(name1,name2)
   
   return score

score=run_friendship_calculator()
print("*"*50)

if score >=75:
   print(f"You both are {score}% alike.\nYou both are like chai smosa, made for each other.")
else:
   print(f"You both are {score}% alike.\nMay be opposite attract each other.")

print("*"*50)   