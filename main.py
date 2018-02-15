#!/usr/bin/python
#Lucio Afonso gr. 1

import sys
import Module
from Module.config import *
from Module.classy import MyError

        
def main():    
    try:
        try:                      
            if (len(sys.argv) == 2):
                if sys.argv[1] == "-h":
                    f = open("README.md","r") #opens file with name of "test.txt"
                    myList = []
                    
                    for line in f:
                        myList.append(line)
                    else:
                        print myList
                        f.close()
                        
                exit(0)
            else:
                x = int(raw_input("\nWhich table operation would you require?\nALTER, CREATE or DROP(1), \
DELETE, INSERT or UPDATE(2), SELECT(3) or exit(4): "))
            
        except ValueError:
            raise MyError("Please enter a number from 1-4 only!")
            
        else:
            if x == 1:   
                Module.altrCrtDrp()

            elif x == 2:            
                Module.delInsUpd()

            elif x == 3:            
                Module.select()

            elif x == 4:                
                return
            
            else:
                raise MyError("Please enter a number from 1-4.")

            main()
            
    except MyError as e: 
        print e.value
        
    finally:
        pass
    
    # Closes all cursors
    cursor.close()
    # Closes all databases
    db.close()	
    
    print "\nGood bye!"	
    exit(0)
    
if __name__== "__main__":
    main()