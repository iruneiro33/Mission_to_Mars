# We'll use Flask to render a template, redirecting to another url and creating a URL
from flask import Flask, render_template, redirect, url_for
# We'll use PyMonto to interact with our Mongo database
from flask_pymongo import PyMongo
# Convert from Jupyter notebook to Python
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = 'mongodb://localhost:27017/mars_app' ## How do I know this number?
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
# allows us to access the database, scrape new data using scraping.py script, update the database, and return a message when successful
def scrape():
    mars = mongo.db.mars #assign a variable that points to Mongo database
    mars_data = scraping.scrape_all() #reference the "scrape_all" function in hte "scraping.py" file from Jupyter Notebook
    mars.update_one({}, {"$set":mars_data}, upsert=True) #After gathering new data, update the database
    #upsert=true -> Mongo to create a new document if one doesn't already exist
    return redirect('/', code=302)
    # navigate our page back to / where we can see the updated content

if __name__ == "__main__":
    app.run()
