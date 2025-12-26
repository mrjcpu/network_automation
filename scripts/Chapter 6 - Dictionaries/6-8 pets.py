pets = {
    "rattlesnake": {
        "type": "reptile",
        "age": 4,
        "habitat": "desert",
        "dietary": "carnivore",
        "body covering": "scales"
    },
    "parrot": {
        "type": "aviary",
        "age": 11,
        "habitat": "jungle",
        "dietary": "carnivore",
        "body covering": "feathers"
    },
    "dolphin": {
        "type": "mammal",
        "age": 5,
        "habitat": "ocean",
        "dietary": "carnivore",
        "body covering": "skin"
    },
    "gorilla": {
        "type": "mammal",
        "age": 5,
        "habitat": "jungle",
        "dietary": "herbivore",
        "body covering": "fur"
    }
}
for pet, pet_info in pets.items():
    print("Pet Information:")
    print(f"\tType: {pet_info['type'].title()}")
    print(f"\tAge: {pet_info['age']}")
    print(f"\tHabitat: {pet_info['habitat'].title()}")
    print(f"\tDiet: {pet_info['dietary'].title()}")
    print(f"\tBody Covering: {pet_info['body covering'].title()}")