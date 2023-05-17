# Hi there! Welcome to "Building an Adaboost model with Sklearn (Introductory Machine Learning)". 

"""
This kata can be broken up into the following steps:

    Import the relevant sklearn libraries (i.e. AdaBoostClassifier, train_test_split)
    Create the "train_ada_boost" function (more details below)
    Split the data (X) into a test set and a training set (you MUST USE sklearns train_test_split for this)
    TRAIN an adaBoostClassfier (Once again, you MUST USE sklearn for this).
    Your "train_ada_boost" function must return a three element tuple (more details below).

The "train_ada_boost" function accepts the following arguments:

    X -- This would normally be a dataset (but in this kata it is a 1D numpy array)
    Target -- This is a 1D numpy array consisting of 1's and 0's. This argument is the set of values we are trying to predict with our model
    estimators -- KEYWORD ARGUMENT if no argument is passed in the default value should be set to 3.
    random_seed -- KEYWORD ARGUMENT if no argument is passed in the default value should be set to 0.

Your function should return a 3 element tuple consisting of the following values in this exact order:

    A TRAINED AdaBoostClassifer (return the actual model)
    A test set (1D numpy array, which was built by sklearns test_train_split function)
    A target array (1D numpy array, which was built by sklearns test_train_split function))

Details:

    Your model should be trained using the specified number of estimators, with a random state equal to seed.
    When splitting the data, be sure to set the random state equal to seed.
    ALL other parameters not mentioned here for both 'test_train_split' and 'AdaBoost' should be set to default values.
    Even though you are handling Numpy arrays there is no need to actually manipulate the arrays yourself (let sklearn to it for you!).

"""

# The Solution 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def train_ada_boost(X, target, estimators=3, random_seed=0):
    # Reshape X to a 2D array
    X = X.reshape(-1, 1)
    
    # Split the data into a test set and training set
    X_train, X_test, y_train, y_test = train_test_split(X, target, random_state=random_seed)
    
    # Create and train an AdaBoostClassifier
    model = AdaBoostClassifier(n_estimators=estimators, random_state=random_seed)
    model.fit(X_train, y_train)
    
    # Return the trained model, test set, and target array
    return model, X_test, y_test

# Example usage
X = np.array([3, 1, 4])  # Example input data
target = np.array([0, 1, 0])  # Example target values
trained_model, test_set, target_array = train_ada_boost(X, target, estimators=5, random_seed=42)

