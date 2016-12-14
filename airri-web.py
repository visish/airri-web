from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/pump/status", methods=["GET","POST"])
def hello():

    return jsonify({"pump":pum_status})

if __name__ == "__main__":
    app.run(debug=True)
