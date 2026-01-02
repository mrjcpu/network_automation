# create a function that defines the shirts text and size
def make_shirt(text, size="Large"):
    """Make a shirt"""
    print(f"I would like a shirt that says '{text.capitalize()}' in size {size}.")

# variables used for text/size
make_shirt(text="life's a bitch!")
make_shirt(text="life's a bitch!", size="Medium")
make_shirt(text="word to yo mutha", size="XXXL")