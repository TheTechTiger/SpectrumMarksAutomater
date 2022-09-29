from time import sleep
import os
try: 
    from tabula.io import convert_into
except:
    print("We ran into a problem")
    print("Trying to fix the code ...........")
    print("Please wait while we try. Afetr we are finished restart the program")
    print("If you still face the error, comment out the try and except and then run a program in a pre opened Terminal to get more details about the error")
    print("Startin fix in 5s. Please read the above details carefully...")
    sleep(5)
    os.system("pip install tabula-py")

def pdftocsv(fin):
    fout = fin[fin.rindex("\\")+1:]+".csv"
    convert_into(fin, fout, output_format="csv", pages='all')
    return fout

def GetStudName(NCno):
    for stud in studs:
        if NCno==stud['number']:
            return stud['name']

def getlist():
    fullLIST = []
    with open("RollNameBatch.csv", "r") as file:
        dat = file.readlines()
        for line in dat:
            str = line.replace("\n", "").split(",")
            curdat = {
                "name": str[1],
                "number": str[0],
                "batch": str[3]
            }
            fullLIST.append(curdat)
    return fullLIST

if __name__=="__main__":
    studs = getlist()
    rescsv = pdftocsv(input("Enter Result PDF file Path: "))
    singleSUBmrk = input("Enter Single Subjects Marks: ")
    newdat = ""

    with open(rescsv, "r") as file:
        resrows = file.readlines()
        for row in resrows:
            rown = row.replace("\n", "").split(",")
            if "Batch" in row:
                row = row.replace(",Batch", ",Name, Batch")
            if singleSUBmrk in row:
                row = row.replace(f",,{singleSUBmrk}", f",,,{singleSUBmrk}")
            if "NC" in rown[0]:
                name = GetStudName(rown[0])
                newdat += f"{rown[0]},{name},{rown[1]},{rown[2]},{rown[3]},{rown[4]},{rown[5]},{rown[6]}\n"
            else:
                newdat += row
    os.remove(rescsv)
    with open(rescsv+"NEWformatted.csv", "w") as f:
        f.write(newdat)
        f.close()