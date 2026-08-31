# 🚢 Titanic EDA Analytics

An interactive **Titanic Exploratory Data Analysis (EDA) website** built using **Python, Flask, Pandas, and Plotly**.

The project explores the Titanic passenger dataset and presents important survival patterns through an interactive web dashboard.

---

## 📌 Project Overview

The Titanic EDA Analytics project analyzes passenger information to understand the factors associated with passenger survival.

The dataset contains information such as:

- Passenger class
- Gender
- Age
- Fare
- Number of siblings/spouses
- Number of parents/children
- Embarkation point
- Survival status

The analysis is presented through an interactive Flask web application with Plotly visualizations.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze the Titanic passenger dataset.
- Understand overall survival patterns.
- Compare survival between male and female passengers.
- Analyze survival across different passenger classes.
- Study passenger age distribution.
- Explore fare distribution.
- Present EDA results through an interactive website.
- Create a simple and professional analytics dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming language |
| 🌐 Flask | Web application framework |
| 🐼 Pandas | Data processing and analysis |
| 📊 Plotly | Interactive data visualization |
| HTML | Website structure |
| CSS | Website styling |
| Jupyter Notebook | Exploratory data analysis |

---

## 📊 Dashboard Features

The web dashboard currently provides:

### 👥 Dataset Overview

Displays important summary statistics:

- **891** Total Passengers
- **342** Survivors
- **549** Did Not Survive
- **38.38%** Survival Rate

### 📈 Interactive Visualizations

The dashboard includes:

1. **Survival Distribution**
   - Compares passengers who survived and did not survive.

2. **Survival by Gender**
   - Compares survival outcomes between male and female passengers.

3. **Survival by Passenger Class**
   - Shows survival patterns across first, second, and third class.

4. **Age Distribution**
   - Displays the distribution of passenger ages.

5. **Fare Distribution**
   - Shows the distribution of passenger fares.

---

## 🔍 Key Analysis Areas

The project focuses on understanding relationships between survival and:

- Gender
- Passenger class
- Age
- Fare
- Family-related information
- Embarkation point

These variables help identify patterns in the Titanic passenger data.

---

## 📁 Project Structure

```text
Titanic-EDA/
│
├── app.py
│
├── train.csv
│
├── Titanic-EDA (2).ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
