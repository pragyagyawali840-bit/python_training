with open("writenote.txt","w") as f:
    f.write("This is text")

with open("writenote.txt", "r") as f:
    content = f.read()
    print(content)