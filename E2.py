import pandas
f = open("testcaseStudent.txt") #to open the testcase
numberoftestcases=int(f.readline()[:-1]) #to read the number of testcases
for item in range(numberoftestcases):
    ff = open("output"+str(item+1)+".txt", "w") #to write to output files.
    batchname=f.readline()[:-1]  #To read the batch filename from testcase.
    stattolook=f.readline()[:-1] #To read the Percentage range pairs
    batchindex=batchwiselist.index(batchname) #Batchwise list is the folder containing the "batchwiselist"
    statval=batchwisestatistics[batchindex][stattolook].values #To retrieve the values of the number of students who have attended the quiz from the given batch 
    for item in statval:
        ff.write("%s\n" % str(item)) 
        
ff.close()
f.close()