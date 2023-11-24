import sys
print("line1")
print("line2")
print("line3")
print(type(sys.argv))  # iterative data type
print(sys.argv)  # iterative data type
if sys.argv[1] == '-g':
    print("I will install this package on globally in your system!")
