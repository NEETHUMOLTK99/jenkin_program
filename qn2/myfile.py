#writing name to file


name = "Neethu"
fd = open("name.txt", "w")
fd.write(name)
fd.close()
