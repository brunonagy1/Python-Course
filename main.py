with open("file.txt","a") as f:
    for line in ["AAAAAA","BBBBBBB","CCCCCCCCC"]:
        print(line,file=f)

with open("file.txt","r") as f:
    for line in f:
        print(line)