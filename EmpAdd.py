# EmpAdd.py<-------Module Name
import pickle
def isquniue(eno):
    with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","rb")  as fp:
        records=[] # For String Record(s)
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        res=True
        for record in records:
            if(record[0]==eno):
                res=False
                break
        return res

def addEmployee():
    with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","ab")  as fp:
        try:
            #accept the employee values
            print("-"*50)
            empno=int(input("Enter Employee Number:"))
            if(isquniue(empno)):
                empname=input("Enter Employee Name:")
                empsal=float(input("Enter Employee Salary:"))
                print("-" * 50)
                lst=list() # Create an empty list
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                pickle.dump(lst,fp)
                print("Employee Data saved in a File")
            else:
                print("Employee Number Already Exists")
            print("-" * 50)
        except ValueError:
            print("\tDon't enter alnums,strs and symbols for empno,and sal--try again")
