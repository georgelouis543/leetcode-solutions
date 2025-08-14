input_string = "george"
count_vowels = 0

vowels = {"a", "e", "i", "o", "u"}

for i in input_string:
    if i in vowels:
        count_vowels += 1

print(count_vowels)