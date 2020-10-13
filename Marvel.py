#importeren van library's
import urllib.parse
import requests
import hashlib
import os

#Hier maken we een variable voor de API URL & geven we ts een waarde van 1 om in de API call, md5 hash te kunnen verwerken 
main_api = "https://gateway.marvel.com:443/v1/public/characters?"
ts = "1"

#hier vragen we de user om een public en private key in te geven, Private key hebben we nodig om de API call te maken.
publicKey = input("Public key: ")
privateKey = input("Private key: ")

#Hier maken we de API call hash
hash_text = ts + privateKey + publicKey
hash_object = hashlib.md5(hash_text.encode())
md5_hash = hash_object.hexdigest()

#hier gaan we het scherm clearen zodat de user op een proper scherm de applicatie kan gebruiken
os.system('clear')

#while true heb ik gebruikt zodat de user meerdere characters kan opvragen
while True:
    
    #hier vragen we voor een character naam, je hebt ook de optie om de applicatie hier te stoppen
    char = input("Character to search for: ")
    if char == "quit" or char == "q":
        break
    
    #Hier gaan we de API call samenstellen door de API URL, character naam, ts, publickey en de md5 hash samen te voegen tot één URL
    url = main_api + urllib.parse.urlencode({"name":char, "ts":ts, "apikey":publicKey, "hash":md5_hash})
    
    #hier gaan we de json output opslagen in de variable json_data
    json_data = requests.get(url).json()
    
    #hier gaan we het aantal comics opzoeken waarin het gekozen character in verschijnt.
    Amount = (json_data["data"]["results"][0]["comics"]["available"])

    #hier vragen we de naam van het character op dat gekozen is.
    character = ((json_data["data"]["results"][0]["name"]))

    #hier gaan we de output voor de user samenstellen.
    print("Description: " + (json_data["data"]["results"][0]["description"]))
    print("=============================================\n")
    print(character + " appears in " + str(Amount) + " comics")
    print("These are some examples:\n")
    for each in json_data["data"]["results"][0]["comics"]["items"]:
            print((each["name"]))
    print("=============================================\n")
    



    