import histogram #import histogram.py file
import part2_and_3 #import part2_and_3.py file to main code

#Progression outcomes as defined by the university regulations
university_regulation_data = [
    [120, 0, 0, 'Progress'], # 1
    [100, 20, 0, 'Progress (module trailer)'], # 2
    [100, 0, 20, 'Progress (module trailer)'], # 3
    [80, 40, 0, 'Do not progress - module retriever'], # 4
    [80, 20, 20, 'Do not progress - module retriever'], # 5
    [80, 0, 40, 'Do not progress - module retriever'], # 6
    [60, 60, 0, 'Do not progress - module retriever'], # 7
    [60, 40, 20, 'Do not progress - module retriever'], # 8
    [60, 20, 40, 'Do not progress - module retriever'], # 9
    [60, 0, 60, 'Do not progress - module retriever'], # 10
    [40, 80, 0, 'Do not progress - module retriever'], # 11
    [40, 60, 20, 'Do not progress - module retriever'], # 12
    [40, 40, 40, 'Do not progress - module retriever'], # 13
    [40, 20, 60, 'Do not progress - module retriever'], # 14
    [40, 0, 80, 'Exclude'], # 15
    [20, 100, 0, 'Do not progress - module retriever'], # 16
    [20, 80, 20, 'Do not progress - module retriever'], # 17
    [20, 60, 40, 'Do not progress - module retriever'], # 18
    [20, 40, 60, 'Do not progress - module retriever'], # 19
    [20, 20, 80, 'Exclude'], # 20
    [20, 0, 100, 'Exclude'], # 21
    [0, 120, 0, 'Do not progress - module retriever'], # 22
    [0, 100, 20, 'Do not progress - module retriever'], # 23
    [0, 80, 40, 'Do not progress - module retriever'], # 24
    [0, 60, 60, 'Do not progress - module retriever'], # 25
    [0, 40, 80, 'Exclude'], # 26
    [0, 20, 100, 'Exclude'], # 27
    [0, 0, 120, 'Exclude'] # 28
]

#define variables
pass_credit=0
fail_credit=0
defer_credit=0
total_of_credits= 0
continue_qn=''
progress = 0
trailer = 0
retriever = 0
exclude = 0
outcome_count=0
history_list=[] #store all the input progression data

#get students credit marks as inputs
def input_credits(level):
    while True:
        try:
            Input = input(f"PLease enter your credits at {level} : ")
            Input = int(Input)
            if 0<=Input<=120 and (Input%20)==0:    #check the credit are in correct range
                return Input
            else:
                print("Out of range") #out of range msg
        except ValueError:
            print("Integer required, please enter a valid number")# required integer msg

#continue qn
def loop_qn():
    while True:
        #ask the user want to add more data or not
        continue_qn = input("\nWould You like to enter another set of data?\nEnter 'y' for yes 0r 'q' to quit and view results :")
        continue_qn=str(continue_qn)
        if continue_qn=='y' or continue_qn=="q":
            return continue_qn
        else:
            print("Invalid input") #if the user enter neither "q" or "y" ask the question again and display "Invalid input"
       

while True:
    pass_credit = input_credits("Pass") #pass argument for input_credit function
    defer_credit = input_credits("Defer")
    fail_credit = input_credits("Fail")
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
        history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")#append trailer data to history_list
    elif result_output == "Do not progress - module retriever":
        retriever +=1 #count the number of retriver marks
        history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")#append retriever data to history_list
    elif result_output == "Exclude":
        exclude += 1 #count the number of exclude marks
        history_list.append(f"{result_output} - {pass_credit} , {defer_credit} , {fail_credit}")#append exclude data to history_list

    continue_qn=loop_qn() 
    if continue_qn == "q": #check loop question's input
        histogram.graph(progress,trailer,retriever,exclude,outcome_count) #call graph function from histogram.py file
        part2_and_3.list_of_history(history_list) #call list_of_history function from part2_and_3.py file
        part2_and_3.create_txt_file(history_list) #call create_txt_file function from part2_and_3.py file
        break
    elif continue_qn == "y":
        continue

    
