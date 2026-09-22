
def ask():
    filename= input("file name please ")
    try:
         with open(filename,"r") as f:
              print(f.read().strip())   
    except FileNotFoundError:
         print("please enter a file name")


ask()

    

                    
