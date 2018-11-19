#used with relative_data.txt. 
#relative path..identifies location of data file relative to script currently running
#starts in given location(working directory we're in) and works down from there
#absolute path starts at top of file system. not relative to running program. fully formed path to specific file

#to open a file using an absolute or relative path we specify the path in the open command
#if can refer to file using relative path is better as absolute paths couple applications very tightly to the file system



f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')       
lines = f.read()           
f.close()                       
print(lines) 




#input cd(change directory) in workspace to change directory. in this case cd files to go into files directory
#then pwd(print working directory) command. shows us our current location on the file system
#can get absolute path of individual file using readlink -f relativde_data.txt
#the output of above line is:    /home/ubuntu/workspace/files/relative_data.txt