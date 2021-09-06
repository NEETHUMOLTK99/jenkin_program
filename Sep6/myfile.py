#writing name to file


name = input("Enter your name: ")
fd = open("name.txt", "w")
fd.write(name)
fd.close()
