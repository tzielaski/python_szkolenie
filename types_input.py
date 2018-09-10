user_name = input("Give me your name: ")
my_name = f"'''My name \"{user_name}\".\n\tI'm an \"\"\"astronaut!\"\"\"'''"
my_name_no_spaces = my_name.replace(' ', '_')
my_name_no_tabs = my_name_no_spaces.replace('\t', '_')
print(my_name_no_tabs)
