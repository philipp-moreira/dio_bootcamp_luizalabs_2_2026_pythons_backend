import sys

# Variables
base_text_introduction = "Entering a {0} to prompt: "
message_to_be_displayed_in_introduction = ""
default_data_splitter_on_prompt = " | "
default_data_type_separator = "=" * 160
default_data_type_sub_separator = "-" * 160
indentation_first_level = ""
indentation_second_level = "\t" * 1
indentation_third_level = "\t" * 2
indentation_fourth_level = "\t" * 3
start_index = 11
end_index = 14


# Method/function to easily the way to edit the message to be displayed
def update_message_to_be_displayed(
    new_text_slice,
    start_index=start_index,
    end_index=end_index,
    default_base_text=base_text_introduction,
) -> str:
    return (
        default_base_text[:start_index] + new_text_slice + default_base_text[end_index:]
    )


# Data Type 'Category': TEXT
# Code:

# Lesson learning: when trying to uses the 'sep' argument, to maintain the values split by comma,
# i learn which this argument, works just only is used with the first argument is a sequence/list/array/etc...
message_to_be_displayed_in_introduction = update_message_to_be_displayed("text type")
print(indentation_first_level + message_to_be_displayed_in_introduction)


print(default_data_type_separator)
# Data Type 'Category': NUMERIC

# Data Type 'Sub-Category': INT [INTEGER]
# Code:

# print('Write a int numeric number to prompt: ' + 1) # This will throw an error because we can not concatenate a string and an integer directly.

# Using this mode to write to the prompt avoids data casting/conversion at this time,
# in order to maintain focus on language types only.
message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "int numeric number"
)
print(indentation_first_level + message_to_be_displayed_in_introduction, end="")
print(1)

print(default_data_type_sub_separator)
# Data Type 'Sub-Category': FLOAT [FLOAT NUMBERS]
# Code:
message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "float numeric"
)
print(indentation_first_level + message_to_be_displayed_in_introduction, end="")
print(0.25, end=default_data_splitter_on_prompt)
print(12345.678910, end=default_data_splitter_on_prompt)
print((1.5 + 1.6))

print(default_data_type_sub_separator)
# Data Type 'Sub-Category': COMPLEX
# Code:
message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "complex numeric"
)
print(indentation_first_level + message_to_be_displayed_in_introduction, end="")
print(3 + 5j, end=default_data_splitter_on_prompt)
print(type(3 + 5j), end=default_data_splitter_on_prompt)
print(4 + 5j, end=default_data_splitter_on_prompt)
print(type(4 + 5j))


print(default_data_type_separator)
# Data Type 'Category': SEQUENCE

# Data Type 'Sub-Category': LIST
# Code
message_to_be_displayed_in_introduction = update_message_to_be_displayed("list type")
print(indentation_first_level + message_to_be_displayed_in_introduction, end="")
first_list = [1, 4, 9, 16, 25]
print(first_list, end=default_data_splitter_on_prompt)
print(type(first_list))

print(indentation_third_level + "|-> Using index resource with list (a sequence type)")
print(indentation_second_level + "|-> Getting index 3 :  ", end="")
print(first_list[3])
print(indentation_second_level + "|-> Taking de second-to-last item (-2):  ", end="")
print(first_list[-2])

# print(indentation_third_level + '|-> Taking de second-to-last item (-6):  ', end='')  # Error: IndexError
# print(first_list[-6], end=default_data_splitter_on_prompt))                                           # Error: IndexError

print(indentation_second_level + "|-> Using slice resource with list (a sequence type)")
print(indentation_second_level + "|-> Getting slice second to fourth :  ")
print(indentation_third_level + "|-> #1: list[1:3]", end=" ")
print(first_list[1:3])
print(indentation_third_level + "|-> #2: list[1:4]", end=" ")
print(first_list[1:4])
print(indentation_third_level + "|-> #3: list[1:5]", end=" ")
print(first_list[1:5])
print(indentation_third_level + "|-> #4: list[1:6]", end=" ")
print(first_list[1:6])

