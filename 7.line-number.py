with open("file.txt")as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "python" in line:
        print(f"the line is present in line no : {lineno}")  
        break
    lineno += 1
else: 
    print( "the line is not present in lines")    