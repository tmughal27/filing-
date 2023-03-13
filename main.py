import os

def addseqfield():
    pf = open("document1.txt","rt")
    sf = open("document2.txt","wt")

    myid = input("enter ID and enter -1 to end program: ")

    if myid != -1:
        isadded = False
        thisid = pf.readline().strip()

        myname = input("enter name:  ")
        mygrade = input("enter grade: ")
        while thisid != "":
            thisname = pf.readline().strip()
            thisgrade = pf.readline().strip()

            if isadded == False and int(myid) < int(thisid):
                isadded = True
                sf.write(myid + "\n")
                sf.write(myname + "\n")
                sf.write(mygrade + "\n")

            sf.write(thisid + "\n")
            sf.write(thisname + "\n")
            sf.write(thisgrade + "\n")

            thisid = pf.readline().strip()

        if isadded == False:
            sf.write(myid + "\n")
            sf.write(myname + "\n")
            sf.write(mygrade + "\n")

    sf.close()
    pf.close()

    os.remove("document1.txt")
    os.rename("document2.txt", "document1.txt")


def readseqfield():
    mf = open("document1.txt","rt")
    id = mf.readline()

    while id != "":
        name = mf.readline()
        grade = mf.readline()

        print(id , end = '')
        print(name , end = '')
        print(grade , end = '')

        id = mf.readline()

    mf.close()

def searchseqfield():
    found = False
    mf = open("document1.txt","rt")
    id = mf.readline().strip()
    myid = input("enter the id you want to search: ")

    while found == False and int(id) <= int(myid):
        name = mf.readline().strip()
        grade = mf.readline().strip()

        if int(id) == int(myid):
            found = True
            print(id , name , grade)
        id = mf.readline().strip()
    mf.close()

def editseqfield():

    myid = input("enter id to edit or enter -1 to end the program: ")
    myname = input("enter name ")
    mygrade = input("enter grade ")
    if myid != -1:
        pf = open("document1.txt","rt")
        sf = open("document2.txt","wt")

        thisid = pf.readline().strip()
        while thisid != "":
            thisname = pf.readline().strip()
            thisgrade = pf.readline().strip()

            if int(thisid) == int(myid):
                sf.write(myid +"\n")
                sf.write(myname + "\n")
                sf.write(mygrade + "\n")
            else:
                sf.write(thisid +"\n")
                sf.write(thisname +  " \n")
                sf.write(thisgrade + "\n")

            thisid = pf.readline().strip()

    else:
        return -1

    sf.close()
    pf.close()

    os.remove("document1.txt")
    os.rename("document2.txt", "document1.txt")

def seqfielddelete():


        myid = input("Enter the ID you want to delete or enter -1 to end program: ")

        if myid != "-1":
            try:
                myid = int(myid)
            except ValueError:
                print("Invalid input. Please enter a valid integer ID.")
                return

            with open("document1.txt", "rt") as pf, open("document2.txt", "wt") as sf:
                while True:
                    thisid = pf.readline().strip()
                    if not thisid:
                        break
                    thisname = pf.readline().strip()
                    thisgrade = pf.readline().strip()

                    if int(thisid) != myid:
                        sf.write(f"{thisid}\n")
                        sf.write(f"{thisname}\n")
                        sf.write(f"{thisgrade}\n")

            os.remove("document1.txt")
            os.rename("document2.txt", "document1.txt")

            print(f"Record with ID {myid} has been deleted from the file.")

        else:
            print("Program terminated by user.")



seqfielddelete()