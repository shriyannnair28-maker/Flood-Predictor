
# 🌊 FLOOD PREDICTOR — AQUA_ALERT

**By Shriyann Nair**

*A Python-Based Flood Risk Assessment and Early Warning Prototype*

## 1. Project Overview

AQUA_ALERT is a Python-based project designed to assess potential flood risk using user-provided environmental information. It evaluates rainfall, humidity, water level, and historical flood occurrence to calculate a risk score and display a corresponding risk category.

The project also provides precautionary recommendations and stores the user's inputs and calculated risk category in a MySQL database for future reference.

AQUA_ALERT was developed to explore how programming, conditional logic, input validation, and database management can be combined to address a real-world environmental concern.

**Note:** This is an educational prototype that uses a rule-based scoring system. It is not a scientifically validated flood-prediction model and does not replace official weather alerts or emergency instructions.

## 2. Project Features

- **User Input:** Accepts rainfall, humidity, water level, and historical flood information.
- **Input Validation:** Checks numerical inputs and rejects invalid or out-of-range values.
- **Risk Assessment:** Calculates a total risk score using predefined rules.
- **Risk Classification:** Displays one of four flood-risk categories.
- **Precautionary Recommendations:** Provides safety suggestions based on the calculated category.
- **MySQL Integration:** Saves user inputs and the resulting risk category in a database.
- **Data Management:** Uses Python and MySQL Connector to communicate with the database.

## 3. Technologies Used

- **Python:** Main programming language used for input handling, validation, calculations, and output.
- **MySQL:** Stores the submitted information and calculated risk category.
- **MySQL Connector/Python:** Connects the Python application to the MySQL database.
- **GitHub Codespaces:** Development and execution environment.

## 4. How the Project Works

1. The user enters rainfall in millimetres, humidity as a percentage, water level in metres, and whether historical floods have occurred.
2. The program validates the inputs.
3. Each environmental factor receives a score according to predefined thresholds.
4. The individual scores are added to calculate the total risk score.
5. The program assigns a flood-risk category based on the total score.
6. Appropriate precautionary recommendations are displayed.
7. The inputs and resulting risk category are saved in MySQL.

## 5. Risk Scoring System

The program assigns scores to four environmental factors using predefined conditions.

| Environmental Factor | Condition | Score |
|---|---|---:|
| Rainfall | Below 20 mm | 0 |
| Rainfall | 20–50 mm | 1 |
| Rainfall | Above 50 mm | 2 |
| Water Level | Below 1 m | 0 |
| Water Level | 1–2 m | 1 |
| Water Level | Above 2 m | 2 |
| Humidity | Below 50% | 0 |
| Humidity | 50–80% | 1 |
| Humidity | Above 80% | 2 |
| Historical Floods | No | 0 |
| Historical Floods | Yes | 1 |

The total score is calculated by adding the four individual scores. The possible total ranges from 0 to 7.

### Risk Categories

| Total Score | Risk Category |
|---|---|
| 0–2 | 🟢 Very Low |
| 3–4 | 🟡 Moderate |
| 5–6 | 🟠 High |
| 7 | 🔴 Very High |

These thresholds were selected as rules for this educational prototype. They have not been scientifically validated and should not be interpreted as official flood-risk thresholds.

## 6. Input Validation

The program uses Python's `try` and `except` statements to handle invalid numerical input.

It also uses conditional statements and loops to ensure that:

- Rainfall cannot be negative.
- Humidity must be between 0 and 100 percent.
- Water level cannot be negative.
- Historical flood input must be either `0` or `1`.
- Non-finite numerical values, such as `NaN` and infinity, are rejected using `math.isfinite()`.

These checks help prevent invalid inputs from interfering with the scoring process.

## 7. Database Integration

AQUA_ALERT uses MySQL to store the records entered by the user.

**Database Name:** `aqua_alert`

**Table Name:** `FLOODUSER_INPUT`

The table stores the following information:

- `Record_ID` — Unique record identifier.
- `Rainfall` — Rainfall entered by the user.
- `Humidity` — Humidity entered by the user.
- `Water_Level` — Water level entered by the user.
- `Historical_Floods` — Historical flood indicator.
- `FLOODRISK` — Calculated flood-risk category.

Python connects to MySQL through `mysql.connector`. After a record is inserted, `mycon.commit()` saves the transaction.

## 8. How to Run the Project

### Requirements

- Python 3
- MySQL Server
- MySQL Connector/Python
- The `aqua_alert` database and `FLOODUSER_INPUT` table

### Step 1: Start MySQL

In the GitHub Codespaces terminal, run:

```bash
sudo service mysql start
```

### Step 2: Install the Connector

If MySQL Connector/Python is not already installed, run:

```bash
pip install mysql-connector-python
```

### Step 3: Prepare the Database

Ensure that the `aqua_alert` database and `FLOODUSER_INPUT` table exist and that their column names and data types match the Python program.

### Step 4: Configure the Database Connection

Update the MySQL connection settings in the Python program for your own environment.

**Security Note:** Never publish your actual database password in a public repository.

### Step 5: Run the Program

Run the Python file from the terminal:

```bash
python main.py
```

Follow the prompts to enter the environmental information. The program will display the risk category and precautions, then attempt to save the record in MySQL.

**Note:** The database service, credentials, database, and table must be configured correctly for the database operation to succeed.

## 9. Safety and Limitations

AQUA_ALERT is an educational prototype, not an operational flood-warning service.

- Its risk categories are based on manually defined rules.
- Its thresholds have not been validated against real flood events.
- It does not use a trained machine-learning model or real-time weather data.
- Its results may not accurately represent actual local flood conditions.
- Its recommendations do not replace official weather warnings, evacuation instructions, or guidance from emergency authorities.

Users should always follow official local emergency and weather guidance.

## 10. Future Improvements

Possible future improvements include:

- Testing and refining the scoring thresholds using reliable historical flood data.
- Adding real-time rainfall and water-level data from trustworthy sources.
- Developing a graphical user interface.
- Improving database record viewing and analysis.
- Evaluating the system against documented flood events before making real-world risk claims.

## 11. Development Journey

This project was developed to strengthen my understanding of Python programming, conditional logic, loops, functions, input validation, and MySQL database integration.

During development, I worked on combining multiple environmental inputs into a scoring system, displaying understandable results, handling invalid entries, and saving records to a database.

The project also helped me recognise the importance of testing, responsible communication of results, and clearly explaining the limitations of a rule-based system.

I used ChatGPT as a learning and troubleshooting aid during development, particularly for guidance on package installation, resolving technical issues, and understanding programming concepts. I tested the project and worked to understand how its components operate.

## 12. Conclusion

AQUA_ALERT demonstrates how basic programming concepts and database management can be combined to build a structured environmental risk-assessment prototype.

The project represents my exploration of programming for real-world problem-solving and provides a foundation for future learning in environmental data analysis and more advanced predictive systems.

---

**Created by Shriyann Nair**

*FLOOD PREDICTOR — AQUA_ALERT*


