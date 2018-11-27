def show_menu():                        #function called show menu
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter Option: ")  #option variable with input function to get the text. prompt is enter option
    return option           #function returns option the user selects
         #we tested the code at this point using print(show_menu())
    
def add_question():
    print("")                                #print a blank line
    question = input("Enter a question\n> ")        #question prompt. store in question variable 
    
    print("")                                   #print blank line
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))  #{0} take question we already asked. blank line. greater than prompt
                #using formaT method we insert question. user asked question when they go to put answer in
                
    file = open("questions.txt", "a")   #open questions.txt for appending
    file.write(question + "\n")         # write question with new line at end
    file.write(answer + "\n")           #answer with new line on end. Q & A on own line
    file.close()
    
    

def game_loop():
    while True:     #ie loop forever unless theres a break
        option = show_menu()        #call show_menu function and store choice in option variable 
        if option == "1":
            print("You selected 'Ask questions'")
        elif option == "2":         #use cat questions.txt to look at the contents of questions.txt in the console
            add_question()           #print("you selected 'Add a question'")..replaced by function add_question()
                                    #here we call function add_question()
        elif option == "3":
            break
        else:
            print("Invalid option") #in case someone enters number other than 1-3
        print("")
        
game_loop()
        
        