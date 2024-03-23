name: list[str] = ['a', 'b', 'c']
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name) if "__" not in i])
