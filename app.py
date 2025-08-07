from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Koneksi ke MySQL RDS
db = mysql.connector.connect(
    host="uts-kesehatan.c9aqqc8kmvd6.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="12345678",
    database="utskesehatan"
)

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT name, price, image_url FROM products")
    products = cursor.fetchall()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
