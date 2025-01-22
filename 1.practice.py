f = open("file.txt")
conta = f.read()
# condition 
if "daddy" in conta:
    s = "daddy"
    print( f" find {s} in file ")

else :
    print(" dont find it in file ")

f.close()

