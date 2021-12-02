import os
import sys

dataFile = "partialTestSet.arff"

if(len(sys.argv) > 1):
    dataFile = sys.argv[1]

print(dataFile)
if(os.path.exists("./" + dataFile)):
    print("exists!")
else:
    print("problem: file doesn't exist in given directory")
    exit(1)

#create .arff file from a given .csv
if(dataFile[-3:-1] + dataFile[-1] == "csv"):
    print("given a .csv, converting to .arff")
    arffFile = dataFile[0:-4] + ".arff"
    os.system("java -cp \"./weka.jar\" weka.core.converters.CSVLoader " + dataFile + " > " + arffFile + " -B 1000")
    dataFile = arffFile

#run model on generated .arff
os.system("java -cp \"./weka.jar\" weka.classifiers.bayes.BayesNet -T " + dataFile + " -l bayesNet.model -p 0 -c 2 > prediction.txt")

# open the sample file used
file = open('prediction.txt')
  
# read the content of the file opened
content = file.readlines()

#read prediction of single instance
dataPoint = content[5]

if "benign" in dataPoint:
    print("it is not malware")
elif "malicious" in dataPoint:
    print("malicious!")

#print prediction
#if(int(val) == 0):
   # print("NOT MALICIOUS")
#else:
   # print("MALICIOUS")