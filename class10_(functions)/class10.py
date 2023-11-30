

def my_function(a: int, b: int, *abc: int, **xyz: int):
    print(a, b, abc, xyz)


my_function(1, 2, 7, 8, 9, 7, 6, 5, 6, 7, 8, c=20, x=100)
