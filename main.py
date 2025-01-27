import random
import time

# Updated list of possible destinations
destinations = [
    ("Isle of Skye", "Scotland, United Kingdom"),
    ("Cotswolds", "England, United Kingdom"),
    ("Easter Island", "Chile"),
    ("Torres del Paine", "Chile"),
    ("Norwegian Fjords", "Norway"),
    ("Zermatt", "Switzerland"),
    ("Hallstatt", "Austria"),
    ("Sintra", "Portugal"),
    ("Colmar", "France"),
    ("Banff", "Canada")
]

# Asking for user input
print("Welcome to DestinyAI, the destiny that awaits you!")
name = input("What is your name? ")

# Greeting and introduction
print(f"Hello {name}, I am DestinyAI, your friendly assistant. \nI will analyze the data with the stars to find your perfect travel destination.")
time.sleep(3)

color = input("What is your favorite color? ")
animal = input("What is your spirit animal? ")

# Calculate the total number of characters
total_characters = len(name) + len(animal)

# Use the total number of characters to choose a destination
index = total_characters % len(destinations)
city, country = destinations[index]

# Analyzing the stars
print("Analyzing the data with the stars...")
time.sleep(1)
print("✨✨✨")
time.sleep(2)

# Displaying the destination to the user with a pause
print("Almost there...")
time.sleep(2)
print(f"🌟 {name}, according to the stars and your affinity for the color {color} and the {animal},\n🗺️ your destination is: {city}, {country}. ✈️🌍 Get ready for an unforgettable adventure! 🌟")
