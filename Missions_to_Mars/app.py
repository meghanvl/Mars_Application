from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#pymongo with flask to establish mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

mars_info = {}

@app.route("/")
def home():

    mars_data = mongo.db.mars_data.find_one()

    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():

    mars_data = mongo.db.mars_data
    mars_info["news"] = scrape_mars.scraped_news()
    mars_info['facts'] = scrape_mars.scraped_facts()
    mars_info['hemispheres'] = scrape_mars.scraped_hemispheres()
    mars_data.update({}, mars_info, upsert=True)

    #redirect to homepage
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


#     {
        
#         "NEWS":{"news_title": news_date,
#         p}
#         ,
#         "FACTS":{'scraped facts': facts}
# ,
#     "HEMISOPHERES":{'hemis':hemispheres}
    
    
#     }
#     data['NEWS']['News_title'][1]