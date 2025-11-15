from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission here
        fullname = request.form.get("fullname")
        phone = request.form.get("phone")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")
        # You can process the data here
        return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)