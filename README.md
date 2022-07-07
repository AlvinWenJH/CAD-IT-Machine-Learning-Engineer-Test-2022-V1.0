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
## Authors

- [@AlvinWenJH](https://github.com/AlvinWenJH)

