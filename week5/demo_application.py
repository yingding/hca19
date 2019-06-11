"""
Demo ANN Application for building a regression model for boston housing problem
"""

from tensorflow import keras
import tensorflow as tf
from distutils.version import LooseVersion
import warnings
import os
import pandas as pd
import matplotlib.pyplot as plt


"""
Checking Tensorflow Versions
"""
# Check Tensorflow Version
assert LooseVersion(tf.__version__) >= LooseVersion('1.12'), 'Please use TensorFlow version 1.12 or newer'
print('TensorFlow Version: {}'.format(tf.__version__))

# Check for Tensorflow GPU Support
if not tf.test.gpu_device_name():
    warnings.warn('No GPU found. Please use a GPU to train your neural network.')
else:
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))


"""
Get bosten housing data
"""

def data_file_path() -> str:
    """
    put the download data to <current dir>/data/xxx.data
    :return: data_file_path
    """
    data_dir_path = os.path.join(os.getcwd(), "data")
    if not os.path.exists(data_dir_path):
        # make <current dir>/data dir if not exists
        os.mkdir(data_dir_path)
    return os.path.join(data_dir_path, "housing.data")

# assign housing_data_file_path
housing_data_file_path = data_file_path()

if not os.path.exists(data_file_path()):
    # not housing data exists, downloading
    dataset_path = keras.utils.get_file(data_file_path(), "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data")
else:
    # assign housing data file_path
    dataset_path = housing_data_file_path

# alternatively you can also use the housing data from sklearn
# from sklearn.datasets import load_boston
# bosten = load_boston()

"""
Loading DataFrame
"""
# described in https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names
# column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# print(column_names)
column_desciption_dic = {
    "CRIM": "per capita crime rate by town",
    "ZN" : "proportion of residential land zoned for lots over 25,000 sq.ft.",
    "INDUS" : "proportion of non-retail business acres per town",
    "CHAS" : "Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)",
    "NOX"  : "nitric oxides concentration (parts per 10 million)",
    "RM" : "average number of rooms per dwelling",
    "AGE" : "proportion of owner-occupied units built prior to 1940",
    "DIS" : "weighted distances to five Boston employment centres",
    "RAD" : "index of accessibility to radial highways",
    "TAX" : "full-value property-tax rate per $10,000",
    "PTRATIO" : "pupil-teacher ratio by town",
    "B" :     "1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town",
    "LSTAT" : "% lower status of the population",
    "MEDV" : "Median value of owner-occupied homes in $1000's"
}
column_names = list(column_desciption_dic.keys())

df_raw_dataset = pd.read_csv(dataset_path, names=column_names, delim_whitespace=True)

df_dataset = df_raw_dataset.copy()
print(df_dataset.head(10))

"""
Splitting data into train and test sets
"""
df_train_dataset = df_dataset.sample(frac=0.8, random_state=0)
df_test_dataset = df_dataset.drop(df_train_dataset.index)

train_dataset = df_train_dataset.to_numpy()
# Split into input (X) and output (Y) variables
train_X = train_dataset[:, 0:13]
train_Y = train_dataset[:, 13]

print("shape of train_dataset: ", train_dataset.shape)
print("shape of train_X: ", train_X.shape)
print("shape of train_Y: ", train_Y.shape)

test_dataset = df_test_dataset.to_numpy()
test_X = test_dataset[:, 0:13]
test_Y = test_dataset[:, 13]
print("shape of test_dataset: ", test_dataset.shape)
print("shape of test_X: ", test_X.shape)
print("shape of test_Y: ", test_Y.shape)

''' Opportunity for improvement '''
# you may notice the data in the data set are not normalized
# please refer to https://www.tensorflow.org/tutorials/keras/basic_regression
# to normalize your data, so that the tf model can quickly converge to a local optimum


""" 
define baseline ANN model
"""


def build_baseline_model(input_dim):
    # create sequential model
    local_model = keras.Sequential()
    # hidden layer with kernel_initializer to init the default neuron weights https://keras.io/initializers/
    local_model.add(keras.layers.Dense(13, input_dim=input_dim, kernel_initializer='normal', activation='relu'))
    local_model.add(keras.layers.Dense(1, kernel_initializer='normal'))
    # optimizer
    optimizer = tf.keras.optimizers.Adam();
    # optimizer = tf.keras.optimizers.RMSprop(0.001);

    # Compile model
    local_model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['mean_squared_error'])
    return local_model

''' Opportunity for improvement '''
# It is a simple model that has a single fully connected hidden layer
# with the same number of neurons as input attributes (13).
# The network uses good practices such as the rectifier activation function for the hidden layer.
# No activation function is used for the output layer because it is a regression problem
# and we are interested in predicting numerical values directly without transform.
# You may want to use ANN with more layers and more hidden states and drop out to improve the model

model = build_baseline_model(train_X.shape[1])
model.summary()

"""
First testing of Prediction with Random initialized weights
"""
example_batch = train_X[:10, :]
example_result = model.predict(example_batch)
print("\nPredicted result of random initialized weights:\n", example_result)


"""
Training Model
"""


class PrintDot(keras.callbacks.Callback):
    """Class PrintDot inherent from Class keras.callbacks.Callback """
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0: print('')
        print('.', end='')


EPOCHS = 2000

history = model.fit(train_X, train_Y, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print("\nThe last 10 trainings history:\n")
print(hist.tail(10))


def plot_history(_history):
    _hist = pd.DataFrame(history.history)
    _hist['epoch'] = history.epoch

    plt.close('all')
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('MSE [Boston Housing]')
    plt.plot(_hist['epoch'], _hist['mean_squared_error'], label='Train Error')
    plt.plot(_hist['epoch'], _hist['val_mean_squared_error'], label='Val Error')
    plt.ylim([0, 50])
    plt.legend()
    plt.show()


# plotting training progress
plot_history(history)

''' Opportunity for improvement '''
# No early stop is implemented in this tutorial
# An example of early stop can be found at
# https://www.tensorflow.org/tutorials/keras/basic_regression

"""
Making Test Prediction
"""

loss, mse = model.evaluate(test_X, test_Y, verbose=0)
print("Testing set Mean Squired Error: {:5.2f} x1000$".format(mse))

test_predictions = model.predict(test_X).flatten()


def plot_prediction(_test_predictions, _test_labels):
    plt.close("all")
    plt.scatter(_test_labels, _test_predictions)
    plt.xlabel('True Values [1000$]')
    plt.ylabel('Predictions [1000$]')
    plt.axis('equal')
    plt.axis('square')
    plt.xlim([0, plt.xlim()[1]])
    plt.ylim([0, plt.ylim()[1]])
    # plotting the diagonal line as visual helper
    _ = plt.plot([-100, 100], [-100, 100])
    plt.show()


# The points shall be close to the diagonal line
plot_prediction(test_predictions, test_Y)


def plot_error_distribution(_test_predictions, _test_labels):
    error = _test_predictions - _test_labels
    plt.close("all")
    plt.hist(error, bins = 25)
    plt.xlabel("Predictin Error [1000$]")
    _ = plt.ylabel("Count")
    plt.show()


# expecting to see a gaussian distribution
plot_error_distribution(test_predictions, test_Y)