def run_diary_exercise():
    with open("diary.txt" , "w") as f:
        f .write("Day 1:Started Python learning.\n")
        f .write("Day 2:Mastered list sequences.\n")
        f .write("Day 3:Exploring safe File I/O.\n")
       
       
    try:
               with open("diary.txt","r") as f:
                   print(f.read().strip())
    except FileNotFoundError:
               print("Diary file is currently missing!")
       
       
    try:
               with open ("missing.txt","r") as f:
                   content = f.read()
    except FileNotFoundError:
               print("Safe exist: missing.txt not found")
run_diary_exercise()
                   
            




