a_dictionary = {
    'a': 123,
    'b': 321,
    'c': 345,
}
max = 0
name = ""
for num in a_dictionary:
    name = num
    if a_dictionary[num] > max:
        max = a_dictionary[num]
print(f"Max: {max} by {name}")