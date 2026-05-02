#EmpSearch.py<-------Module Name
import pickle
def searchEmployee():
    with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","rb")  as fp:
        records=[] # For String Record(s)
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        empno = int(input("Enter Employee Number to View Employee Details:"))
        res=False # decision making var
        for record in records:
            if(record[0]==empno):
                res=True
                break
        print("-" * 50)
        if(res):
            print("\tValid Employee")
        else:
            print("\tInvalid Employee")
        print("-" * 50)
