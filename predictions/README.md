type "python3 runModel.py" or "python3 runBayesNet.py {FILENAME}" to print out the prediction         
runBayesNet.py uses the current model       
it will print the number of errors and the number of instances
in the test set. The full output will be in prediction.txt      
       
Some things to note:      
the FILENAME field should be either testing.csv or partialTestSet.arff, or any other correctly created data files       
runBayesNet.py uses the partialBayesNet model which i arbitrarily split the data into training and test data by hand     
This means it did not use a 10-fold cross validation        
This allows us run the model and test using runBayesNet.py manually, something we can do for a presentation without testing on the same data that we used to train the model       

bayesNet.model is the model that was trained using the entirety of our data and as such i don't actually have data to test it with     
Instead, a 10 fold cross validation was used