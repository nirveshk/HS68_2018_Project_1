
import numpy as np






class data_split:
    """
    Create class data_split to predict a perfect train and test data split ratio.

    define methods to accomplish this task.

    return a split ratio.

    Identify Missing values as Nan, return train and test data with uniform division
    of NAN between train and test data per the data split ratio.

    """
    def __init__(self, data):
        self.data = data


    def test_train():
        """
        Reads in csv file using np.genfromtxt, counts number of NANs in the dataset

        """

        data = np.genfromtxt('heart.csv', delimiter=',', skip_header=1)
        #print np.isnan(data).sum() #counts the number of "NANs" in dat
        print data.shape


        #set calculation standard for specific datalengths
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

        print non_nandata.shape

        ### nan dataframe
        nan_data = data[np.isnan(data).any(axis = 1)]
        #print nan_data

        #####split  Nan data and non_nandata using the split ratio
        #####determined above

        # train_nan_data = nan_data[:train, :]
        # test_nan_data = nan_data[train:, :]
        # print train_nan_data.shape
        # print test_nan_data


        ##split non Nan data to train and test sets
        train_non_nan = non_nandata[:train, :]
        test_non_nan =  non_nandata[train:, :]
        #print train_non_nan
        ##split Nan data to train and test sets

        train_nan = train/100 *(len(nan_data))
        test_nan = test/100 *(len(nan_data))
        #print train_nan

        ####Add train_non_nan and train_nan

        #np.concatenate(train_non_nan, train_nan)

        #train_non_nan.append(train_nan)

        #### Add test_non_nan and test_nan



        #final_train_dataframe
        #final_test-dataframe

    test_train()










