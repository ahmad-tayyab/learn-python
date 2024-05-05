name: list[str] = ['a', 'b', 'c']
print(name)  # print
print(type(name))  # type
print(id(name))  # physical address
print([i for i in dir(name) if "__" not in i])
