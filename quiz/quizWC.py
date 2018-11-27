def show_menu():                        #function called show menu
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter Option: ")  #option variable with input function to get the text. prompt is enter option
    return option           #function returns option the user selects
         #we tested the code at this point using print(show_menu())

def ask_questions():
    questions = []      #2 empty lists[]. 1 each for Q&A
    answers = []
    
    with open("questions.txt", "r") as file:        #with block. 
        lines = file.read().splitlines()  #read file in and split the lines and put in variable lines
        #once you leave with block..it closes automatically as in next line of code
        
    for i, text in enumerate(lines): #enumerate function turns each list into a tuple wit line num stored in i
        if i%2 == 0:                    #and the text stored in text
            questions.append(text)  #if i is even = question. first line is line zero(even)
        else:
            answers.append(text)     #otherwise odd..an answer
            
    for question, answer in zip(questions, answers): #take Q&A and use zip function to put them together
        guess = input(question + "> ")      #an input with guess
        
        
    
    
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
            ask_questions()     # when building we had this instead.....print("You selected 'Ask questions'")
        elif option == "2":         #use cat questions.txt to look at the contents of questions.txt in the console
            add_question()           #print("you selected 'Add a question'")..replaced by function add_question()
                                    #here we call function add_question()
        elif option == "3":
            break
        else:
            print("Invalid option") #in case someone enters number other than 1-3
        print("")
        
game_loop()

"""
we use "with" block. we open questions.txt 
we use enumerate function which creates a tuple in memory with line num at beginning which we represent with i
and then the text
then we check to see if line nums are even or odd and we put them into questions or answers
finally we use zip function to put everything together into another tuple in memory

tuple looks like this:
[
("What is capital of Ireland?", "Dublin")   question followed by answer
("what is capital of France?", "Paris")
]
"""
"""        
  OK then, tell me the answer
3
> 3

1. Ask questions
2. Add a question
3. Exit Game
Enter Option: 3
tom1mol:~/workspace/quiz (master) $ python3 quiz.py
1. Ask questions
2. Add a question
3. Exit Game
Enter Option: 1
Traceback (most recent call last):
  File "quiz.py", line 60, in <module>
    game_loop()
  File "quiz.py", line 50, in game_loop
    ask_questions()     # when building we had this instead.....print("You selected 'Ask questions'")
  File "quiz.py", line 18, in ask_questions
    for i, text in enumerate(lines): #enumerate function turns each list into a tuple wit line num stored in i
TypeError: 'builtin_function_or_method' object is not iterable
tom1mol:~/workspace/quiz (master) $ 
"""