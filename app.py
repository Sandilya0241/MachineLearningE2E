import pandas as pd
import numpy as np
from flask import Flask,request,render_template
from src.pipelines.predict_pipeline import StudentData,PredictPipeline

application=Flask(__name__)


###
# 
# Route for home page
# 
# ###
@application.route("/")
def index():
    return render_template('index.html')


###
# 
# Function to predict the output
# 
# ###
@application.route("/predictdata",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("Home.html")
    else:
        stud_dt=StudentData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race_ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score"))
        )
        features_df=stud_dt.get_data_as_data_frame()
        pred_ppl=PredictPipeline(features_df)
        results=pred_ppl.predict()
        return render_template("Home.html", results=results)


if __name__=="__main__":
    application.run(host="0.0.0.0", debug=True)