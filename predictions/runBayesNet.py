import os

os.system("java -cp \"./weka.jar\" weka.classifiers.bayes.BayesNet -T partialTestSet.arff -l partialBayesNet.model -p 0 -c 2 > prediction.txt")
# open the sample file used
file = open('prediction.txt')
  
# read the content of the file opened
content = file.readlines()

#read prediction of single instance
val = content[5][30]

val2 = content[41][34]

numErrors = 0
numInstances = len(content) - 6
for i in range(5,len(content) - 1):
    val3 = content[i][34]
    if val3 == "+":
        numErrors += 1

print(numErrors)
print("number of errors: ") 
print(numErrors)
print("number of instances: ")
print(numInstances)
print("accuracy: ")
print((numInstances - numErrors)/(numInstances))

#print prediction
#if(int(val) == 0):
   # print("NOT MALICIOUS")
#else:
   # print("MALICIOUS")