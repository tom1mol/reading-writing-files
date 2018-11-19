f = open("newfile.txt", "a")        #"w" argument for write instead of "r"for read. could also use "a" for append
lines = ["Hello", "World", "Welcome", "To", "File IO"]
text = "\n".join(lines)     #joins above line into 1 string using \n as a seperator
f.writelines(text)            #had f.write and replaced with f.writelines. also changed inside brackets(from " Hello\n" to (lines))..then chaged to text
f.close()



#when we run this a new file called newfile.txt is created