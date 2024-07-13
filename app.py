from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        expression = request.form.get("display")

        try:
            result = str(eval(expression))
        except Exception:
            result = "Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
