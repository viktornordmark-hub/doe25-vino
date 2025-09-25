'''
Bygg ett litet program som:
1. Frågar användaren efter namn, ålder och favoritfärg.
2. Sparar informationen i en dictionary.
3. Lägger till användarens favoritfilmer i en lista.
4. Skriver ut en personlig hälsning och sammanfattning av informationen.
5. Om användaren är under 18, skriv en extra rad: "Du är minderårig."
'''
def print_films(films):
    for film in films:
        print(film)

my_dict = {} #skapa dictionary

my_dict["name"] = input("Vad heter du? ")
my_dict["age"] = int(input("Hur gammal är du? "))
my_dict["color"] = input("Vilken är din favoritfärg? ")

film1 = input("Skriv en favoritfilm: ")
film2 = input("Skriv en till favoritfilm: ")
film3 = input("Skriv en sista favoritfilm: ")
my_films = [film1, film2, film3] #skapa lista

for key, value in my_dict.items():
    if key == "name":
        name = value
    elif key == "age":
        age = value
    elif key == "color":
        color = value
        break

print(f"Hej {name}, du är {age} gammal och {color} är din favoritfärg!")
print("Här är dina favoritfilmer: ")
print_films(my_films)
if age < 18:
    print("Du är omyndig!")
