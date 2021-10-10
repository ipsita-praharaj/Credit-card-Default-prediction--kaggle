from flask import Flask, render_template
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("Home page.html")

@app.route("/rus",methods=["GET"])
def rus():
    return render_template("Modelling_(RUS)_Model_results.html")

@app.route("/adasyn",methods=["GET"])
def adasyn():
    return render_template("Modeling_(ADASYN)_Model_Results.html")

@app.route("/prep",methods=["GET"])
def prep():
    return render_template("Preprocessing & Visualisations.html")


if __name__=="__main__":
    app.run(debug=True)
