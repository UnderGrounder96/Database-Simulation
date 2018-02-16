#!/usr/bin/python
#Lucio Afonso gr. 1

import sys
import Module
import argparse
from Module.config import *
from Module.classy import MyError
        
def mainly():    
    try:
        try:     
            parser = argparse.ArgumentParser(description="This program is a front-end for MySQL server and allows basic CRUD operations. Please run \'python main.py\' in order to use it.")
            parser.parse_args()       
            
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

            mainly()
            
    except MyError as e: 
        print e.value
        
    finally:
        pass
    
def main():
    mainly()
    
    # Closes all cursors
    cursor.close()
    # Closes all databases
    db.close()	
    
    print "\nGood bye!"	
    exit(0)

if __name__== "__main__":
    main()