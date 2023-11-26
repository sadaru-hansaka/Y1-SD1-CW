import histogram

#Progression outcomes as defined by the university regulations
university_regulation_data = [
    [120, 0, 0, 'Progress'], # 1
    [100, 20, 0, 'Progress (module trailer)'], # 2
    [100, 0, 20, 'Progress (module trailer)'], # 3
    [80, 40, 0, 'Do not Progress - module retriever'], # 4
    [80, 20, 20, 'Do not Progress - module retriever'], # 5
    [80, 0, 40, 'Do not Progress - module retriever'], # 6
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
pass_credit=0
fail_credit=0
defer_credit=0
total_of_credits= 0
loop=''
progress = 0
trailer = 0
retriever = 0
exclude = 0

    #get students credit marks as inputs
def input_credits(level):
    while True:
        try:
            Input = input(f"PLease enter your credits at {level} : ")
            Input = int(Input)
            if 0<=Input<=120 and (Input%20)==0:    #check the credit is in correct range
                return Input
            else:
                print("Out of range") #out of range msg
        except ValueError:
            print("Integer required, please enter a valid number")# required integer msg


#def progression_outcome():
    #obb = str
    #if total_of_credits != 120:
        #print("Total incorrect")
        #return
    #for credit in university_regulation_data:
        #if credit[0]==pass_credit and credit[1]==defer_credit and credit[2]==fail_credit:
            #obb = credit[3]
            #print(obb)

def qn():
    while True:
        loop = input("\nWould You like to enter another set of data?\nEnter 'y' for yes 0r 'q' to quit and view results :")
        loop=str(loop)
        if loop=='y':
            print("Continuing")
            return "y"
        elif (loop=="q"):
            print("Thank you for using our system")
            return "q"
        else:
            print("Invalid input")
            return loop

while True:
    pass_credit = input_credits("Pass")
    defer_credit = input_credits("Defer")
    fail_credit = input_credits("Fail")
    total_of_credits = pass_credit+defer_credit+fail_credit

    obb = str
    if total_of_credits != 120:
        print("Total incorrect")
    for credit in university_regulation_data:
        if credit[0]==pass_credit and credit[1]==defer_credit and credit[2]==fail_credit:
            obb = credit[3]
            print(obb)
    #count the progress , exclude , Trailer , Retriever
    if obb == "Progress":
        progress+=1
    elif obb == "Progress (module trailer)":
        trailer+=1
    elif obb == "Do not Progress - module retriever":
        retriever +=1
    elif obb == "Exclude":
        exclude += 1
    print(f"Progress = {progress}")
    print(f"Trailer = {trailer}")
    print(f"Retiever = {retriever}")
    print(f"Exclude = {exclude}")

    loop=qn()
    if loop == "q":
        histogram.graph()
        break
    elif loop == "y":
        continue
    elif (loop!="y" or loop!="q"):
        break
    
