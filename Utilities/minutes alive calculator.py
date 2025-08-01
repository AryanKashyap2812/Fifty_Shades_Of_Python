"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""
age_in_years = float(input("Enter your age in years: "))

age_in_days = age_in_years*365.25
age_in_hours=age_in_days*24
age_in_minutes= age_in_hours*60

print("You are approximately:")
print(f" - {format(age_in_days,',')} days old")
print(f" - {format(age_in_hours,',')} hours old")
print(f" - {format(age_in_minutes,',')} minutes old")