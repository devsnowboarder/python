import operator

original_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

sorted_x = sorted(original_dict.items(), key=operator.itemgetter(1))
print(sorted_x)

sorted_x.reverse()
print(sorted_x)