# Concatenate lists
second_list = [2, 8, 18, 32, 50]
print(indentation_second_level + "|-> Other stuffs with Lists")

print(indentation_second_level + "|-> Declaring and initialize lists:")
print(indentation_third_level + "|-> First list: \t\t\t", end="")
print(first_list)
print(indentation_third_level + "|-> Second list: \t\t\t", end="")
print(second_list)
second_list_with_duplicate_item = [1, 16, 2, 8, 18, 32, 50]
print(indentation_third_level + "|-> Second list with duplicate items: \t", end="")
print(second_list_with_duplicate_item)

print(indentation_second_level + "|-> 'Pasting' lists (concatenation):")
print(indentation_third_level + "|-> First_list + Second_ list: \t\t\t\t\t", end="")
print(first_list + second_list)
print(
    indentation_third_level
    + "|-> First_list + Second_ list_with_duplicate_items: \t\t",
    end="",
)
print(
    first_list + second_list_with_duplicate_item
)  # It only performed the concatenation operation, without applying any other action to the lists

# Changing an item in list
first_list[1] = 24
print(
    indentation_second_level
    + "|-> First list after changing (second item at index 1): \t\t",
    end="",
)
print(first_list)

# Append an item to the list
second_list.append("new item")
print(
    indentation_second_level
    + "|-> Second list after appending a new item, using append() method:\t",
    end="",
)
print(second_list)

second_list = second_list + ["another new item"]
print(
    indentation_second_level
    + "|-> Second list after appending again a new item, but now, using list concatenate resource: \t\t",
    end="",
)
print(second_list)

print(
    indentation_second_level
    + "|-> Watching behavior in lists, when work with variables.: \t"
)
# On work wit lists and variables, i need to watch, because, on to assign a list define in a variable to another variable, that second variable will to have a reference to the first one.
# This means that if you make changes to the second variable, those changes will be reflected in the first variable.
three_first_letters_alphabet = ["a", "b", "c"]
three_first_letters_alphabet_copy = three_first_letters_alphabet

print(
    indentation_third_level + '|-> List "three_first_letters_alphabet´: \t\t\t\t ',
    end="",
)
print(three_first_letters_alphabet)

print(
    indentation_third_level + '|-> List "three_first_letters_alphabet_copy´: \t\t\t\t ',
    end="",
)
print(three_first_letters_alphabet_copy)

# This is the same or has a same behavior the next line
# three_first_letters_alphabet_copy += ['d', 'e']
three_first_letters_alphabet_copy = three_first_letters_alphabet_copy + ["d", "e"]

print(
    indentation_third_level
    + '|-> List "three_first_letters_alphabet again´: \t\t\t\t ',
    end="",
)
print(three_first_letters_alphabet)

print(
    indentation_third_level
    + '|-> List "three_first_letters_alphabet_copy after change just only to it´: ',
    end="",
)
print(three_first_letters_alphabet_copy)

print(default_data_type_sub_separator)
# Data Type 'Sub-Category': TUPLE
# Code:

