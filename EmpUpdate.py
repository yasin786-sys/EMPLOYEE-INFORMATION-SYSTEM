#EmpUpdate.py<-------Module Name
import pickle
def updateEmployee():
    with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","rb")  as fp:
        records=[] # For String Record(s)
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    eno = int(input("Enter Employee Number for updating Salary: "))
    res=False
    for index in range(len(records)):
        if(records[index][0]==eno):
            recindex=index
            res=True
            break
    print("-"*50)
    if(res):
        newsal=float(input("Enter New Salary for Employee: "))
        records[recindex][2]=newsal
        #re-write the updated record to the file
        with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","wb")  as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Salary Updated--verify")
    else:
        print("\tEmployee Record Does not Exist")
    print("-" * 50)