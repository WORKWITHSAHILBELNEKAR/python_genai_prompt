animals_and_sounds = {
    "Chicks": "chick",
    "Duck": "quack",
    "Turkey": "gobble",
    "Pig": "oink",
    "Cow": "moo",
    "Cat": "meow",
    "Mule": "Heehaw",
    "Dog": "bow wow",
    "Turtle": "nerp"
}

with open("poem.txt", "r") as file:
    template_poem = file.read()

completed_poem = ""
for animal, sound in animals_and_sounds.items():
    animal_poem = template_poem.replace("%ANIMAL%", animal).replace("%SOUND%", sound)
    completed_poem += animal_poem + "\n"  

with open("completed_poem.txt", "w") as file:
    file.write(completed_poem)

print("The completed poem has been written to 'completed_poem.txt'.")
