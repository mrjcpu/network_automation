# 6-3 & 6-4 Glossary
programming_words = {
    'string': 'Words not numbers',#    'digit': 'Numbers not works',
    'loop': 'Cycle through a list for values',
    'list': 'Values kept in a location to be referenced',
    'variables': 'Data that may change',
    'dictionary': 'A collection of keys with values defining them',
    'key': 'Item title within a dictionary',
    'value': 'Item defining a key'
}
#for key, value in programming_words.items():
    print(f"{key.title()}: {value}\n")

for word, definition in programming_words.items():
    print(f"{word.title()}: {definition}")