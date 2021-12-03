import os
import sys

dataFile = "partialTestSet.arff"

#check if there is an argument given THERE NEEDS TO BE ONE
if(len(sys.argv) > 1):
    dataFile = sys.argv[1]
else:
    print("error: no argument given")
    exit(1)

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
    generated.writelines(arffContent[4096])
    generated.close()
    generatedWriteable = open("generated.arff")
    generatedContent = generatedWriteable.readlines()

    #convert arff file to generated
    arffWriteable = open("flamingo.txt", "w")
    arffWriteable.writelines(generatedContent)
    
    #remove generated
    os.remove("generated.arff")
    os.remove(arffFile)
    os.rename("flamingo.txt",arffFile)
    arffWriteable.close()

#run model on generated .arff
os.system("java -cp \"./weka.jar\" weka.classifiers.bayes.BayesNet -T " + dataFile + " -l bayesNet.model -p 0 -c 1 > prediction.txt")

# open the sample file used
file = open('prediction.txt')
  
# read the content of the file opened
content = file.readlines()

#read prediction of single instance
val = content[5]

if "malicous" in val:
    print("MALWARE")
elif "benign" in val:
    print("BENIGN")
else:
    print("ERROR")