#Program for accepting List of Employee Values and save them in a file
#EmpPickEx.py
import pickle
def saverecord():
    with open("emp.pick","ab")  as fp:
        while(True):
            try:
                #accept the employee values
                print("-"*50)
                empno=int(input("Enter Employee Number:"))
                empname=input("Enter Employee Name:")
                empsal=float(input("Enter Employee Salary:"))
                print("-" * 50)
                lst=list() # Create an empty list
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                pickle.dump(lst,fp)
                print("Employee Data saved in a File")
                print("-" * 50)
                ch=input("Do you want to insert another record?(yes/no):")
                if ch.lower()=="no":
                    print("Thx for using program")
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for empno,and sal--try again")

#Main Program
saverecord()