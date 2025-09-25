#dictionary
# Skapa en dictionary för en användare med nycklarna 'namn', 'ålder', 'stad'.
# Skriv ut värdena med print().
# Lägg till en ny nyckel 'favoritfärg'.
# Loopa igenom dictionaryn och skriv ut alla nycklar och värden
#ändrade och la in i dictionary manuellt

my_dict = {}

my_name = input("Vad heter du? ")
my_dict["name"] = my_name
my_age = input("Hur gammal är du? ")
my_dict["age"] = my_age
my_city = input("Vilken stad bor du i? ")
my_dict["city"] = my_city
my_color = input("Vilken är din favoritfärg? ")
my_dict["color"] = my_color
#print(my_dict) #placeholder comment#

for key, value in my_dict.items():
    print(f"{key}: {value}")
