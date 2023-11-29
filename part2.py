# part 2 : Display  all the history
def list_of_history(data):
    print("Part 2:")
    for i in data:
        print(i)   
    
def create_txt(data):
    file = open("History of the marks.txt","w")
    file.write("Part 3 :\n")
    for i in data:
        file.write(f"{i}\n")
    file.close()