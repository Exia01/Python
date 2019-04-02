# min_max_key_in_dictionary
# Write a function called min_max_key_in_dictionary which returns a list with the lowest key in the dictionary and the highest key in the
# dictionary. You can assume that the dictionary will have keys that are numbers.


def min_max_key_in_dictionary(dictionary):
    temp_generator = list((val for val in dictionary.keys()))
    temp_min, temp_max = min(temp_generator), max(temp_generator)
    results = [temp_min, temp_max]
    return results


# Test Cases
print(min_max_key_in_dictionary(
    {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))  # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"}))  # [1,4]
