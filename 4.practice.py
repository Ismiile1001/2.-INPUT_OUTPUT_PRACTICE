
#  replace a word  by  (####)  


word = "kona"

with open( "file.txt", "r" ) as f: 
    
    contain = f.read()

containnew = contain.replace( word ,"####")

with open( "file.txt", "w" ) as f:
     f.write(containnew)