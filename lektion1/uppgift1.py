#Program som frågar efter ålder och namn
#Kontrollera om personen är myndig
#loopa en personlikg hälsning 5 ggr

name = input("Vad heter du? ")

while True:
    try:
        age = int(input("Hur gammal är du? "))
        break
    except ValueError:
        print("Du måste skriva ett heltal!")

if age >= 18:
    for i in range(5):
        print(f"Hej {name} du är {age} och myndig. Grattis!", i)
elif age < 18:
    for i in range(5):
        print(f"Hej {name} du är {age} gammal och inte myndig.", i)  
