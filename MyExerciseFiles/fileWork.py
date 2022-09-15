##Open file to work with


fl = open('inputFile.txt', 'r')

##File reading and selecting. Ennumerate resoulting list

#counter = 1
#for line in fl:
#    line_split = line.split()
#    if line_split[2] == 'P':
#        print(str(counter) + '-' + line )
#        counter+=1

#fl.close()

##Write files.

passFile= open('PassFile.txt', 'w')
failFile = open('FailFile.txt', 'w')
for line in fl:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

fl.close()
passFile.close()
failFile.close()