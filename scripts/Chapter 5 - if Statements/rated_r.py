from platform import processor

age = 66
if age < 18:
    price = 'not applicable'
#    print("You are not old enough to see this movie without a parent or guardian.")
elif age >= 18 and age < 65:
    price = '$10'
elif age >= 60:
    price = '$8'
#    print("You qualify for senior discount, the price is $8.")
else:
    price = '$12'
print(f"Your admission cost is {price}")
#    print("You are old enough to see this movie and the price is $12.")
