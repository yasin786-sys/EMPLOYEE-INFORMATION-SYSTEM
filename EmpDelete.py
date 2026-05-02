#EmpDelete.py<-------Module Name
import pickle
def deleteEmployee():
    with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick","rb")  as fp:
        records=[] # For String Record(s)
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    eno=int(input("Enter Employee Number to Delete:"))
    res=False
    for record in records:
        if(record[0]==eno):
            rec=record
            res=True
            break
    print("-"*50)
    if(res):
      records.remove(rec)
      #Re-write the records back to the fle
      with open("D:\\PYTHON PROGRAMS\\EMPLOYEE INFORMATION SYSTEM\\EMPPROJECT.pick", "wb") as fp:
          for record in records:
              pickle.dump(record, fp)
      print("\tEmployee Record Deleted--verify")
    else:
        print("Employee Record Does Not Exist")
    print("-" * 50)
