def sort_by_mark(my_class):
    return sorted(my_class, reverse=True)
print(sort_by_mark([[6, 'Alan'], [37, 'Shannon']]))


def sort_by_name(my_class):
        return sorted(my_class, key=lambda myclass: myclass[1]
        )
print(sort_by_name([[6, 'Alan'], [37, 'Shannon']]))


# Uncomment the following lines as needed
# if you want to test your implementation a bit:

# my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

# print(sort_by_mark(my_class))
# print(sort_by_name(my_class))
