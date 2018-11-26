with open("challenge1.txt", "w+") as f:
    f.write("Hello, World")
    f.seek(0)
    data = f.read()
    
    
    
#down in the workspace i entered:
#
# f = open("challenge1.txt", "w+")      this clears the text from the file challenge1.txt
# f.write("ur a cunt")            this loads the new text but doesnt print it
# data = f.read() or f.close()   this prints out the text(ur a cunt) in the challenge1.txt file

#there are 2 ways of doing it out. as a .py file and call it from the workspace python3 challeng1.py 
#or in the workspace line 10-12