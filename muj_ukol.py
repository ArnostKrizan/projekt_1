"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Arnost Krizan
email: KrizanA@seznam.cz
discord: arnost0782
"""
# import ...

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

kapitoly = len(TEXTS)
oddelovac = "-" * 40

user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
podminka_splnena = False

while True:
    login = input("Press your UserName: ")
    password = input("Press your password: ")
    print("$ python projekt1.py")
    print("username:", login)
    print("password:", password)
    print(oddelovac)
    
    if login in user and user[login] == password:
        print(f"Welcome to the app, {login}.\nWe have {kapitoly} texts to be analyzed.")
        print(oddelovac)
        podminka_splnena = True
        break
    else:
        if not podminka_splnena:
            print("unregistered user, terminating the program..")

textIndex = []
podminka_textu = False

while True:
    cislo_textu = int(input(f"Enter a number btw. {len(TEXTS[-1:])} and {len(TEXTS)} to select: "))    
    print(oddelovac)  
    if 1 <= cislo_textu <= len(TEXTS):
        textIndex = [cislo_textu - 1]
        podminka_textu = True
        break
    else:
        if not podminka_textu:
            print("Spatna hodnota textu ")

textSplit = TEXTS[cislo_textu-1].split()
word_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
number_count = 0
sum_of_numbers = 0

for word in textSplit:
    word_count += 1
        # Počet slov začínajících velkým písmenem
    if word.istitle():
        titlecase_count += 1
        # Počet slov psaných velkými písmeny
    elif word.isupper():
        uppercase_count += 1
        # Počet slov psaných malými písmeny
    elif word.islower():
        lowercase_count += 1
        # Počet čísel a suma všech čísel
    elif word.isnumeric():
        number_count += 1
        sum_of_numbers += int(word)

print("There are", word_count, "words in the selectd text.")
print("There are:", titlecase_count, "titlecase words.")
print("There are:", uppercase_count, "uppercase words.")
print("There are:", lowercase_count, "lowercase words.")
print("There are:", number_count, "numeric strings.")
print("The sum of all the numbers", sum_of_numbers)

cetnost = [len(obj) for obj in textSplit]
setcetnost = set(cetnost)
cetnostdict = {}

for length in setcetnost:
    cetnostdict[length] = cetnost.count(length)

max_value = max(cetnostdict.values())
max_key = max(cetnostdict.keys())
max_keyLen = len(str(max_key))
len_oc = len("OCCURENCES")
occRight = 1
if ((max_value-len_oc)/2+1) % 2 == 0: occRight = 0

print(oddelovac)
print(f"{'LEN|': <{max_keyLen+1}}{' ': >{(max_value-len_oc)/2+1}}{'OCCURENCES'}{' ': <{(max_value-len_oc)/2+occRight}}{'|NR.'}")
print('-' * 40)

for key, value in cetnostdict.items():
    print(f"{key: >{max_keyLen+1}}|{'*' * value: <{max_value+1}}|{value}")
