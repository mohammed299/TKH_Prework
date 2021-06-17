name_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

longest_name = ""
for name in name_list:
    if len(name) > len(longest_name):
        longest_name = name
    else:
        pass
print(longest_name)