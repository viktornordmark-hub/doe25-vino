# startmeny 
def calc_avg_age():
    total_age = sum(students.values())
    total_students = len(students) 
    average_age = total_age / total_students
    return average_age
'''
def print_heading(text):
    print("="*len(text))
    print(text)
    print("="*len(text))
'''
def add_student(name, age, student_dict):
    student_dict[name] = age
    print(f"{name} har lagts till med åldern {age}")

students = {}

'''
header_text1 = input("")
print_heading(header_text1)
header_text2 = input("")
print_heading(header_text2)
'''


input_menu = True
while input_menu:
    menu_choice = input("--MENY--:\n1. Lägg till student\n2. Lista alla studenter\n3. Sök Student\n4. Snittålder\n5. Avsluta\n:")
    if menu_choice == '1':
        name = input("Vad heter studenten? ")
        age = int(input("Hur gammal är studenten? "))
        add_student(name, age, students)
    elif menu_choice == '2':
        for key, value in students.items():
            print(f"{key}, {value} år.")
    elif menu_choice == '3':
        name_search = input("Ange namn: ")
        if name_search in students:
            print(f"{name_search}, {students[name_search]} år gammal.")
        else: print(f"{name_search} finns inte i listan.") 
    elif menu_choice == '4':
        print(f"Snittåldern är {calc_avg_age():.2f} år")
    elif menu_choice == '5':
        input_menu = False
    else:
        print("Ogiltig inmatning!\nFörsök igen.")       
