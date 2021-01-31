from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#pymongo with flask to establish mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


app = Flask(__name__)

@app.route("/")
def home():

    mars_data = mongo.db.mars_data.find_one()

    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():

    mars_app = scrape_mars.scrape_info()





ir __name__ == "__main__":
    app.run(debug=True)