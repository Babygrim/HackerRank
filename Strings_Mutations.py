def mutate_string(string, position, character):
    modified = list(string)
    modified[position] = character
    return ''.join(modified)
print(mutate_string("abracadabra", 5, "k"))