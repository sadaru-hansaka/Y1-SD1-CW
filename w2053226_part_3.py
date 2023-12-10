#part 3   
def create_txt_file(history_list):
    file = open("History of the marks.txt","w") #create a text file in write mode
    file.write("Part 3 :\n") #heading
    for i in history_list:
        file.write(f"{i}\n")
    file.close()