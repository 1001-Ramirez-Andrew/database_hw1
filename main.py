#Author: Andrew Ramirez
#Project 1 CS 457
#Date: 9/23/2022
import os

#used to keep track of the path the directory the program first started in
cwd = os.getcwd()

# for USE command: selects the Database to be used implemented by changing directories
def useDB(db):
    path = os.path.join(cwd, db)
    try:
        os.chdir(path)
    except OSError as error:
        print("!Failed to use", db, "because it does not exist.")

#used for DROP command: removes a Database and is implemented by deleting a directory using OS
def dropDB(db):
    path = os.path.join(cwd, db)
    clear = True
    try:
        os.rmdir(path)
    except OSError as error:
        print("!Failed to delete", db, "because it does not exist.")
        clear = False
    if clear:
        print("Database", db, "deleted.")


#used for DROP command: removes a table(file) inside a Database(directory) by means of os.remove()
def dropTBL(tbl):
    clear = True
    try:
        os.remove(tbl)
    except:
        print("!Failed to delete", tbl, "because it does not exist.")
        clear = False
    if clear:
         print("Table tbl_1 deleted.")

#used for CREATE command: creates a Database(directory). Uses os.path.join() to find appropriate path
def createDB(db):
    path = os.path.join(cwd, db)
    clear = True
    try:
        os.mkdir(path)
    except OSError as error:
        print("!Failed to create database", db, "because it already exists.")
        clear = False
    if clear:
        print("Database", db, "created.")

#This creates the table by making a file. The first line in the file contains the variable types that are stored
def createTBL(tbl, args):
    clear = True
    try:
        f = open(tbl, 'x')
    except:
        print("!Failed to create table", tbl, "because it already exists.")
        clear = False
    if clear:
        f.close()
    if clear:
        fin = open(tbl, 'w')
        for vars in args:
            fin.write(vars + " ")
        fin.write("\n")
        fin.close()

#this function is not on the example output but is called whenever there are mistakes in the command
def errFormat():
    print("Not a valid command")

#reads from the first line in the table(file). There is string splicing and function calls to get it into the proper format
def selectTBL(property, tbl):
    clear = True
    try:
        f = open(tbl, 'r')
    except:
        print("!Failed to query table", tbl, "because it does not exist.")
        clear = False
    if clear:
        if property == "*":
            for line in f:
                newline = line.lstrip("(").removesuffix(")").rstrip(" \n")
                newline = newline[:-1]
                args = newline.split(",")
                select = ""
                for vars in args:
                    select = select + vars.lstrip() + " | "
                select = select.rstrip(" | ")
                print(select)
        f.close() 

#modifies the first line of the file and adds the new variable name and type.
def alterTBL(tbl, tname, vartype):
    clear = True
    try:
        f = open(tbl, "r")
    except:
        print("!Failed to modify", tbl, "because it does not exist")
        clear = False
    if clear:
        old = f.readline()
        f.close()
        oldModify = old.rstrip(" \n")
        new = oldModify[:-1] + ", " + tname + " " + vartype + ")"
        f = open(tbl, 'w')
        f.write(new + "\n")
        f.close()

#this is the main loop that prompts the user and parses the input/calls approiate functions
while True:
    #input takes the whole line from the user including endline
    userInput = input()
    if userInput[-1] != ";":
        errFormat()
        continue
    userInput = userInput.replace(";", "")
    tokens = userInput.split()
    if len(tokens) == 0:
        errFormat()
        continue

    if tokens[0].upper() == "CREATE":
        if tokens[1].upper() == "DATABASE":
            createDB(tokens[2])
        elif tokens[1].upper() == "TABLE":
            createTBL(tokens[2], tokens[3:])
        else:
            errFormat()
    elif tokens[0].upper() == "SELECT":
        if tokens[2].upper() == "FROM":
            selectTBL(tokens[1], tokens[3])
        else:
            errFormat()
    elif tokens[0].upper() == "DROP":
        if tokens[1].upper() == "DATABASE":
            dropDB(tokens[2])
        elif tokens[1].upper() == "TABLE":
            dropTBL(tokens[2])
        else:
            errFormat()
    elif tokens[0].upper() == "USE":
        useDB(tokens[1]) 
    elif tokens[0].upper() == "ALTER":
        if (tokens[1] != "TABLE") and (tokens[3] != "ADD"):
            errFormat()
            continue
        alterTBL(tokens[2], tokens[4], tokens[5])
    elif tokens[0].upper() == ".EXIT":
        break
    else:
        errFormat()
print("All done.") 
         

            
            
     






