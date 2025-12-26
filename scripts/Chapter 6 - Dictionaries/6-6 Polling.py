# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
names = (
    'jen',
    'paul',
    'melanie',
    'sarah',
    'edward',
    'phil',
    'jake'
)

for name in favorite_languages:
    language = favorite_languages[name]
    print(f"Hello, {name.title()}, your favorite language is {language.title()}.")

print()

for name in names:
    if name not in favorite_languages:
        print(f"{name.title()}, please take our poll.")