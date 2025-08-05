"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Phone","Email"])
        
def add_contact():
    name=input("Name: ").strip()
    phone=input("Phone: ").strip()
    email=input("Email: ").strip()
    
    # Check for duplicates
    with open(FILENAME,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists!")
                return
            
    with open(FILENAME,'a',encoding="utf-8") as f:
        writer = csv.writer(f)    
        writer.writerow([name,phone,email])
        print("Contact added!")
        
def view_contacts():
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        rows=list(reader)
        
        if len(rows)<1:
            print("No contacts found")
            return
        
        print("Your contacts:")
        
        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()
        
def search_contacts():
    term = input("Enter the name to search: ").strip().lower()
    found = False
    
    with open(FILENAME,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row['Name']} | {row['Phone']}")
                found=True
                
        if not found:
            print("NO match found!")        
            
def update_contacts():
    name = input("Enter the name whose contacts you want to update: ").strip().lower()
    updated = False

    # Read all contacts
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        contacts = list(reader)

    # Update the contact
    for row in contacts:
        if name in row["Name"].lower():
            new_phone = input("New phone number: ").strip()
            new_email = input("New email id: ").strip()
            row["Phone"] = new_phone
            row["Email"] = new_email
            updated = True

    # Write back to CSV if updated
    if updated:
        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(contacts)
        print("Contact updated!")
    else:
        print("No matching contact found.")
   
def main():
    while True:
        print("Contact Book")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update existing contacts")
        print("5. Exit")
        
        choice = input("Enter an option from 1 to 5: ").strip()
        
        if choice == "1":
            add_contact()
            
        elif choice == "2":
            view_contacts()
            
        elif choice == "3":
            search_contacts()
            
        elif choice == "4":
            update_contacts()
            
        elif choice == "5":
            print("Thanks for using our software.")
            break
        
        else: 
            print("Invalid choice.")
            
if __name__=="__main__":
    main()