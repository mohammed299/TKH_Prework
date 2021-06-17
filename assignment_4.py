def largest_name(names):
  longest_name = ""
  for name in names:
    if len(name) > len(longest_name):
        longest_name = name
    else:
        pass
  print(longest_name)

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

largest_name(names_list)
