import pandas
import os
os.chdir('C:\ws\python\Spider\Dataset')
filenames = []
def create(filenames):    
    str1 = r'Dataset\Iteration_'
    i = 1
    while i in range(1,31):
        str2 = str1 + str(i) + "\\" + str(i) + "_0_"
        for j in range(1,14):
            str3 = str2 + str(j)
            for k in range(2):
                if k == 0:
                    str4 = str3 + "_a"+".csv"
                    filenames.append(r'{}'.format(str4))
                else:
                    str4 = str3 + "_b"+".csv"
                    filenames.append(r'{}'.format(str4))
        i += 1
    while i in range(31,61):
        str2 = str1 + str(i) + "\\" + str(i) + "_1_"
        for j in range(1,14):
            str3 = str2 + str(j)
            for k in range(2):
                if k == 0:
                    str4 = str3 + "_a"+".csv"
                    filenames.append(r'{}'.format(str4))
                else:
                    str4 = str3 + "_b"+".csv"
                    filenames.append(r'{}'.format(str4))
        i += 1
    while i in range(61,91):
        str2 = str1 + str(i) + "\\" + str(i) + "_2_"
        for j in range(1,14):
            str3 = str2 + str(j)
            for k in range(2):
                if k == 0:
                    str4 = str3 + "_a"+".csv"
                    filenames.append(r'{}'.format(str4))
                else:
                    str4 = str3 + "_b"+".csv"
                    filenames.append(r'{}'.format(str4))
        i += 1
create(filenames)
#def subtract(filenames):
#for filename in filenames:
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, filenames[0])
testFile=open(filename)
testFile.read()
print(type(testFile))
    
       
        
        
        
        
create(filenames)   
