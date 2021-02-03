from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#pymongo with flask to establish mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():

    mars = mongo.db.mars

    mars_info = scrape_mars.scrape()

    mars.update({}, mars_info, upsert=True)

    #redirect to homepage
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
