#EmpView.py<-------Module Name
import pickle
def viewSingleEmployee():
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
                rec=record
                res=True
                break
        print("-" * 50)
        if(res):
            print("\tEmployee Number:{}".format(rec[0]))
            print("\tEmployee Name:{}".format(rec[1]))
            print("\tEmployee Salary:{}".format(rec[2]))
        else:
            print("\tEmploye Record Does not Exist")
        print("-" * 50)

def viewAllEmployees():
    try:
        with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","rb")  as fp:
            print("-----------------------------------------")
            print("\tENO\t\tNAME\tSAL")
            print("-----------------------------------------")
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-----------------------------------------")
                    break
    except FileNotFoundError:
        print("File Does Not Exist")
