from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ---------------------------------------
# Risk Classification
# ---------------------------------------
def classify_risk(cases):

    if cases >= 20000:
        return "High Risk"

    elif cases >= 10000:
        return "Medium Risk"

    else:
        return "Low Risk"


# ---------------------------------------
# Safety Recommendation
# ---------------------------------------
def recommendation(level):

    if level == "High Risk":

        return (
            "Increase traffic police deployment, install speed cameras, "
            "improve road lighting, install warning signs and conduct "
            "road safety awareness programs."
        )

    elif level == "Medium Risk":

        return (
            "Repair damaged roads, enforce speed limits, "
            "install caution boards and monitor accident-prone areas."
        )

    else:

        return (
            "Maintain regular road inspections and encourage "
            "safe driving practices."
        )


# ---------------------------------------
# Load Data From SQLite
# ---------------------------------------
def load_data():

    conn = sqlite3.connect("accidents.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accidents")

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:

        row = dict(row)

        row["Risk_Level"] = classify_risk(
            row["road_cases"]
        )

        row["Recommendation"] = recommendation(
            row["Risk_Level"]
        )

        data.append(row)

    return data


# ---------------------------------------
# Home Page
# ---------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    data = load_data()

    result = None

    # ---------------- Dashboard Statistics ----------------

    total_states = len(data)

    high_risk = sum(
        1 for row in data
        if row["Risk_Level"] == "High Risk"
    )

    medium_risk = sum(
        1 for row in data
        if row["Risk_Level"] == "Medium Risk"
    )

    low_risk = sum(
        1 for row in data
        if row["Risk_Level"] == "Low Risk"
    )

    total_road_cases = sum(
        row["road_cases"] for row in data
    )

    total_injured = sum(
        row["road_injured"] for row in data
    )

    total_deaths = sum(
        row["road_died"] for row in data
    )

    # ---------------- Search ----------------

    if request.method == "POST":

        search = request.form["location"].strip().lower()

        for row in data:

            if row["location"].lower() == search:

                result = row

                break

        if result is None:

            result = "not_found"

    # ---------------- Top 10 Chart ----------------

    sorted_data = sorted(

        data,

        key=lambda x: x["road_cases"],

        reverse=True

    )

    chart_data = sorted_data[:10]

    # Include searched state if not in Top 10

    if result and result != "not_found":

        found = False

        for row in chart_data:

            if row["location"] == result["location"]:

                found = True

                break

        if not found:

            chart_data.pop()

            chart_data.append(result)

    labels = [

        row["location"]

        for row in chart_data

    ]

    cases = [

        row["road_cases"]

        for row in chart_data

    ]    # ---------------- Chart Colors ----------------

    colors = []

    for row in chart_data:

        if (
            result
            and result != "not_found"
            and row["location"] == result["location"]
        ):

            # Highlight searched state
            colors.append("#ef4444")

        else:

            colors.append("#2563eb")


    # ---------------- Map Data ----------------

    map_data = []

    for row in data:

        map_data.append({

            "location": row["location"],

            "road_cases": row["road_cases"],

            "road_injured": row["road_injured"],

            "road_died": row["road_died"],

            "risk": row["Risk_Level"]

        })


    # ---------------- Render Template ----------------

    return render_template(

        "index.html",

        data=data,

        result=result,

        total_states=total_states,

        high_risk=high_risk,

        medium_risk=medium_risk,

        low_risk=low_risk,

        total_road_cases=total_road_cases,

        total_injured=total_injured,

        total_deaths=total_deaths,

        labels=labels,

        cases=cases,

        colors=colors,

        map_data=map_data

    )


# ---------------------------------------
# Run Flask
# ---------------------------------------

if __name__ == "__main__":

    app.run(debug=True)