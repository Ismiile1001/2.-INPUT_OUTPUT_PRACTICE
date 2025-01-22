#   easy   and fezzy
badword = ["donkey", "bad"]

# must be read the line 
with open("file.txt", "r")as f:
    contain = f.read()

#replace  the bad word 

for word in badword:
    contain = contain.replace(word , "#" *len(word)) 


# writing the file again
with open( "file.txt", "w" ) as f:
    f.write(contain)           

