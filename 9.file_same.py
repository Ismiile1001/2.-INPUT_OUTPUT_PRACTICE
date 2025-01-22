#  identifier the file are same or not  

with open("file.txt")as f: 
    contain1 = f.read()
with open("kona.txt")as f: 
    contain = f.read()
if contain1 == contain:
    print( "the file have the same contents")
else:
    print( "the file have the same not same contents")