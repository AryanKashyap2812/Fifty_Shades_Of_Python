"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string,random,getpass

def check_password_strenght(password):
    issues=[]
    if len(password)<8:
        issues.append("Too short (minimum 8 characters)")
    if not any(character.islower() for character in password):
        issues.append("Missing lower case letter")
    if not any(character.isupper() for character in password):
        issues.append("Missing upper case letter")
    if not any(character.isdigit() for character in password):
        issues.append("Missing digits in password")
    if not any(character in string.punctuation for character in password):
        issues.append("Missing special characters")
    return issues

def generate_strong_password(length=12):
    chars=string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter your password: ")
issues = check_password_strenght(password)

if not issues:
    print("You password is strong. You are good to go!")            
else:
    print("You got a weak password.")
    for issue in issues:
        print(f"- {issue}")
        
    suggestion = generate_strong_password()
    print("\nSuggesting a new password:")
    print(suggestion)    