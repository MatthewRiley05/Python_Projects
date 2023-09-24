import time
termConversions = {
    "AOT": "Attack on Titan",
    "AOE": "Anime Original Ending",
    "ANR": "Akatsuki no Requiem",
    "KFT": "King Fritz Theory",
    "FT": "Founding Titan",
    "AT": "Attack Titan",
    "WHT": "Warhammer Titan",
    "CT": "Colossal Titan"
}
while True:
    search_term = input("Enter the abbreviation: ").upper()
    if search_term in termConversions:
        print(termConversions[search_term])
    else:
        print("Error abbreviation not found.")

    print()

    continue_program = input("Do you want to continue? (y/n): ")
    if continue_program.lower() != "y":
        break

print("Program has been terminated")
time.sleep(3)
