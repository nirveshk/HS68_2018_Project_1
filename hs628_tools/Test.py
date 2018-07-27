
import numpy as np
from sklearn.model_selection import train_test_split






class data_split:
    """
    Create class data_split to predict a perfect train and test data split ratio.

    defines method to accomplish this task.

    returns a split ratio.

    Identifies Missing values as Nan for any missing value, return train and test dataframe with uniform division
    of NAN between train and test data per the data split ratio.

    """
    def __init__(self, data):
        self.data = data


    def test_train():
        """
        Reads in csv file using np.genfromtxt, counts number of NANs in the dataset

        """

        data = np.genfromtxt(csv_datafile, delimiter=',', skip_header=1)
        np.isnan(data).sum() #counts the number of "NANs" in dat
        #print data.shape



        #set calculation standard for specific datalengths, this is based on the general rule of thumb
        #ratio increases as the length of the data increases, so to ensure we have  enough data to train and test
        #for the smaller datasets
        
        if len(data) <= 500:
            train = 60
            test = 40
        elif len(data) > 500 and row_len <= 10000:
            train = 70
            test = 30
        elif len(data) > 10000 and row_len <=100000:
            train = 75
            test = 25
        else:
            train = 80
            test = 20
        print 'train:',train, 'test:',test


        # drops all NAN values from data
        non_nandata = data[~np.isnan(data).any(axis=1)]

        #print non_nandata.shape

        #print non_nandata.shape



        ### nan dataframe
        nan_data = data[np.isnan(data).any(axis = 1)]
        #print nan_data

        #####split  Nan data and non_nandata using the split ratio
        #####determined above




        int_train = (train/float(100))
        #print int_train

        ##split Nan data to train and test sets

        train_nan_data = nan_data[:int(train/float(100)*len(nan_data)), :]
        test_nan_data = nan_data[int(train/float(100)*len(nan_data)):, :]
        #print train_nan_data.shape
        #print test_nan_data.shape



        ##split non Nan data to train and test sets
        train_non_nan = non_nandata[:int(train/float(100)*len(non_nandata)), :]
        test_non_nan =  non_nandata[int(train/float(100)*len(non_nandata)):, :]
        #print train_non_nan.shape
        #print test_non_nan.shape







        ####Add train_non_nan and train_nan_data

        final_train = np.concatenate([train_non_nan, train_nan_data])
        #print final_train.shape



        #### Add test_non_nan and test_nan_data

        final_test = np.concatenate([test_non_nan, test_nan_data])
        #print final_test.shape




        ##This module prints out the train and test data as per the preset ratio
        ## determined based on the length of the data and includes missing data
        ## uniformly between train and test data
        print "This is the final train data:"\
                ,final_train
        print "This is the final test data:" \
            , final_test

    test_train()










