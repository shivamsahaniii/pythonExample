# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

studentInfo = {"Shivam": 80, "Ashish": 90, "Vijay": 99, "Vedant": 85, "Aniket": 95}
print(f"Please select A, B, C, D \n A - Add a student \n B - Update marks \n C - Search for a student \n D - Display all students and marks")
option = input("Enter your option: ")

def dicOperations(option, studentInfo):

    match option:
        case 'A':
            AddStudent = input("Enter the name: ")
            AddMarks = int(input("Enter the marks:"))
            studentInfo[AddStudent] = AddMarks
            print(studentInfo)
        case 'B':
            AddStudent = input("Enter the name: ")
            AddMarks = int(input("Enter the upadted marks:"))
            studentInfo.update({AddStudent: AddMarks})
            print(studentInfo)
        case 'C':
            AddStudent = input("Search the name: ")
            student = studentInfo[AddStudent]
            print(f"{AddStudent}: {student}")
        case 'D':
            print(studentInfo)

dicOperations(option, studentInfo)


# studentInfo = {"Shivam": 80, "Ashish": 90, "Vijay": 99, "Vedant": 85, "Aniket": 95}

# print("""
# Select an option:
# A - Add a student
# B - Update marks
# C - Search for a student
# D - Display all students and marks
# """)

# option = input("Enter your option: ").upper()

# def dicOperations(option, studentInfo):
#     match option:
#         case 'A':
#             name = input("Enter the name: ")
#             marks = int(input("Enter the marks: "))
#             studentInfo[name] = marks
#             print("Student added successfully.")

#         case 'B':
#             name = input("Enter the name: ")
#             if name in studentInfo:
#                 marks = int(input("Enter the updated marks: "))
#                 studentInfo[name] = marks
#                 print("Marks updated.")
#             else:
#                 print("Student not found.")

#         case 'C':
#             name = input("Enter the name to search: ")
#             if name in studentInfo:
#                 print(f"{name}: {studentInfo[name]}")
#             else:
#                 print("Student not found.")

#         case 'D':
#             for name, marks in studentInfo.items():
#                 print(f"{name}: {marks}")

#         case _:
#             print("Invalid option.")

# dicOperations(option, studentInfo)