message_to_be_displayed_in_introduction = update_message_to_be_displayed("tuple type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

first_tuple = 1, 2, 3, 4, "5"
print(indentation_second_level + "|-> first_tuple:\t ", end="")
print(first_tuple)

second_tuple = 6, 7, 8, 9, 10
print(indentation_second_level + "|-> second_tuple:\t ", end="")
print(second_tuple)

# first_tuple[4] = 5    #This action will throw a error (''tuple" object does not support item assignment")
# print(indentation_second_level + '\-> Try alter a item in first_tuple: ', end='')
# print(first_tuple)

print(indentation_second_level + "|-> Nesting tuples: \t ", end="")
nested_tuple = "a", "b", first_tuple
print(nested_tuple)

pasting_tuples = first_tuple + second_tuple
print(
    indentation_third_level + "|-> Pasting tuples (first_tuple + second_tuple):\t ",
    end="",
)
print(pasting_tuples)


second_tuple_with_duplicate_item_from_first = 4, "5", 6, 7, 8, 9, 10
pasting_tuple_with_duplicate_items = (
    first_tuple + second_tuple_with_duplicate_item_from_first
)
print(
    indentation_third_level
    + "|-> Pasting tuples (first_tuple + second_tuple_with_duplicate_item_from_first):\t ",
    end="",
)
print(pasting_tuple_with_duplicate_items)
# When a specific item was retrieved from a given index, a type conversion occurred, during which the value was written to the prompt.
print(
    indentation_third_level
    + "|-> Accessing a specific element by index (first_tuple[4])):\t ",
    end="",
)
print(first_tuple[4])
print(
    indentation_third_level
    + "|-> Accessing a specific element by index (first_tuple[-1])):\t ",
    end="",
)
print(first_tuple[-1])
# print(
#     indentation_third_level
#     + "|-> Accessing a specific element by index (first_tuple['5'])):\t ",
#     end='',
# )
# print(first_tuple['5']) # This action will throw a error (TypeError: tuple indices must be integers or slices, not str)

print(indentation_second_level + "|-> Tuple with mutable objects: \t ", end="")
first_list_numbers = [0, 9, 8]
second_list_numbers = [7, 6, 5]
third_list_numbers = [1, -1, +1]

tuple_with_mutable_objects = (first_list_numbers, second_list_numbers)
print(tuple_with_mutable_objects)
# tuple_with_mutable_objects[0] = third_list_numbers  This action will throw a error ("TypeError: "tuple" object does not support item assignment")
# print(tuple_with_mutable_objects)

tuple_with_mutable_objects[0][1] = tuple_with_mutable_objects[0][1] ** 2
print(
    indentation_third_level
    + """|-> Not changing the element ('first_list_numbers')  at index (0) of the tuple, 
                    but changing the element (1 -> '9') of item (0) of the tuple:
                \'tuple_with_mutable_objects[0][1] = tuple_with_mutable_objects[0][1] ** 2\' ==> \t """,
    end="",
)
print(tuple_with_mutable_objects)

empty_tuple = ()
print(indentation_second_level + '|-> Tuple no elements "empty_tuple" \t ', end="")
print(empty_tuple)

tuple_with_only_one_element = (first_tuple,)
print(
    indentation_second_level
    + '|-> Tuple unless one element  "tuple_with_only_one_element" \t ',
    end="",
)
print(tuple_with_only_one_element)
print(
    indentation_second_level + "|-> Length (tuple_with_only_one_element):\t\t ", end=""
)
print(
    len(tuple_with_only_one_element)
)  # Has just one element, because, i"m using nested tuple

# first_index, second_index, third_index = first_tuple  # This action will throw a error ("ValueError: not enough values to unpack (expected 6, got 5)")
# (
#     first_index,
#     second_index,
#     third_index,
#     fourth_index,
#     fifth_index,
#     element_not_existent,
# ) = first_tuple                                       # This action will throw a error ("ValueError: not enough values to unpack (expected 6, got 5)")
first_index, second_index, third_index, fourth_index, fifth_index = first_tuple
print(
    indentation_second_level
    + '|-> Using unpacking to access values from tuple "first_tuple":\t '
)
print(indentation_third_level + '|-> "first_index"\t=\t', end="")
print(first_index)
print(indentation_third_level + '|-> "second_index"\t=\t', end="")
print(second_index)
print(indentation_third_level + '|-> "third_index"\t=\t', end="")
print(third_index)

print(default_data_type_sub_separator)
# Data Type 'Sub-Category': RANGE
# Code:
first_range = range(1, 10, 1)
message_to_be_displayed_in_introduction = update_message_to_be_displayed("range type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

print(indentation_second_level + "|-> first_range:\t :", end="")
print(first_range)

# first_list_length = len(first_list)
# second_range = range((first_list_length - 1))
# print(indentation_second_level + '|-> second_range:\t :', end='')
# print(second_range)
# print(indentation_second_level + '|-> The "first_list"length is:\t: ', end='')
# print(first_list_length)
# print(second_range.index(0), end='')  # Write to prompt 0, because, the first item of the range is 0, and the index of the first item is 0
# print(second_range.index(1), end='')  # Write to prompt 1, because, the second item of the range is 1, and the index of the second item is 1
# print(second_range.index(2), end='')  # Write to prompt 2, because, the third item of the range is 2, and the index of the third item is 2
# print(second_range.index(3), end='') # Write to prompt 3, because, the fourth item of the range is 3, and the index of the fourth item is 3
# print(second_range[4], end='')            # An error occurs because the `range` type is just a data type that has indices, or indexers; it doesn't have a reference to values ​​themselves.
# print(5 in second_range) # False
# print(3 in second_range) # True
# print(9 in second_range) # False

first_list_length = len(first_list)
# second_range = range(first_list_length)
# second_range = range(0, first_list_length, 1)
# second_range = range(0, 100, 2)
second_range = range(first_list_length)

print(indentation_second_level + "|-> second_range:\t :", end="")
print(second_range)

# Range"s features supported: CONTAINMENT TESTS - "0 in second_range"
print(indentation_third_level + "|-> Index 0 exists in second_range? -->:\t :", end="")
print(0 in second_range)
print(indentation_third_level + "|-> Index 1 exists in second_range? -->:\t :", end="")
print(1 in second_range)
print(indentation_third_level + "|-> Index 2 exists in second_range? -->:\t :", end="")
print(2 in second_range)
print(indentation_third_level + "|-> Index 3 exists in second_range? -->:\t :", end="")
print(3 in second_range)
print(indentation_third_level + "|-> Index 4 exists in second_range? -->:\t :", end="")
print(4 in second_range)
print(indentation_third_level + "|-> Index 5 exists in second_range? -->:\t :", end="")
print(5 in second_range)
# The `stop` argument in the `range` constructor is a unique limit, meaning that it will not be considered at the end of the range.

# Range"s features supported: ELEMENT INDEX LOOKUP
print(
    indentation_third_level
    + '|-> Range"s features supported: ELEMENT INDEX LOOKUP #1 --> "second_range.index(4)":\t ',
    end="",
)
# "range.index()" searches for the value in the range and returns the index that contains the value.
print(second_range.index(4))
# print(
#     indentation_third_level
#     + '|-> Range"s features supported: ELEMENT INDEX LOOKUP #1 --> "second_range.index(5)'':\t :',
#     end='',
# )
# print(second_range.index(5)) # An error occurs ("ValueError: range.index(x): x not in range")

# Accessing the index and return the value
print(
    indentation_third_level
    + '|-> Range"s features supported: ELEMENT INDEX LOOKUP #2 --> "second_range[4]":\t ',
    end="",
)
print(second_range[4])
# print(
#     indentation_third_level
#     + '|-> Range"s features supported: ELEMENT INDEX LOOKUP #2 --> "second_range[5]'':\t :',
#     end='',
# )
# print(second_range[5]) # An error occurs ("IndexError: range object index out of range")

# Range"s features supported: SLICING AND SUPPORT FOR NEGATIVE INDICES
print(
    indentation_third_level
    + '|-> Range"s features supported: SLICING AND SUPPORT FOR NEGATIVE INDICES #1 --> "second_range[:3]":\t ',
    end="",
)
print(second_range[:3])

print(
    indentation_third_level
    + '|-> Range"s features supported: SLICING AND SUPPORT FOR NEGATIVE INDICES #1 --> "second_range[-3]":\t ',
    end="",
)
print(second_range[-3])

print(indentation_second_level + '|-> The "first_list"length is:\t: ', end="")
print(first_list_length)

# # An error occurs()"TypeError: unsupported operand type(s) for +: "range" and "range'')
# concatenate_range = first_range + second_range
# print(concatenate_range[0])

print(default_data_type_separator)
# Data Type 'Category': MAP OR DICTIONARY
# Data Type 'Sub-Category': DICT
# Code:

message_to_be_displayed_in_introduction = update_message_to_be_displayed("dict type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

empty_dictionary = {}
print(
    indentation_second_level
    + "|-> Declaring and initializing a empty dict:\t\t\t\t\t\t\t\t\t\t\t",
    end="",
)
print(empty_dictionary)

first_dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(
    indentation_second_level
    + "|-> Declaring and initializing a dict with some key-value pairs:\t\t\t\t\t\t\t\t",
    end="",
)
print(first_dictionary)

print(
    indentation_second_level
    + '|-> Accessing a specific element in "first_dictionary" -> "first_dictionary[\'key3\']":\t\t\t\t\t\t',
    end="",
)
print(first_dictionary["key3"])

# In a accessing action to the value by an inexistent key, an error occurs ("KeyError: "key4'')
# But in a action to assigning  a value to an inexistent key, the new key is created and the value is assigned to it, without any error.

# print(
#     indentation_second_level
#     + '|-> Accessing a inexistent  element in "first_dictionary" -> "first_dictionary[\'key4\']":\t',
#     end='',
# )
# print(first_dictionary['key4']) # An error occurs ("KeyError: "key4'')

print(
    indentation_second_level
    + '|-> Attempting to access a non-existent element in "first_dictionary" using the method "get()"->"first_dictionary.get(\'key6\')":\t',
    end="",
)
print(first_dictionary.get("key6"))

first_dictionary["key4"] = "Value4"
print(
    indentation_second_level
    + '|-> Assigning a new value to the dictionary  "first-dictionary" and a non-existent key "key4":\t\t\t\t\t',
    end="",
)
print(first_dictionary)

del first_dictionary["key3"]
print(
    indentation_second_level
    + '|-> Deleting a key-value pair from the dictionary  "first-dictionary" -> "del first_dictionary[\'key3\']":\t\t\t',
    end="",
)
print(first_dictionary)

first_dictionary["key4"] = "Value5"
print(
    indentation_second_level
    + "|-> Changing the value of an existing key in the dictionary  \"first-dictionary\" -> \"first_dictionary['key4'] = 'Value5'\":\t",
    end="",
)
print(first_dictionary)

print(
    indentation_second_level
    + '|-> Checking if a key exists in the dictionary  "first-dictionary" -> "\'key7\' in first_dictionary":\t\t\t\t',
    end="",
)
print("key7" in first_dictionary)

list_keys_from_dictionary = list(first_dictionary)
print(
    indentation_second_level
    + '|-> Converting the dictionary keys to a list -> "list(first_dictionary)":\t\t\t\t\t\t\t',
    end="",
)
print(list_keys_from_dictionary)

unordered_list_keys_from_dictionary = list(first_dictionary)
print(
    indentation_second_level
    + '|-> Converting the dictionary keys to an unordered list -> "list(first_dictionary)":\t\t\t\t\t\t',
    end="",
)
print(unordered_list_keys_from_dictionary)

print(default_data_type_separator)
# Data Type 'Category': COLLECTION

# Data Type 'Sub-Category': SET
# Code:

message_to_be_displayed_in_introduction = update_message_to_be_displayed("set type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

empty_set = (
    set()
)  # Using the '{ }' notation results in a dictionary, not an empty set as I expected.
print(
    indentation_second_level
    + "|-> Declaring and initializing a empty set:\t\t\t\t\t\t",
    end="",
)
print(empty_set)

first_set = {"element1", "element2", "element3", "element4", "element1", "element3"}
print(
    indentation_second_level
    + "|-> Declaring and initializing a set with some elements (with duplicates):\t\t",
    end="",
)
print(first_set)

list_to_set = ["element1", "element2", "element3", "element4", "element1", "element3"]
print(
    indentation_second_level + "|-> list to use in the set:\t\t\t\t\t\t\t\t",
    end="",
)
print(list_to_set)

second_set = set(list_to_set)
print(
    indentation_second_level
    + "|-> Declaring and initializing a set with some elements (with duplicates) from a list:\t",
    end="",
)
print(second_set)

# Membership testing
print(
    indentation_second_level
    + '|-> Membership testing: "element3" in second_set --> "\'element3\' in second_set)":\t',
    end="",
)
print("element3" in second_set)

print(
    indentation_second_level
    + '|-> Membership testing: "element5" in second_set --> "\'element5\' in second_set)":\t',
    end="",
)
print("element5" in second_set)

# Set data type supports mathematical operations like union, intersection, difference and symmetric difference

set_alphabet_vowels = set("aeiou")
# set_alphabet_vowels = set("aeiou")

set_alphabet_consonants = set("bcdfg")
# set_alphabet_consonants = set("bcdfg")

set_alphabet_vowels_and_consonants = set("aiubcdfg")
# set_alphabet_vowels_and_consonants = set("aiubcdfg")


print(indentation_third_level + "|-> My sets to mathematical operations:\t")

print(indentation_third_level + "|-> " + str(set_alphabet_vowels))
print(indentation_third_level + "|-> " + str(set_alphabet_consonants))
print(indentation_third_level + "|-> " + str(set_alphabet_vowels_and_consonants))

# Union
print(
    indentation_fourth_level
    + '|-> Set Mathematical operations [Union] \t\t"set_alphabet_vowels | set_alphabet_vowels_and_consonants":\t',
    end="",
)
print(set_alphabet_vowels | set_alphabet_vowels_and_consonants)

# Intersection
print(
    indentation_fourth_level
    + '|-> Set Mathematical operations [Intersection] \t\t"set_alphabet_vowels & set_alphabet_vowels_and_consonants":\t',
    end="",
)
print(set_alphabet_vowels & set_alphabet_vowels_and_consonants)

# Difference
print(
    indentation_fourth_level
    + '|-> Set Mathematical operations [Difference] \t\t"set_alphabet_vowels - set_alphabet_vowels_and_consonants":\t',
    end="",
)
print(set_alphabet_vowels - set_alphabet_vowels_and_consonants)

# Symmetric difference
print(
    indentation_fourth_level
    + '|-> Set Mathematical operations [Symmetric difference] \t"set_alphabet_vowels ^ set_alphabet_vowels_and_consonants":\t',
    end="",
)
print(set_alphabet_vowels ^ set_alphabet_vowels_and_consonants)

print(default_data_type_sub_separator)
# print(default_data_type_sub_separator)
# Data Type 'Sub-Category': FROZENSET
# Code:

message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "frozenset data type"
)
print(indentation_first_level + message_to_be_displayed_in_introduction)

first_frozenset = frozenset("abcde")
print(
    indentation_second_level
    + "|-> Declaring and initializing a frozenset with some elements:\t\t\t\t",
    end="",
)
print(first_frozenset)

# first_frozenset.add("b") # This action will throw a error ("AttributeError: 'frozenset' object has no attribute 'add'"), because, the frozenset is an immutable data type, so, it does not have the method "add()"

second_frozenset_vowels = frozenset("aeiou")
third_frozenset_consonants = frozenset("bcdfg")
fourth_frozenset_vowels_and_consonants = frozenset("eiodf")

print(indentation_third_level + "|-> My frozensets to mathematical operations:\t")

print(indentation_third_level + "|-> " + str(second_frozenset_vowels))
print(indentation_third_level + "|-> " + str(third_frozenset_consonants))
print(indentation_third_level + "|-> " + str(fourth_frozenset_vowels_and_consonants))


# Union
print(
    indentation_fourth_level
    + '|-> Frozenset Mathematical operations [Union] \t\t\t"second_frozenset_vowels | third_frozenset_consonants":\t\t\t',
    end="",
)
print(second_frozenset_vowels | third_frozenset_consonants)

# Intersection
print(
    indentation_fourth_level
    + '|-> Frozenset Mathematical operations [Intersection] \t\t"second_frozenset_vowels & fourth_frozenset_vowels_and_consonants":\t',
    end="",
)
print(second_frozenset_vowels & fourth_frozenset_vowels_and_consonants)

# Difference
print(
    indentation_fourth_level
    + '|-> Frozenset Mathematical operations [Difference] \t\t"first_frozenset - fourth_frozenset_vowels_and_consonants":\t\t',
    end="",
)
print(first_frozenset - fourth_frozenset_vowels_and_consonants)

# Symmetric difference
print(
    indentation_fourth_level
    + '|-> Frozenset Mathematical operations [Symmetric Difference] \t"first_frozenset ^ fourth_frozenset_vowels_and_consonants":\t\t',
    end="",
)
print(first_frozenset ^ fourth_frozenset_vowels_and_consonants)

print(default_data_type_separator)
# print(default_data_type_separator)
# Data Type 'Category': BOOLEAN
# Code:

message_to_be_displayed_in_introduction = update_message_to_be_displayed("boolean type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

my_var_boolean_true = True
my_var_boolean_false = False

print(
    indentation_second_level
    + "|-> Boolean variable with value True 'my_var_boolean_true':\t ",
    end="",
)
print(my_var_boolean_true)

print(
    indentation_second_level
    + "|-> Boolean variable with value False 'my_var_boolean_false':\t ",
    end="",
)
print(my_var_boolean_false)

print(indentation_second_level + "TRUE")

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_true == 1':\t\t ",
    end="",
)
print(my_var_boolean_true == 1)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_true == bool(1)':\t ",
    end="",
)
print(my_var_boolean_true == bool(1))

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_true == 2':\t\t ",
    end="",
)
print(my_var_boolean_true == 2)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_true == bool(2)':\t ",
    end="",
)
print(my_var_boolean_true == bool(2))

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_true == 1000':\t ",
    end="",
)
print(my_var_boolean_true == 1000)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_true == bool(1000)':\t ",
    end="",
)
print(my_var_boolean_true == bool(1000))


