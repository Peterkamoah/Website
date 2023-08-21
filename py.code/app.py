from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Set up the home page
@app.route("/")
def home():
    return render_template("home.html")

# Set up the logic gates page
@app.route("/logic_gates")
def logic_gates_page():
    return render_template("logic_gates.html", logic_gates=logic_gates)

# Set up the questions page
@app.route("/questions", methods=["GET", "POST"])
def questions_page():
    if request.method == "POST":
        score = 0
        for question in questions:
            if request.form[question["question"]] == question["answer"]:
                score += 1
        return render_template("score.html", score=score)
    else:
        return render_template("questions.html", questions=questions)

# Set up the score page
@app.route("/score")
def score_page():
    return render_template("score.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
