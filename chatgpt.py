# List (리스트)
my_list = [1, 2, 3, 4, 5]

# Tuple (튜플)
my_tuple = (1, 2, 3, 4, 5)

# Dictionary (사전)
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}

# Set (집합)
my_set = {1, 2, 3, 4, 5}

# List의 예제
print("List:")
print("Length:", len(my_list))
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slicing:", my_list[1:4])
print("Appending 6:", my_list + [6])

# Tuple의 예제
print("\nTuple:")
print("Length:", len(my_tuple))
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slicing:", my_tuple[1:4])

# Dictionary의 예제
print("\nDictionary:")
print("Length:", len(my_dict))
print("Value associated with 'apple':", my_dict['apple'])
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())

# Set의 예제
print("\nSet:")
print("Length:", len(my_set))
print("Adding 6:", my_set.add(6))
print("Removing 3:", my_set.remove(3))

# Set 연산 (합집합, 교집합, 차집합)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