print(indentation_second_level + "FALSE")

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_false  == 0':\t\t ",
    end="",
)
print(my_var_boolean_false == 0)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_false == bool(0)':\t ",
    end="",
)
print(my_var_boolean_false == bool(0))

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_false == 1':\t\t ",
    end="",
)
print(my_var_boolean_false == 1)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_false == bool(1)':\t ",
    end="",
)
print(my_var_boolean_false == bool(1))

print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (directly) values 'my_var_boolean_false == 1000':\t ",
    end="",
)
print(my_var_boolean_false == 1000)
print(
    indentation_second_level
    + "|-> Comparison of boolean variable with integer (with cast) values 'my_var_boolean_false == bool(1000)':",
    end="",
)
print(my_var_boolean_false == bool(1000))


print(default_data_type_separator)
# Data Type 'Category': BINARY
# Code:

# Data Type 'Sub-Category': BYTES
# Code:
message_to_be_displayed_in_introduction = update_message_to_be_displayed("bytes type")
print(indentation_first_level + message_to_be_displayed_in_introduction)

my_var_bytes_using_prefix = b"some phrase"
print(
    indentation_second_level
    + "|-> Declaring and initializing a bytes variable with 'my_var_bytes_using_prefix = b\"some phrase\"':\t\t\t\t ",
    end="",
)
print(my_var_bytes_using_prefix)

