ascii_art = """
 /$$$$$$$  /$$      /$$ /$$$$$$        /$$$$$$   /$$$$$$  /$$        /$$$$$$ 
| $$__  $$| $$$    /$$$|_  $$_/       /$$__  $$ /$$__  $$| $$       /$$__  $$
| $$  \ $$| $$$$  /$$$$  | $$        | $$  \__/| $$  \ $$| $$      | $$  \__/
| $$$$$$$ | $$ $$/$$ $$  | $$        | $$      | $$$$$$$$| $$      | $$      
| $$__  $$| $$  $$$| $$  | $$        | $$      | $$__  $$| $$      | $$      
| $$  \ $$| $$\  $ | $$  | $$        | $$    $$| $$  | $$| $$      | $$    $$
| $$$$$$$/| $$ \/  | $$ /$$$$$$      |  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/
|_______/ |__/     |__/|______/       \______/ |__/  |__/|________/ \______/
"""
line = "________________________________________________________________________________"
print(line)
print(ascii_art)
print(line)
print("\n")

weight = input("Please enter your weight in kg: ")
height = input("Please enter your height in cm: ")

height_m = float(height)/100
bmi = int(float(weight)/(float(height_m)**2))

print("\nYour BMI is " + str(bmi) + "\n")

if bmi < 18.5:
    message = "Eat more food blud 💀!"
    prompt = "Press any key to kill yourself..."
elif 18.5 < bmi <25:
    message = "Wow you're so fit daddy 🥵!"
    prompt = "Press any key to kill yourself..."
elif bmi > 25:
    message = "Stop eating you fat fuck 🤡!"
    prompt = "Press any key to kill yourself..."

print(message + "\n")
input(prompt)