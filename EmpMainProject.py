#EmpMainProject.py<---Main Program
from EmpMenu import menu
from EmpAdd import addEmployee
from EmpView import viewAllEmployees,viewSingleEmployee
from EmpUpdate import updateEmployee
from EmpSearch import searchEmployee
from EmpDelete import deleteEmployee
import sys
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addEmployee()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployees()
            case 6:
                searchEmployee()
            case 7:
                print("\tThx for using Project")
                sys.exit()
            case _:
                print("\tUR Selection of Operation is wrong--try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice--try again")