print(
    indentation_third_level + "|-> Representation ways: ",
)
print(
    indentation_fourth_level + "|-> Raw/Default:\t ",
    end="",
)
print(my_var_bytes_using_prefix)

print(
    indentation_fourth_level + "|-> Hexadecimal:\t ",
    end="",
)
print(my_var_bytes_using_prefix.hex(" "))

print(
    indentation_fourth_level + "|-> List of Integers:\t ",
    end="",
)
print(list(my_var_bytes_using_prefix))

print(
    indentation_third_level + "|-> Measure ways: ",
)

print(
    indentation_fourth_level
    + "|-> Using function 'len()' ==> 'len(my_var_bytes_using_prefix)':\t ",
    end="",
)
print(len(my_var_bytes_using_prefix))

print(
    indentation_fourth_level
    + "|-> Using function 'sys.getsizeof(my_var_bytes_using_prefix)':\t\t ",
    end="",
)
print(sys.getsizeof(my_var_bytes_using_prefix))

print(
    indentation_fourth_level
    + "|-> Representations to "
    + str(my_var_bytes_using_prefix[0])
    + "/"
    + chr(int(my_var_bytes_using_prefix[0]))
    + "==> 'f\"{my_var_bytes_using_prefix[0]:08b}\"':\t ",
    end="",
)
print(f"{my_var_bytes_using_prefix[0]:08b}")

