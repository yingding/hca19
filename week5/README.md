# Packages used for this tutorials:
* tensorflow==1.13.1
* pandas
* matplotlib
<!-- * h5py-->

# (optional) Update pip package installer
If you use the pip3 packagte intaller, you may want to update it with
`sudo -H pip3 install --upgrade pip`

# Install python3 packages in your python3 environment
A requirements.txt file is provided in folder `week5/`
* pip3 user can simply call `pip3 install -r requirements.txt` or install all the packages manually with
 ```console
pip3 install --no-cache-dir pandas matplotlib tensorflow==1.13.1 
```
* conda user need to install all the packages manually with
```console
conda install pandas matplotlib tensorflow==1.13.1
```

# Run this demo in commandline
```console
cd <path>/week5
python3 demo_application.py
```

# Prerequisites
* Python Plugin shall be installed and activated in your Intellij IDEA Utmimate

# Tensorflow Installation
* <a href="https://www.tensorflow.org/install/" target="_blank">Installation Guid of TensorFlow</a>

```console
# using pip3 to install the tensorflow for Python 3.n
pip3 install --upgrade tensorflow
```
Note: the current version of TensorFlow is 1.13.1 on 11.June.2019

* <a href="https://www.tensorflow.org/api_docs/" target="_blank">TensorFlow API r1.13.1</a>

# Approach
* load a CSV dataset and make it available to Keras.
* create a neural network model with Keras for a regression problem.
* use scikit-learn with Keras to evaluate models using cross-validation.
<!-- 
* perform data preparation in order to improve skill with Keras models.
* tune the network topology of models with Keras.
-->

# How to use this example?
<!-- * run the fetch_data.py to fetch data --> 
* run the application.py to run the example (data will be fetched automatically)

# Add Virtual Environment IntelliJ Utimate 2018.1
* https://www.jetbrains.com/help/idea/2018.1/creating-virtual-environment.htmll

# Interactive Code Running in IntelliJ
* Menu -> Tools -> Python Console...
* Select the section of code that shall be run in the Python Console and press `shift + alt + E`
* Show the variables in the Python Console while press the sixth button from the toolbar positioned on the left side of the Python Console
Note: debugging will achieve the same effect

**Alternatively**: you can select the code and with the right mouse click on the code selection with "Execute Selection in Console" action.
![Run Part of Code in Python Console](docs/executePartOfCodes.png)


# Change Logs 
* Since the __file__ can not be recognized by the interactive shell, refered to <a href="https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined" target="_blank">this stackoverflow reference</a>. The __file__ is not anymore used in the `application.py`.

# Issues
* while using the virtual environment, the virtual env shall also be added to the SDK of IntelliJ and this virtual env shall be choosen in the project structure settings of the particular IntelliJ project

# Resources
* Example of Building Regression Model with Tensorflow Core https://www.tensorflow.org/tutorials/keras/basic_regression
* https://medium.com/@robertjohn_15390/simple-housing-price-prediction-using-neural-networks-with-tensorflow-8b486d3db3ca
* https://anujdutt9.github.io/LinearRegressionTF.html



