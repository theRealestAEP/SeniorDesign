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

    #open arff
    arff = open(dataFile)
    arffContent = arff.readlines()

    #generate a new file
    generated = open("generated.arff", 'a')

    #read from header
    headerFile = open("headers.txt")
    headerContent = headerFile.readlines()

    #write header content to generated
    generated.writelines(headerContent)
    generated.writelines("\n")

    #write arff content to generated
    generated.writelines(arffContent[4097:])
    print("WHY PARSE" + arffContent[4097])
    generated.close()
    generatedWriteable = open("generated.arff")
    generatedContent = generatedWriteable.readlines()

    #convert arff file to generated
    arffWriteable = open("flamingo.txt", "w")
    arffWriteable.writelines(generatedWriteable)

    #remove generated
    #os.remove("generated.arff")

#run model on generated .arff
os.system("java -cp \"./weka.jar\" weka.classifiers.bayes.BayesNet -T " + dataFile + " -l bayesNet.model -p 0 -c 2 > prediction.txt")

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