print(
    "\t"
    + indentation_fourth_level
    + "|-> Using 'my_var_bytes_using_prefix[0].get_bit_length()':\t\t ",
    end="",
)
print(my_var_bytes_using_prefix[0].bit_length())

print(
    "\t"
    + indentation_fourth_level
    + "|-> Using 'my_var_bytes_using_prefix[0].bit_count()':\t\t\t ",
    end="",
)
print(my_var_bytes_using_prefix[0].bit_count())


my_var_bytes_using_constructor = bytes("some phrase", "utf-8-sig")  # utf-8-bom
print(
    indentation_second_level
    + '|-> Declaring and initializing a bytes variable with \'my_var_bytes_using_constructor = bytes("some phrase", "utf-8-sig") \':\t ',
    end="",
)
print(my_var_bytes_using_constructor)

print(
    indentation_third_level
    + "|-> Apply decoding to  my_var_bytes_using_constructor => 'my_var_bytes_using_constructor.decode('utf-8-sig')':\t\t ",
    end="",
)
print(my_var_bytes_using_constructor.decode("utf-8-sig"))

my_var_bytes_using_constructor_2 = bytes("some phrase", "utf-8")
print(
    indentation_second_level
    + '|-> Declaring and initializing a bytes variable with \'my_var_bytes_using_constructor_2 = bytes("some phrase", "utf-8")\':\t ',
    end="",
)
print(my_var_bytes_using_constructor_2)


