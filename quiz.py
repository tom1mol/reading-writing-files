f = open('data.txt', 'r')       #variable f..and open data.txt file for reading
lines = f.read()           #changed to read from readlines as readlines split it into line of strings
                            #all data now in single string and appears as text not a list of strings
                            #new line character(\n) causes the string to be displayed over 4 lines
f.close()                       #close file handle
print(lines)                    #print results to screen




#this runs with data.txt

"""
f = open("data.txt", "r")
lines = f.readlines()
#f.close()
print(lines)

"""
#output:
#['This is the first line  \n', 'And this is the second\n', 'Here is the third line\n', 'And here, the fourth\n', '\n', '\n', '\n']
    
#code opened the file. read the lines into a variable called lines and outputs a list of strings(on line above)^each with \n
#readlines method splits the string