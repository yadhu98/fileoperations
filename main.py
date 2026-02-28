def readFile(file):
    try:
        file.seek(0)
        r =file.read()
        print(r)
    finally:
        file.close()

def writeFile(file,string):
     try:
        file.write(' {}'.format(string))
        file.seek(0)
        rd = file.read()
        print(rd)
     finally:
        file.close()

def countWords(file):
     try:
        file.seek(0)
        r = file.read()
        cumulativewordcount=0
        for item in r:
            if(item == ' '):
                cumulativewordcount+=1
        cumulativelettercount = 0
        for item in r:
            if(item != ' '):
                cumulativelettercount+=1
        print('letter count: {}\n word count: {}'.format(cumulativelettercount,cumulativewordcount))
    
     finally:
        file.close()


def clearFile(file):
    try:
        file.seek(0)
        file.truncate()
    finally:
        file.close()


while True:
    try:
        option = int(input("Choose an option\n 1) Write 2) Read 3) Count 4) Clear file 5)Exit   "))
        if(option == 5):
            break
        with open("./test.txt","a+") as f:
            if(option == 1):
                sentences= input('Enter some script')
                writeFile(f,sentences)
            elif(option == 2):
                readFile(f)
            elif(option == 3):
                countWords(f)
            elif(option == 4):
                clearFile(f)
            else:
                print("Invalid Input")
    except ValueError:
        print("!! Invalid Input. Please enter a number (1, 2, 3, 4 or 5).")
        print("-" * 30)