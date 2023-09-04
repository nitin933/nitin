from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")


@app.route("/predict", methods=["GET"])
def predict():
    # user input
    Inflation= float(request.args.get("Inflation"))
    Unemployment_rate = float(request.args.get("Unemployment_Rate"))
    Federal_Funds= float(request.args.get("Federal_Funds"))
    Consumer_Confidence_Index= float(request.args.get("Consumer_Confidence_Index"))
    Market_Cap_to_GDP= float(request.args.get("Market_Cap_to_GDP"))
    Average_T10Y3M= float(request.args.get("Average_T10Y3M"))
    Housing_Price= float(request.args.get("Housing_Price"))
    Debt_to_GDP= float(request.args.get("Debt_to_GDP"))
    Manufacturing_Output= float(request.args.get("Manufacturing_Output"))
    M2V= float(request.args.get("M2V"))


    import pickle
    model_file = open("recession_model.pk", "rb")
    model= pickle.load(model_file)
    model_file.close()
    recession = model.predict([[Inflation,Unemployment_rate,Federal_Funds,Consumer_Confidence_Index,Market_Cap_to_GDP,Average_T10Y3M,Housing_Price,Debt_to_GDP,Manufacturing_Output,M2V]])
    if recession[0] == 1:
        return render_template("index_1_prediction_yes.html")
    else:
        return render_template("index_0_prediction_no.html")


app.run(port=8080, debug=True, host="0.0.0.0")