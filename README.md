# CBFV
Tool to quickly create a composition-based feature vector

## Usage
The file `example_code.py` can be used to quickly make predictions for any given property. Simply input the location of your desired train and test data. 

## making the composition-based feature vector
The folder cbfv has the script `composition.py` and the folder "element_properties".

This script uses some chemical parsing tools from matminer and then does numpy operations to vectorize composition at a rate of ~10,000 formulae per second. 

## getting the features on their own.
These can be extracted and saved to csv or simply used in the learning process. See example_code.py for how to access the featurized data
