#Create a sample file consisting of four lines of text.

#Using the r+ mode, overwrite the first line. Then, move the file cursor to overwrite 
#the third line. Finally, append a line to the file.

with open("challenge2.txt", "r+") as f:
    f.write("line 0")
    current_position = f.tell() 
    f.seek(current_position + 8)
    f.write("line 6")
    f.seek(0, 2)
    f.write("\nline 5")
    
"""
>>> f = open("challenge2.txt", "r+")
>>> f.write("line 0")
6
>>> current_position = f.tell()  #when u press enter line 1 is replaced by line 0
>>> f.seek(current_position + 8)
14
>>> f.write("line 6")
6
>>> f.seek(0, 2)     #this inserts line 6 instead of line 3. 
27
>>>f.write("\nLine 5")

"""
