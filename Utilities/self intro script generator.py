"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime

name = input("Please enter your name here: ").strip()
age = int(input("Please enter your age here: ").strip())
city= input("Please enter your city here: ").strip()
profession = input("Please enter your profession here: ").strip()
hobby = input("Please enter your hobby here: ").strip()

para= (f"Hello! My name is {name} and I am {age} years old. " 
       f"I live in {city}. My profession is {profession} and I like to {hobby}."
       f" Nice to meet you.")

current_date=datetime.date.today().isoformat()

para+=f"\nLogged on: {current_date}"

border="*"*118

final_message=f"{border}\n{para}\n{border}"

print("\n" + final_message)