dati=[]
##1.uzd
with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")

        if row[4] == "Oman":
            dati.append(row[6])
print(min(dati))
##2.uzd
dati1 = []
with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")

        if row[4] == "Latvia":
            dati1.append(row[0])
print(len(dati1))
##3.uzd
dati2 = []
with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")

        if row[4] == "Latvia" and row[7] == "Telecommunications":
            dati2.append(row[0])
print(len(dati2))
##4.uzd
dati3 = []
with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        x = row[3].startswith("https://")

        if row[4] == "Latvia" and x == True:
            dati3.append(row[0])
print(len(dati3))
##5.uzd
dati4 = []
with open("data.txt","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        y = row[3].endswith(".org/")

        if row[4] == "Latvia" and y == True:
            dati4.append(row[0])
print(len(dati4))