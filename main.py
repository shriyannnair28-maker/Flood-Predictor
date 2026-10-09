#FLOOD PREDICTOR - AQUA_ALERT - by Shriyann Nair
#AI/ML Based flood risk prediction & early warning prototype
#Using PYTHON + MYSQL + ML

#Importing necessary modules:
import os
import mysql.connector as mys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ==============================
# MACHINE LEARNING MODEL
# ==============================

# Loading the flood dataset
data = pd.read_csv("data/flood_risk_dataset_india.csv")

# Selecting the features used by the ML model
X = data[[
    "Rainfall (mm)",
    "Humidity (%)",
    "Water Level (m)",
    "Historical Floods"
]]

# Selecting what we want the model to predict
y = data["Flood Occurred"]
print("Flood Occurred values:")
print(y.value_counts())
print()
print("Average values for each flood outcome:")
print(data.groupby("Flood Occurred")[[
    "Rainfall (mm)",
    "Humidity (%)",
    "Water Level (m)",
    "Historical Floods"
]].mean())
print()

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Creating the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Training the model
model.fit(X_train, y_train)

# Checking the model accuracy
accuracy = model.score(X_test, y_test)

print("AI/ML model loaded successfully!")
print("ML Model Accuracy:", round(accuracy * 100, 2), "%")
print()


#Project name
print('===============================================')
print('               FLOOD PREDICTOR                 ')
print('===============================================')
 
 #Inputting details from user:

rainfall=float(input('Enter amount of rainfall(mm)'))
humidity=float(input('Enter amount of humidity (%)'))
water_level = float(input("Enter water level (m): "))
historical_floods = int(input("Historical floods? (1 = Yes, 0 = No): "))

#Show user the entered details:
print()
print()
print("Data received successfully!")
print("Rainfall:", rainfall, "mm")
print("Humidity:", humidity, "%")
print("Water Level:", water_level, "m")
if historical_floods==0:
    print('historical floods = No')
elif historical_floods==1:
    print('historical floods = Yes')
else:
    print('historical floods = Invalid entry!!')
print()
print()

#Making situations for the user to see:
#Creating a score for each component so that the complexity of the project reduces

#Rainfall
rainfall_score=0
if rainfall<20:
    rainfall_score=0
elif 20<=rainfall<=50:
    rainfall_score=1
elif rainfall>50:
    rainfall_score=2

#Water level
waterlevel_score=0
if water_level<1:
    waterlevel_score=0
elif 1<=water_level<=2:
    waterlevel_score=1
elif water_level>2:
    waterlevel_score=2

#Humidity
humidity_score=0
if humidity<50:
    humidity_score=0
elif 50<=humidity<=80:
    humidity_score=1
elif humidity>80:
    humidity_score=2

#Historical floods
historicalfloods_score=0
if historical_floods==0:
    historicalfloods_score=0
elif historical_floods==1:
    historicalfloods_score=1

#Scoring system to evaluate
total=rainfall_score+waterlevel_score+humidity_score+historicalfloods_score

#Creating a function Total_risk to calculate risk level:
#Returning the value so that it can be used in the future for further calculations
def Total_risk(tr):
    if 0<=tr<=2:
        c='The risk of flood is 🟢 VERY LOW'
        return c
    elif 3<=tr<=4:
        c='The risk of flood is 🟡 MODERATE'
        return c
    elif 5<=tr<=6:
        c='The risk of flood is 🟠 HIGH'
        return c
    elif 6<tr<=7:
        c='The risk of flood is 🔴 VERY HIGH'
        return c

#Showing the user RISK LEVEL:
if historical_floods==0 or historical_floods==1:
    print(Total_risk(total))
    print('Please note the following precaution steps for your safety')
else:
    print()
    print('Cannot calculate flood risk level due to invalid input of historical flood value')
    print()
    print('Restarting program to enter correct value...')
    print()
    os.system('python main.py') #Added this function so that the program restarts so that the user can enter the correct value
    exit() #Added exit() as if user enters wrong value,the python program doesn't add this to the MySQL table
print()

#Displaying user precaution steps to take for different situations:
#Note:All precaution steps are taken from https://www.redcross.org/ :
if 0<=total<=2:
    print('PRECAUTION STEPS:\n1.Continue normal monitoring of local weather conditions.\n2.Stay aware of changes in rainfall and water levels.\n3.Keep basic emergency information accessible.\n4.Follow local authorities if conditions change.')
elif 3<=total<=4:
    print('PRECAUTION STEPS:\n1.Monitor local weather and flood updates regularly.\n2.Keep an emergency kit and important supplies ready.\n3.Know your local evacuation route and higher-ground locations.\n4.Follow instructions from local authorities if a warning is issued.')
elif 5<=total<=6:
    print('PRECAUTION STEPS:\n1.Stay updated with official weather and flood warnings.\n2.Be prepared to evacuate quickly if authorities advise it.\n3.Move toward higher ground if flooding becomes imminent.\n4.Do not walk or drive through floodwater.')
else:
    print('PRECAUTION STEPS:\n1.Follow official evacuation instructions immediately.\n2.Move to higher ground and stay there when flooding threatens.\n3.Stay away from floodwater and flooded roads.\n4.Do not return to an evacuated area until officials say it is safe')

# ==============================
# AI/ML FLOOD PREDICTION
# ==============================

# Giving the user's data to the ML model
user_data = pd.DataFrame([[
    rainfall,
    humidity,
    water_level,
    historical_floods
]], columns=[
    "Rainfall (mm)",
    "Humidity (%)",
    "Water Level (m)",
    "Historical Floods"
])

# Making the prediction
prediction = model.predict(user_data)

if prediction[0] == 1:
    print("AI/ML Prediction: FLOOD DETECTED")
else:
    print("AI/ML Prediction: NO FLOOD DETECTED")

print()
#=========================================================================================================================================================================================

#Creating connection between MySQL and python:(This is done because the MySQL table is the database part of AQUA_ALERT, which can be used by ML(machine learning) for calculating prediction)
#Note: In GitHub, MySQL doesn't start on its own. So in the terminal box type command - 'sudo service mysql start'

mycon=mys.connect(host='localhost',user='root',password='DRAGON',database='aqua_alert')
mycursor=mycon.cursor()
#The name of the table used is 'FLOODUSER_INPUT' and the database used is 'aqua_alert'
query="INSERT INTO FLOODUSER_INPUT (Rainfall,Humidity,Water_Level,Historical_Floods,FLOODRISK) VALUES({},{},{},{},'{}')".format(rainfall,humidity,water_level,historical_floods,Total_risk(total))
mycursor.execute(query)
mycon.commit()
print('The record entered by the user is successfully saved for future predictions!')
mycursor.close()
mycon.close()