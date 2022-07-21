from flask import Flask , render_template, request
from templates.model import weight_estimate

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def hello():
    if request.method == "POST":
        Species = request.form["Species"]
        Length  = request.form["Length"]
        Height  = request.form["Height"]
        Width   = request.form["Width"]
        
    return render_template("index.html")
    

@app.route("/subb", methods = ["POST","GET"])
def sub():
    if request.method == "POST":
        try:
            Species = request.form["Species"]
            Length  = request.form["Length"]
            Height  = request.form["Height"]
            Width   = request.form["Width"]
            prediction = weight_estimate(Species, Length ,Height, Width)
        except ValueError:
            return render_template("index.html")

    return render_template("sub.html", prediction = prediction )

    
    


if __name__ == "__main__":
    app.run(debug=True)

