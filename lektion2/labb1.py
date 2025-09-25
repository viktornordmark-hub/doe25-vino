# startmeny 

def add_student(name, age, student_dict):
    student_dict[name] = age
    print(f"{name} har lagts till med åldern {age}")

students = {}


input_menu = True
while input_menu:
    menu_choice = input("Gör ett val:\n1. Lägg till student\n2. Lista alla studenter\n3. Avsluta\n:")
    if menu_choice == '1':
        name = input("Vad heter studenten? ")
        age = int(input("Hur gammal är studenten? "))
        add_student(name, age, students)
    elif menu_choice == '2'
