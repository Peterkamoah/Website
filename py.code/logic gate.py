from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Set up the logic gates information
logic_gates = [
    {
        "name": "AND Gate",
        "description": "The AND gate is a digital logic gate that has two or more inputs and produces an output that is the logical AND of the inputs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/AND_ANSI.svg/1200px-AND_ANSI.svg.png"
    },
    {
        "name": "OR Gate",
        "description": "The OR gate is a digital logic gate that has two or more inputs and produces an output that is the logical OR of the inputs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/OR_ANSI.svg/1200px-OR_ANSI.svg.png"
    },
    {
        "name": "NOT Gate",
        "description": "The NOT gate is a digital logic gate that has one input and produces an output that is the logical NOT of the input.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NOT_ANSI.svg/1200px-NOT_ANSI.svg.png"
    },
    {
        "name": "NAND Gate",
        "description": "The NAND gate is a digital logic gate that has two or more inputs and produces an output that is the logical NAND of the inputs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/NAND_ANSI.svg/1200px-NAND_ANSI.svg.png"
    },
    {
        "name": "NOR Gate",
        "description": "The NOR gate is a digital logic gate that has two or more inputs and produces an output that is the logical NOR of the inputs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/NOR_ANSI.svg/1200px-NOR_ANSI.svg.png"
    },
    {
        "name": "XOR Gate",
        "description": "The XOR gate is a digital logic gate that has two inputs and produces an output that is the logical XOR of the inputs.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/XOR_ANSI.svg/1200px-XOR_ANSI.svg.png"
    }
]

# Set up the questions
questions = [
    {
        "question": "What is the output of an AND gate if both inputs are 1?",
        "answer": "1"
    },
    {
        "question": "What is the output of an OR gate if both inputs are 0?",
        "answer": "0"
    },
    {
        "question": "What is the output of a NOT gate if the input is 1?",
        "answer": "0"
    },
    {
        "question": "What is the output of a NAND gate if both inputs are 1?",
        "answer": "0"
    },
    {
        "question": "What is the output of a NOR gate if both inputs are 0?",
        "answer": "1"
    },
    {
        "question": "What is the output of an XOR gate if both inputs are 1?",
        "answer": "0"
    }
]

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
        score = 6
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
