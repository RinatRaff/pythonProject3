import operator
dict_with_files = {}

list_files = ['1.txt', '2.txt', '3.txt']

for i in list_files:
    with open(i, 'r', encoding='utf-8') as f:
        list_lines = f.readlines()
        dict_with_files[len(list_lines)] = "\n".join(list_lines)
list_with_files = sorted(dict_with_files.items(), key=operator.itemgetter(1))
sorted_dict_with_files = dict(list_with_files)
with open(i, 'r', encoding='utf-8') as f:
    print(dict_with_files)