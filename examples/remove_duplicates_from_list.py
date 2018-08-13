def Remove(duplicates):
    final_list = []
    for i in duplicates:
        if i not in final_list:
            final_list.append(i)
    return final_list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
