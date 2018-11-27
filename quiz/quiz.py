def show_menu():                        #function called show menu
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter Option: ")
    return option
    
def add_question():
    print("")                                #print a blank line
    question = input("Enter a question\n> ")        #question prompt
    
    print("")                                   #print blank line
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))  #{0} take question we already asked. blank line. greater than prompt
                #using formaT method we insert question. user asked question when they go to put answer in
                
    file = open("questions.txt", "a")   #open questions.txt for appending
    file.write(question + "\n")         # write question with new line at end
    file.write(answer + "\n")           #answer goes on own line
    file.close()
    
    
#print(show_menu())  we had this to check the code worked
def game_loop():
    while True:     #ie loop forever unless theres a break
        option = show_menu()        #call show_menu function and store choice in option variable 
        if option == "1":
            print("You selected 'Ask questions'")
        elif option == "2":         #use cat questions.txt to look at the contents of questions.txt
            add_question()                        #print("you selected 'Add a question'")
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()
        
        