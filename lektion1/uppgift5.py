#skapa en lista med 3 favoritfilmer
#lägg till film med append()
#skriv ut hela listan 
#skriv ut endast första och sista filmen
film1 = input("Skriv en favoritfilm: ")
film2 = input("Skriv en favoritfilm: ")
film3 = input("Skriv en favoritfilm: ")
my_films = [film1, film2, film3]
print("Här är filmerna: ") 
for film in my_films:
    print(film)

while True:
    answer = input("Vill du lägga till en film? j/n: ").lower()
    if answer == "j":
        film4 = input("Vilken film? ")
        my_films.append(film4)
        break
    elif answer == "n":
        print("Okej detta är dina favoritfilmer: ", my_films)
        break
    else: 
        print("Skriv bara 'j' eller 'n'.")
print("Denna är först i listan:", my_films[0])
print("senaste filmen du la till: ", my_films[-1])
