a = "  salut ca va ?\n hey  "

print([i.rstrip().lstrip() for i in a.split("\n")])

print(a.split())
