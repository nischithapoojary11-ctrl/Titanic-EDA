from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
import json

app = Flask(__name__)

# ==========================================
# LOAD TITANIC DATASET
# ==========================================

df = pd.read_csv("train.csv")


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    # --------------------------------------
    # BASIC STATISTICS
    # --------------------------------------

    total_passengers = len(df)

    survivors = int(df["Survived"].sum())

    not_survived = total_passengers - survivors

    survival_rate = round(
        (survivors / total_passengers) * 100,
        2
    )


    # ======================================
    # 1. SURVIVAL DISTRIBUTION
    # ======================================

    survival_data = (
        df["Survived"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    survival_data.columns = [
        "Survived",
        "Count"
    ]

    survival_data["Status"] = survival_data[
        "Survived"
    ].map({
        0: "Did Not Survive",
        1: "Survived"
    })


    fig_survival = px.bar(
        survival_data,
        x="Status",
        y="Count",
        text="Count",
        title="Survival Distribution"
    )

    fig_survival.update_traces(
        textposition="outside"
    )

    fig_survival.update_layout(
        template="plotly_white",
        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        ),
        font=dict(
            family="Arial",
            size=13
        )
    )

    survival_chart = json.dumps(
        fig_survival,
        cls=plotly.utils.PlotlyJSONEncoder
    )


    # ======================================
    # 2. SURVIVAL BY GENDER
    # ======================================

    gender_data = (
        df.groupby(
            ["Sex", "Survived"]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )

    gender_data["Status"] = gender_data[
        "Survived"
    ].map({
        0: "Did Not Survive",
        1: "Survived"
    })


    fig_gender = px.bar(
        gender_data,
        x="Sex",
        y="Count",
        color="Status",
        barmode="group",
        text="Count",
        title="Survival by Gender"
    )

    fig_gender.update_traces(
        textposition="outside"
    )

    fig_gender.update_layout(
        template="plotly_white",
        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        )
    )

    gender_chart = json.dumps(
        fig_gender,
        cls=plotly.utils.PlotlyJSONEncoder
    )


    # ======================================
    # 3. SURVIVAL BY PASSENGER CLASS
    # ======================================

    class_data = (
        df.groupby(
            ["Pclass", "Survived"]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )

    class_data["Status"] = class_data[
        "Survived"
    ].map({
        0: "Did Not Survive",
        1: "Survived"
    })


    class_data["Pclass"] = (
        "Class "
        + class_data["Pclass"].astype(str)
    )


    fig_class = px.bar(
        class_data,
        x="Pclass",
        y="Count",
        color="Status",
        barmode="group",
        text="Count",
        title="Survival by Passenger Class"
    )

    fig_class.update_traces(
        textposition="outside"
    )

    fig_class.update_layout(
        template="plotly_white",
        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        )
    )

    class_chart = json.dumps(
        fig_class,
        cls=plotly.utils.PlotlyJSONEncoder
    )


    # ======================================
    # 4. AGE DISTRIBUTION
    # ======================================

    age_data = df.dropna(
        subset=["Age"]
    )


    fig_age = px.histogram(
        age_data,
        x="Age",
        nbins=30,
        title="Age Distribution"
    )

    fig_age.update_layout(
        template="plotly_white",
        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        ),
        xaxis_title="Age",
        yaxis_title="Number of Passengers"
    )


    age_chart = json.dumps(
        fig_age,
        cls=plotly.utils.PlotlyJSONEncoder
    )


    # ======================================
    # 5. FARE DISTRIBUTION
    # ======================================

    fare_data = df.dropna(
        subset=["Fare"]
    )


    fig_fare = px.histogram(
        fare_data,
        x="Fare",
        nbins=30,
        title="Fare Distribution"
    )

    fig_fare.update_layout(
        template="plotly_white",
        margin=dict(
            l=50,
            r=30,
            t=70,
            b=50
        ),
        xaxis_title="Fare",
        yaxis_title="Number of Passengers"
    )


    fare_chart = json.dumps(
        fig_fare,
        cls=plotly.utils.PlotlyJSONEncoder
    )


    # ======================================
    # SEND DATA TO HTML
    # ======================================

    return render_template(
        "index.html",

        total_passengers=total_passengers,

        survivors=survivors,

        not_survived=not_survived,

        survival_rate=survival_rate,

        survival_chart=survival_chart,

        gender_chart=gender_chart,

        class_chart=class_chart,

        age_chart=age_chart,

        fare_chart=fare_chart
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )