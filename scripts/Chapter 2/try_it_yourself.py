from tabnanny import filename_only

name = "eric"
name_title = name.title()
message=(f"Hello {name_title}, would you like to learn some Python today?")

famous_person = " albert einstein"
quote = '"A person who never made a mistake never tried anything"'
famous_quote = f"{famous_person.title().lstrip()} once said: \n{quote}"

filename = "python_notes.txt"
filename_no_ext = filename.removesuffix('.txt')

print(famous_quote)

print(filename_no_ext)