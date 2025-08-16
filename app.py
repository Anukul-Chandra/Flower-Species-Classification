from flask import request,Flask,jsonify,render_template
import numpy as np
import pickle
app = Flask(__name__)


# Load the model
model = pickle.load(open("finalized_model.pkl", "rb"))

# Get request
@app.route("/")
def home():
    result =''
    return render_template("index.html", **locals())



@app.route("/predict", methods=["POST", "GET"])
def prediict():
    if request.method == "POST":
        sepal_length = float(request.form.get("sepal_length"))
        sepal_width = float(request.form.get("sepal_width"))
        petal_length = float(request.form.get("petal_length"))
        petal_width = float(request.form.get("petal_width"))
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

        if result == 0:
            result = 'Iris Setosa'
        elif result == 1:
            result = 'Iris Versicolor'
        elif result == 2:
            result = 'Iris Virginica'   
    else:
        result = ''
    return render_template("index.html", **locals())




# Post request
@app.route("/post", methods=["POST"])
def post():
    name  = request.form.get("name")
    age = request.form.get("age")

    return jsonify({'message' : f'Hello {name}, you are {str(age)} years old!'})


if __name__ == "__main__":
    app.run(debug=True)
