#FLOOD PREDICTOR - AQUA_ALERT - by Shriyann Nair
#Python-Based Flood Risk Assessment and Early Warning Prototype.
#Using PYTHON + MYSQL 
#Note : Before running the program, start MySQL in GitHub by typing - 'sudo service mysql start' in terminal:

#Importing necessary modules:
import mysql.connector as mys
import math

#Project name
print('===============================================')
print('               FLOOD PREDICTOR                 ')
print('===============================================')
 
#Inputting details from user:

#Input and validate rainfall:
while True:
    try:
        rainfall = float(input('Enter amount of rainfall (mm):'))
        if not math.isfinite(rainfall):
            print('Invalid input! Please enter a valid number.')
            continue

        if rainfall<0:
            print('Invalid input! Rainfall cannot be negative.')
        else:
            break

    except ValueError:
        print('Invalid input! Please enter a number.')

#Input and validate humidity:
while True:
    try:
        humidity = float(input('Enter amount of humidity (%):'))

        if not math.isfinite(humidity):
            print('Invalid input! Please enter a valid number.')
            continue

        if humidity<0 or humidity>100:
            print('Invalid input! Humidity must be between 0 and 100.')
        else:
            break

    except ValueError:
        print('Invalid input! Please enter a number.')

#Input and validate water level:
while True:
    try:
        water_level = float(input('Enter water level (m):'))

        if not math.isfinite(water_level):
            print('Invalid input! Please enter a valid number.')
            continue

        if water_level<0:
            print('Invalid input! Water level cannot be negative.')
        else:
            break

    except ValueError:
        print('Invalid input! Please enter a number.')
#Input and validate historical floods:
while True:
    historical_floods = input('Historical floods? (1 = Yes, 0 = No):')

    if historical_floods == '0' or historical_floods == '1':
        historical_floods = int(historical_floods)
        break
    else:
        print('Invalid input! Please enter 1 or 0.')

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
    if tr<=2:
        c='The risk of flood is 🟢 VERY LOW'
        return c
    elif tr<=4:
        c='The risk of flood is 🟡 MODERATE'
        return c
    elif tr<=6:
        c='The risk of flood is 🟠 HIGH'
        return c
    elif tr<=7:
        c='The risk of flood is 🔴 VERY HIGH'
        return c

#Showing the user RISK LEVEL:
print('The risk level is:')
print(Total_risk(total))
print()
print()

#Displaying user precaution steps to take for different situations:
#Note:All precaution steps are taken from https://www.redcross.org/ :
if total<=2:
    print('PRECAUTION STEPS:')
    print('1.Continue normal monitoring of local weather conditions.')
    print('2.Stay aware of changes in rainfall and water levels.')
    print('3.Keep basic emergency information accessible.')
    print('4.Follow local authorities if conditions change.')

elif total<=4:
    print('PRECAUTION STEPS:')
    print('1. Monitor official weather and flood updates regularly.')
    print('2. Keep emergency supplies ready.')
    print('3. Know your evacuation route and higher-ground locations.')
    print('4. Follow local authority instructions.')

elif total<=6:
    print('PRECAUTION STEPS:')
    print('1. Follow official weather and flood warnings.')
    print('2. Be prepared to evacuate if authorities advise it.')
    print('3. Move to higher ground if flooding threatens.')
    print('4. Never walk or drive through floodwater.')

else:
    print('PRECAUTION STEPS:')
    print('1. Follow official evacuation instructions.')
    print('2. Move to higher ground if flooding threatens.')
    print('3. Stay away from floodwater and flooded roads.')
    print('4. Wait for officials to confirm it is safe to return.')

#=========================================================================================================================================================================================

# Connect Python with MySQL

mycon=mys.connect(host='localhost',user='root',password='YOURPASSWORD',database='aqua_alert')
# Enter your own MySQL password below before running the program
mycursor=mycon.cursor()

#The name of the table used is 'FLOODUSER_INPUT' and the database used is 'aqua_alert'
# Save user inputs and calculated risk

query="INSERT INTO FLOODUSER_INPUT (Rainfall,Humidity,Water_Level,Historical_Floods,FLOODRISK) VALUES({},{},{},{},'{}')".format(rainfall,humidity,water_level,historical_floods,Total_risk(total))
mycursor.execute(query)
mycon.commit()
print()
print('The record entered by the user is successfully saved for future reference!')
mycursor.close()
mycon.close()

#===============================================================================================================================================================================================