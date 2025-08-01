"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime

today_learning = input("Enter what you learned today: ").strip()
rating = int(input("Rate your days productivity in (1-5): ").strip())

now=datetime.datetime.now()
date_str=now.strftime("%Y-%m-%d - %I:%M %p")

journal = f"\n{date_str}\n{today_learning}"

if rating:
    rating_format = f"\nProductivity Rating: {rating}/5"
    journal+=rating_format
    
    
with open("learning_journal.txt","a") as file:
    file.write(f"{journal}\n")