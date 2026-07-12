import sqlite3

conn = sqlite3.connect("accidents.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("SELECT * FROM accidents")

rows = cursor.fetchall()

cursor.execute("SELECT MAX(road_cases) FROM accidents")
maximum = cursor.fetchone()[0]


def classify(cases):

    if cases >= maximum * 0.7:
        return "High Risk"

    elif cases >= maximum * 0.4:
        return "Medium Risk"

    return "Low Risk"


for row in rows:

    row = dict(row)

    print("--------------------------------")

    print("Location :", row["location"])
    print("Road Cases :", row["road_cases"])
    print("Risk :", classify(row["road_cases"]))

conn.close()