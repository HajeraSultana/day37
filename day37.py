print("🌟Star Wars Name Generator🌟")
print()
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in"). split()
first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
country = all[3].strip()

print()
fullname = f"Your Star Wars name is {first[0:3].title()}{last[0:3].lower()} {maiden[0:2].title()}{country[-3:].lower()}"

print(fullname)

