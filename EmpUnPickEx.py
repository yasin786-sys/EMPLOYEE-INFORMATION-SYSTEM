#Program for reading the records from the file by using un-pickling Process
#EmpUnPickEx.py
import pickle
def readrecords():
    try:
        with open("emp.pick","rb") as fp:
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

#main Program
readrecords()