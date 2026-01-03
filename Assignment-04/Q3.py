# Concept: Encapsulation
# Q3. Create a class Student with private attributes _name, _roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_info(self):
        return self.__name, self.__roll_no, self.__marks

    def set_info(self, new_name, new_roll_no, new_marks):

        if new_name.strip() == "":
            print("Name cannot be empty")
            return

        if not (1 <= new_roll_no <= 100):
            print("Roll number must be between 1 and 100")
            return

        if not (0 <= new_marks <= 100):
            print("Marks must be between 0 and 100")
            return

        # Update ONLY if all validations pass
        self.__name = new_name
        self.__roll_no = new_roll_no
        self.__marks = new_marks


# ---- Testing ----
stud01 = Student("shivam", 20, 60)
print(stud01.get_info())

validate = stud01.set_info("shivansh", 56, 10)   # Invalid marks
if (validate == True):
    print(stud01.get_info())


# if you want input from user then 
# name = input("Enter student name: ")
# roll_no = int(input("Enter roll number (1–100): "))
# marks = int(input("Enter marks (0–100): "))

# stud01 = Student(name, roll_no, marks)

# print("Initial data:", stud01.get_info())

# # Update info
# new_name = input("Enter new name: ")
# new_roll_no = int(input("Enter new roll number (1–100): "))
# new_marks = int(input("Enter new marks (0–100): "))

# stud01.set_info(new_name, new_roll_no, new_marks)

# print("Updated data:", stud01.get_info())
