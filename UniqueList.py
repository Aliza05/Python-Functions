def unique_list(user_list):
    new_unique_list = []
    for item in user_list:
        if item not in new_unique_list:
            new_unique_list.append(item)
    return new_unique_list


integer_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(integer_list))
