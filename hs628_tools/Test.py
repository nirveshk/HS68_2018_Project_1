
import numpy as np
from sklearn import datasets
import csv
import os




class data_split:
    """
    Create class data_split to predict a perfect train and test data split ratio

    define methods to accomplish this task

    return a split ratio

    """
    def __init__(self, data):
        self.data = data

    #set path to read the csv file in the directory
    def test_train():

        pathName = os.getcwd()

        dataset = []
        fileNames = os.listdir(pathName)

        # read file with extension .csv
        for fileNames in fileNames:
            if fileNames.endswith(".csv"):
                dataset.append(fileNames)

        for k in dataset:
            file = open(os.path.join(pathName, k), "rU")
            data = csv.reader(file, delimiter=',')
            # data_len =sum(1 for line in data)
            # print data_len


        for column in data:

            for column in data:

                for row in column:

                    if row == "?":
                        pass
                    if row == "NA":
                        pass
                    if row == "NAN":
                        pass
                    else:
                        print (row)
            return row

        #********

    test_train()

    # row_len = sum(1 for line in test_train())
    # print row_len
