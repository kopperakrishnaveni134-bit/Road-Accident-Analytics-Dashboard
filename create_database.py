import sqlite3
import csv

conn = sqlite3.connect("accidents.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS accidents")

cursor.execute("""
CREATE TABLE accidents(
    id INTEGER,
    location TEXT,
    road_cases INTEGER,
    road_injured INTEGER,
    road_died INTEGER,
    railway_cases INTEGER,
    railway_injured INTEGER,
    railway_died INTEGER,
    crossing_cases INTEGER,
    crossing_injured INTEGER,
    crossing_died INTEGER,
    total_cases INTEGER,
    total_injured INTEGER,
    total_died INTEGER
)
""")

count = 0

with open("accidents_data.csv", "r", encoding="utf-8-sig") as file:

    reader = csv.DictReader(file)

    print("CSV Columns:", reader.fieldnames)

    for row in reader:

        try:
            if not row["Sl. No."].isdigit():
                continue

            cursor.execute("""
            INSERT INTO accidents VALUES
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                int(row["Sl. No."]),
                row["State/UT/City"],
                int(row["Road Accidents - Cases"]),
                int(row["Road Accidents - Injured"]),
                int(row["Road Accidents - Died"]),
                int(row["Railway Accidents - Cases"]),
                int(row["Railway Accidents - Injured"]),
                int(row["Railway Accidents - Died"]),
                int(row["Railway Crossing Accidents - Cases"]),
                int(row["Railway Crossing Accidents - Injured"]),
                int(row["Railway Crossing Accidents - Died"]),
                int(row["Total Traffic Accidents - Cases"]),
                int(row["Total Traffic Accidents - Injured"]),
                int(row["Total Traffic Accidents - Died"])
            ))

            count += 1

        except Exception as e:
            print("Error:", e)
            print(row)

conn.commit()
conn.close()

print(f"{count} rows inserted successfully.")