print(default_data_type_sub_separator)
# Data Type 'Sub-Category': BYTEARRAY
# Code:
message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "bytearray type"
)
print(indentation_first_level + message_to_be_displayed_in_introduction)

# Creating an empty instance
empty_bytearray = bytearray()
print(
    indentation_second_level
    + "|-> Declaring and initializing a empty bytearray:\t\t\t\t\t\t",
    end="",
)
print(empty_bytearray)

# Creating a zero-filled instance with a given length
empty_bytearray_with_given_length = bytearray(10)
print(
    indentation_second_level
    + "|-> Declaring and initializing a empty bytearray with a given length (10):\t\t\t",
    end="",
)
print(empty_bytearray_with_given_length)

my_iterable_range = range(12)
print(
    indentation_second_level + "|-> The iterable (range(12)):\t\t\t\t\t\t\t\t\t",
    end="",
)
print(my_iterable_range)

byte_array_from_iterable = bytearray(my_iterable_range)
print(
    indentation_second_level
    + "|-> Declaring and initializing a bytearray from an iterable (range(12)):\t\t\t",
    end="",
)
print(byte_array_from_iterable)


print(default_data_type_sub_separator)
# Data Type 'Sub-Category': MEMORYVIEW
# Code:
message_to_be_displayed_in_introduction = update_message_to_be_displayed(
    "memoryview type"
)
print(indentation_first_level + message_to_be_displayed_in_introduction)

empty_memoryview = memoryview(my_var_bytes_using_prefix)
print(
    indentation_second_level
    + "|-> Declaring and initializing a memoryview from a bytes variable (my_var_bytes_using_prefix),  the memory position is :\t\t",
    end="",
)
print(empty_memoryview)

