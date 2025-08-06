"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
   students={}
   
   while True:
      name = input("Enter name of the student or enter done to exit: ").strip()
      
      if name.lower()=="done":
         break
      if name in students:
         print("Student already exists.")
         continue
      
      try: 
         marks = float(input(f"Enter marks of {name}: ")) 
         students[name]=marks
      except ValueError:
         print("Enter valid marks")
         
   return students

def display_report(students:dict):
   if not students:
      print("No student data.")
      return
   
   marks = list(students.values())
   max_score=max(marks)
   min_score=min(marks)
   average=sum(marks)/len(marks)
   
   topper=[name for name,score in students.items() if score == max_score]
   bottomer=[name for name,score in students.items() if score == min_score]
   
   print("Students marks report: ")
   print("-"*30)
   print(f"Total students: {len(students)}")
   print(f"Average marks of each student: {average}")
   print(f"Highest marks: {max_score} by {', '.join(topper)}")
   print(f"Lowest marks: {min_score} by {', '.join(bottomer)}")
   print("-"*30)
   print("Detailed Marks: ")
   for name,score in students.items():
      print(f"-{name} : {score}")

students = collect_student_data()
display_report(students)