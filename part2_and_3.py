# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: ……………………..…
# Date: ……………………..…


# part 2 : Display  all the history
def list_of_history(history_list):
    print("\nPart 2:")
    for i in history_list:
        print(i)   

#part 3   
def create_txt_file(history_list):
    file = open("History of the marks.txt","w") #create a text file in write mode
    file.write("Part 3 :\n") #heading
    for i in history_list:
        file.write(f"{i}\n")
    file.close()