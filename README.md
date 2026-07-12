# 🚦 Road Accident Analytics Dashboard

A Flask-based web application that analyzes road accident statistics across Indian States and Union Territories. The dashboard classifies accident-prone areas into different risk levels and visualizes the data using interactive charts and maps.

---

## 📌 Project Overview

The **Road Accident Analytics Dashboard** helps users analyze road accident data by providing:

- State-wise accident statistics
- Risk level classification
- Safety recommendations
- Interactive dashboard
- Bar chart visualization
- Interactive India map

The application uses **SQLite** as the database and **Flask** as the backend framework.

---

## ✨ Features

- 🔍 Search accident statistics by state
- 📊 Dashboard with summary statistics
- 🚦 Automatic Risk Classification
  - High Risk
  - Medium Risk
  - Low Risk
- 💡 Safety recommendations
- 📈 Top 10 accident-prone states (Chart.js)
- 🗺️ Interactive India map (Leaflet.js)
- 💾 SQLite database integration
- 📱 Responsive user interface

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML5
- CSS3
- JavaScript

### Libraries
- Chart.js
- Leaflet.js

---

## 📂 Project Structure

```
Road-Accident-Analytics-Dashboard/
│
├── app.py
├── create_database.py
├── accident_analysis.py
├── accidents.db
├── accidents_data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── tech_bg.jpg
│   └── ...
│
└── README.md
```

---

## 🗄️ Database

The application uses an SQLite database named:

```
accidents.db
```

Main table:

```
accidents
```

Important columns:

- location
- road_cases
- road_injured
- road_died
- railway_cases
- total_cases
- total_died

---

## 🚦 Risk Classification

| Road Accident Cases | Risk Level |
|--------------------|------------|
| ≥ 20,000 | 🔴 High Risk |
| 10,000 – 19,999 | 🟠 Medium Risk |
| < 10,000 | 🟢 Low Risk |

---

## 💡 Safety Recommendations

### High Risk
- Increase traffic police deployment
- Install speed cameras
- Improve road lighting
- Conduct road safety awareness programs

### Medium Risk
- Repair damaged roads
- Enforce speed limits
- Install caution boards

### Low Risk
- Regular road maintenance
- Promote safe driving awareness

---

## 📊 Dashboard

The dashboard displays:

- Total States
- High Risk States
- Medium Risk States
- Low Risk States
- Road Accident Statistics
- Search Results
- Interactive Charts
- Interactive Map

---

## 📈 Data Visualization

### Bar Chart
Displays the Top 10 accident-prone locations using **Chart.js**.

### Interactive Map
Displays accident locations using **Leaflet.js** with risk-level markers.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/kopperakrishnaveni134-bit/Road-Accident-Analytics-Dashboard.git
```

Move into the project

```bash
cd Road-Accident-Analytics-Dashboard
```

Install Flask

```bash
pip install flask
```

Run the application

```bash
python app.py
```

Open in your browser

```
http://127.0.0.1:5000
```

---


## 🎯 Learning Outcomes

Through this project I learned:

- Flask Web Development
- SQLite Database Integration
- HTML & CSS Dashboard Design
- JavaScript
- Chart.js Visualization
- Leaflet Interactive Maps
- Risk Classification Logic
- Git & GitHub Version Control

---

## 👩‍💻 Author

**Krishnaveni Koppera**

GitHub:
https://github.com/kopperakrishnaveni134-bit

---

## ⭐ If you found this project useful, consider giving it a star!
