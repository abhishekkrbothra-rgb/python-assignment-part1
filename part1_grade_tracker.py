# Task 1: Data Parsing & Profile Cleaning
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("--- Task 1: Data Cleaning & Validation ---")
for student in raw_students:
    # Cleaning name: removing spaces and fixing to Title Case
    clean_name = student["name"].strip().title()
    
    # Converting roll to integer
    clean_roll = int(student["roll"])
    
    # Splitting marks string into a list of integers
    clean_marks = [int(m) for m in student["marks_str"].split(",")]
    
    # Validation: checking if name contains only alphabets/spaces
    is_valid = all(part.isalpha() for part in clean_name.split())
    status_icon = "✓ Valid name" if is_valid else "X Invalid name"
    
    print(f"{clean_name}: {status_icon}")
    
    # Store the cleaned data
    cleaned_info = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
    cleaned_students.append(cleaned_info)
    
    # Printing the formatted profile card
    print("================================")
    print(f"Student  : {clean_name}")
    print(f"Roll No  : {clean_roll}")
    print(f"Marks    : {clean_marks}")
    print("================================\n")

# Extra requirement for Roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"Roll 103 - Upper: {s['name'].upper()}, Lower: {s['name'].lower()}\n")

# Task 2: Marks Analysis (Focusing on Ayesha)
print("--- Task 2: Marks Analysis (Ayesha) ---")
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
ayesha_marks = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
    m = ayesha_marks[i]
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    print(f"{subjects[i]}: {m} ({grade})")

# Task 3: Class Performance Summary
print("\n--- Task 3: Class Summary ---")
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

all_averages = []
passed = 0
failed = 0

print(f"{'Name':<15} | {'Average':<7} | {'Status'}")
print("-" * 35)

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    all_averages.append(avg)
    
    if status == "Pass": passed += 1
    else: failed += 1
    
    print(f"{name:<15} | {avg:<7.2f} | {status}")

print(f"\nPassed: {passed}, Failed: {failed}")
print(f"Class Average: {round(sum(all_averages)/len(all_averages), 2)}")

# Task 4: String Manipulation
print("\n--- Task 4: Essay Utility ---")
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science. "
clean_essay = essay.strip() # Step 1
print(f"Title Case: {clean_essay.title()}") # Step 2
print(f"Python count: {clean_essay.lower().count('python')}") # Step 3
replaced_essay = clean_essay.replace("python", "Python 🐍") # Step 4
print(f"Replaced: {replaced_essay}")
sentences = replaced_essay.split(". ") # Step 5
for idx, sent in enumerate(sentences, 1): # Step 6
    if sent:
        formatted = sent.strip()
        if not formatted.endswith("."): formatted += "."
        print(f"{idx}. {formatted}")
