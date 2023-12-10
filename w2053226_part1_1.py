# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID:
# Date: 



import w2053226_part1_2 #import histogram.py file
import w2053226_part_2 #import part2_and_3.py file to main code
import w2053226_part_3

#Progression outcomes as defined by the university regulations
#progress - 1
#progress(module trailer)-2
#do not progress - 19
#exclude - 6
university_regulation_data = [
    [120,0,0, "Progress"], 
    [100,20,0, "Progress (module trailer)"],
    [100,0,20, "Progress (module trailer)"], 
    [80,40,0, "Do not progress - module retriever"],
    [80,20,20, "Do not progress - module retriever"],
    [80,0,40, "Do not progress - module retriever"],
    [60,60,0, "Do not progress - module retriever"],
    [60,40,20, "Do not progress - module retriever"],
    [60,20,40, "Do not progress - module retriever"],
    [60,0,60, "Do not progress - module retriever"],
    [40,80,0, "Do not progress - module retriever"], 
    [40,60,20, "Do not progress - module retriever"],
    [40,40,40, "Do not progress - module retriever"],
    [40,20,60, "Do not progress - module retriever"],
    [20,100,0, "Do not progress - module retriever"], 
    [20,80,20, "Do not progress - module retriever"],
    [20,60,40, "Do not progress - module retriever"], 
    [20,40,60, "Do not progress - module retriever"], 
    [0,120,0, "Do not progress - module retriever"], 
    [0,100,20, "Do not progress - module retriever"], 
    [0,80,40, "Do not progress - module retriever"], 
    [0,60,60, "Do not progress - module retriever"], 
    [40, 0,80,"Exclude"],
    [20,20,80,"Exclude"],
    [20,0,100,"Exclude"],
    [0,40,80, "Exclude"], 
    [0,20,100,"Exclude"], 
    [0,0,120, "Exclude"] 
]

#define variables
pass_credit=0
fail_credit=0
defer_credit=0
total_of_credits= 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
outcome_count=0
history_list=[] #store all the input progression data

#get students credit marks as inputs
def user_input_credits(grade):
    while True:
        try:
            Input = input(f"PLease enter your credits at {grade} : ")
            Input = int(Input)
            if 0<=Input<=120 and (Input%20)==0:    #check the credit are in correct range [20,40,60,80,100,120]
                return Input 
            else:
                print("Out of range") #out of range msg
        except ValueError:
            print("Integer required, please enter a valid number")# required integer msg

#continue qn
def loop_qn():
    while True:
        #ask the user want to add more data or not
        continue_qn = input("\nWould You like to enter another set of data?\nEnter 'y' for yes 0r 'q' to quit and view results :").lower()
        continue_qn=str(continue_qn)
        if continue_qn=='y' or continue_qn=="q":
            return continue_qn #pass to belove comparison
        else:
            print("Invalid input") #if the user enter neither "q" or "y" ask the question again and display "Invalid input"
#ask user are you a tudent or a staff member
start_qn=input("Are you a student or a staff member?\nIf you are a student enter 's' or if you are a staff member enter 'm' : ").lower()      
start_qn=str(start_qn)
#student part
#if the user was a student the program should only display the progression outcome
if start_qn == "s":
    pass_credit = user_input_credits("Pass") #pass argument for input_credit function
    defer_credit = user_input_credits("Defer")
    fail_credit = user_input_credits("Fail")
    total_of_credits = pass_credit+defer_credit+fail_credit #calculate total of credits

    result_output = str
    if total_of_credits != 120: #check total is equal to 120
        print("Total incorrect")
    for credit in university_regulation_data: #check entered marks are in the list
        if credit[0]==pass_credit and credit[1]==defer_credit and credit[2]==fail_credit:#check user inputs are in the list
            result_output = credit[3] #according to the grade marks
            print(result_output) #display the progression outcome
    #Python for loops. Available at: https://www.w3schools.com/python/python_for_loops.asp (Accessed: 25 November 2023). 
#staff member part
#if the user was a staff member progran should display progrssion outcome,histogram,text file and history list
elif start_qn=="m":
    while True:
        pass_credit = user_input_credits("Pass") #pass argument for input_credit function
        defer_credit = user_input_credits("Defer")
        fail_credit = user_input_credits("Fail")
        total_of_credits = pass_credit+defer_credit+fail_credit #calculate total of credits

        result_output = str
        if total_of_credits != 120: #check total is equal to 120
            print("Total incorrect")
        for credit in university_regulation_data: #check entered marks are in the list
            if credit[0]==pass_credit and credit[1]==defer_credit and credit[2]==fail_credit:#check user inputs are in the list
                result_output = credit[3]
                print(result_output) #display the progression outcome
                outcome_count += 1 #count the number of outcomes

        #count the progress , exclude , Trailer , Retriever
        if result_output == "Progress":
            progress+=1 #count the number of progress marks
            history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")#append progress data to history_list
        elif result_output == "Progress (module trailer)":
            trailer+=1 #count the number of trailer marks
            #append trailer data to history_list
            history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")
        elif result_output == "Do not progress - module retriever":
            retriever +=1 #count the number of retriver marks
            #append retriever data to history_list
            history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")
        elif result_output == "Exclude":
            exclude += 1 #count the number of exclude marks
            #append exclude data to history_list
            history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")

        #get the returns from the loop_qn()
        continue_qn=loop_qn()
        #when user input "q" display - histogram,text file, history list 
        if continue_qn == "q": #check loop question's input
            w2053226_part1_2.graph(progress,trailer,retriever,exclude,outcome_count) #call graph function from histogram.py file
            w2053226_part_2.list_of_history(history_list) #call list_of_history function from part2_and_3.py file
            w2053226_part_3.create_txt_file(history_list) #call create_txt_file function from part2_and_3.py file
            break
        elif continue_qn == "y":
            continue
#if user not a student or a stafff member
else:
    print("oops! Something went wrong, Try again later.")
    
