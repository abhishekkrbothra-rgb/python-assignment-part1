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
