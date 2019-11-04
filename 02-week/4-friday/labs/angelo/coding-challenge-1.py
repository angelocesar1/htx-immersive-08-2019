# Using a function check the list for duplicate names. Create a new list by removing the duplicates.
names = ['Alex', 'John', 'Mary', 'Steve', 'John', 'Steve']
new_names = []
def remove_duplicates(names):
    for duplicates in names:
        if duplicates not in new_names:
            new_names.append(duplicates)
    return new_names

print(remove_duplicates(names))