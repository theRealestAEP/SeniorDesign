import os

os.system("java -cp \"./weka.jar\" weka.classifiers.bayes.BayesNet -T single_instance.arff -l current_model.model -p 0 -c 2 > prediction.txt")
# open the sample file used
file = open('prediction.txt')
  
# read the content of the file opened
content = file.readlines()

#read prediction of single instance
val = content[5][30]

#print prediction
if(int(val) == 0):
    print("NOT MALICIOUS")
else:
    print("MALICIOUS")