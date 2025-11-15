from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)
CSV_FILE = 'database.csv'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        phone = request.form.get("phone")
        address = request.form.get("address")
        postal_code = request.form.get("postal_code")

        # Check if file exists to determine if we need to write headers
        file_exists = os.path.isfile(CSV_FILE)
        
        # Open CSV file in append mode
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['نام و نام خانوادگی', 'شماره تماس', 'آدرس محل سکونت', 'کد پستی']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write header if file is new
            if not file_exists:
                writer.writeheader()
            
            # Write the form data
            writer.writerow({
                'نام و نام خانوادگی': fullname,
                'شماره تماس': phone,
                'آدرس محل سکونت': address,
                'کد پستی': postal_code
            })

        return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)