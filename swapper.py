def swappingFile():
    f1 = input("Enter The Original File: ")
    f2 = input("Enter The File To Be Swapped: ")

    with open(f1, 'r') as a:
        data_1 = a.read()
    with open(f2, 'r') as b:
        data_2 = b.read()

    
    with open(f1, 'w') as a:
        a.write(data_2)
    with open(f2, 'w') as b:
        b.write(data_1)

swappingFile()