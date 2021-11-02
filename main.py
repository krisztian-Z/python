import string
fn=input("What is your first name?\n")
ln=input("What is your surname?\n")
fncount=0
lncount=0
for i in fn:
    if i in string.ascii_letters:
        fncount+=1
for i in ln:
    if i in string.ascii_letters:
        lncount+=1
print("Your first name has " + str(fncount) + " letters, and your surname has " + str(lncount) + " letters.")