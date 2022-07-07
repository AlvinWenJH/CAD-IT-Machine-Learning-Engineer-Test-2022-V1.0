
# CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0

This is my work on the CAD-IT Assessment 


## Analysis

### Q1 - Faulty Check 

In this problem, data about the Temperature and Vibration of two chiller pumps was given in [**Q1.csv**](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/Q1.csv).
The columns of the data are :

* **Timestamp**	 : datetime
* **CHP1Temp1(Deg C)** : float
* **CHP1Temp2(Deg C)** : float
* **CHP2Temp1(Deg C)** : float
* **CHP2Temp2(Deg C)** : float
* **CHP1Vib1(mm/s)** : float	
* **CHP1Vib2(mm/s)** : float
* **CHP2Vib1(mm/s**) : float	
* **CHP2Vib2(mm/s)** : float	
* **Fault** : bool, where 0 means Not Faulty and 1 means Faulty

#### EDA
To visualize the **balancy** of the label (Fault), we can make use of the Matplotlib's histogram plot.
<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/BalancyHist.png" width="480">
    <br>
</p>
<br>

From the picture above we can see that the Faulty data is less than the Not Faulty data but beacuse it is not significant, this might not affect the accuracy of the test prediction. 
On the other hand to ensure that the model can learn, we can simply check the importance of each features using Matplotlib's scatter plot as shown in the figure below.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/Features.png" width="720">
    <br>
</p>
<br>

From each of the scatter plots, we can see there are indeed some important features like the second chiller's vibrations and temperatures. This can be seen by inspecting which plot's x-axis value doesn't have 2 values (Faulty & Not Faulty).
These features existence will help the model learn to classify much easier. One more thing that should be mentioned is there are still missing data for certain range of temperatures or vibration. This means that there will be some range in the input variable which will not have good predicting accuracy. This problem can be solve by collecting more data.

#### Training 
In this work, I train the typical RandomForest and MLP model that was said to perform well in predicting tabular data. The library used for training these models is Sklearn.

* RandomForestClassifier(n_estimator=100)
* MLPClassifier(max_iter=100)
Both of the models gives similar accuracies at around **99.952 %**

The app made can be downloaded at [this link](https://drive.google.com/drive/folders/1kGoras_T30VTshLlvlUd8HpffhnaPlpo?usp=sharing). Below are the preview of the app.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/Q1app.png" width="360">
    <br>
</p>
<br>

**NB** : Please download the whole folder to run the app.

### Q2 - Extracting Data from PDF to excel

The data that should be extracted are Description, Possible root cause and page number from the [Q2.pdf](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/Q2.pdf).
To extract all the information, the library Tabula-py and PyPDF2 were utilized. Sample of the output data can be seen in the figure below.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/dfSample.png" width="720">
    <br>
</p>
<br>

The app made can be downloaded at [this link](https://drive.google.com/drive/folders/1kGoras_T30VTshLlvlUd8HpffhnaPlpo?usp=sharing). Below are the preview of the app.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/Q2app.png" width="360">
    <br>
</p>
<br>



### Q3 - Text Classifying

In this problem, labeled text data are given in the [Q3](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/tree/main/Q3) folder. This folder contains many txt files and each txt files contains many lines of labeled sentences. Below is the description of the label given.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/labeldesc.png" width="720">
    <br>
</p>
<br>

By splitting the lines using the label as delimiters by specifying `max_split=1` , the dataframe obtained was as below with 3117 rows and 2 columns (texts and labels).

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/textSample.png" width="480">
    <br>
</p>
<br>

By vectorizing all the data using Tensorflow, we then get a vector of numbers that represent all the words in data. This steps are just like storing vocab into our dictionary. After that the vectorized text then was encoded using One-Hot Encoding method from the Sklearn library.

The model itself was build by using the Keras Sequential API. The layers that was included in the architecture are Embedding, Bidirectional LSTM, and Dense layers. The model then compiled using Adam optimizer and CategoricalCrossEntropy loss. Lastly, the model was trained by using validation split of 80:20 for 10 epoch. Below are the plots of the training history.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/TrainingHistory.png" width="720">
    <br>
</p>
<br>

From the figures above it can be seen that the training was stopped before overfitting and the accuracy acquired was at 84.46 %.

The app made can be downloaded at [this link](https://drive.google.com/drive/folders/1kGoras_T30VTshLlvlUd8HpffhnaPlpo?usp=sharing). Below are the preview of the app.

<br>
<p align="center">
    <img src="https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/images/Q3app.png" width="360">
    <br>
</p>
<br>

**NB** : Please download the whole folder to run the app.


## Training

All the source code for training the model can be accessed from the [Q1.ipynb](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/Q1.ipynb), [Q2.ipynb](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/Q2.ipynb) and [Q3.ipynb](https://github.com/AlvinWenJH/CAD-IT-Machine-Learning-Engineer-Test-2022-V1.0/blob/main/Q3.ipynb)


## Authors

- [@AlvinWenJH](https://github.com/AlvinWenJH)

