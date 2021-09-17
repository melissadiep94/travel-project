# import dependences
from flask import Flask, render_template, redirect
import pymongo
from natlparks import NatlParks
import json

# Create an instance of Flask
app = Flask(__name__)

# Use PyMOngo to establish Mongo connection
conn = "mongodb://localhost:27017"

#Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

#connect to a database.
db = client.parks_db
collection = db.parks

# Route to render index.html template using data from Mongo
@app.route("/")
@app.route("/index")
def index():
    parks = collection.find_one()
    return render_template("index.html", parks=parks)

# route to find parks by name
@app.route('/name')
def park_names():
    
 names = ["Acadia National Park",
         "Adams National Historical Park",
         "American Memorial Park",
         "Amistad National Recreation Area",
         "Anacostia Park",
         "Arches National Park",
         "Badlands National Park",
         "Baltimore-Washington Parkway",
         "Big Bend National Park",
         "Bighorn Canyon National Recreation Area",
         "Biscayne National Park",
         "Black Canyon Of The Gunnison National Park",
         "Blackstone River Valley National Historical Park",
         "Boston National Historical Park",
         "Bryce Canyon National Park",
         "Cane River Creole National Historical Park",
         "Canyonlands National Park",
         "Capitol Hill Parks",
         "Capitol Reef National Park",
         "Carlsbad Caverns National Park",
         "Catoctin Mountain Park",
         "Channel Islands National Park",
         "Chesapeake & Ohio Canal National Historical Park",
         "Chickamauga & Chattanooga National Military Park",
         "Colonial National Historical Park",
         "Coltsville National Historical Park",
         "Congaree National Park",
         "Crater Lake National Park",
         "Cuyahoga Valley National Park",
         "Death Valley National Park",
         "Dry Tortugas National Park",
         "Everglades National Park",
         "Gateway Arch National Park",
         "Glacier National Park",
         "Grand Canyon National Park",
         "Grand Teton National Park",
         "Great Basin National Park",
         "Great Smoky Mountains National Park",
         "Guadalupe Mountains National Park",
         "HaleakalƒÅ National Park",
         "Harpers Ferry National Historical Park",
         "Harriet Tubman National Historical Park",
         "Hawai Volcanoes National Park",
         "Hot Springs National Park",
         "Independence National Historical Park",
         "Indiana Dunes National Park",
         "Isle Royale National Park",
         "Jimmy Carter National Historical Park",
         "Joshua Tree National Park",
         "Kalaupapa National Historical Park",
         "Kenai Fjords National Park",
         "Keweenaw National Historical Park",
         "Kobuk Valley National Park",
         "Lake Clark National Park & Preserve",
         "Lassen Volcanic National Park",
         "Lowell National Historical Park",
         "Mammoth Cave National Park",
         "Mesa Verde National Park",
         "Mount Rainier National Park",
         "North Cascades National Park",
         "Olympic National Park",
         "Petrified Forest National Park",
         "Pinnacles National Park",
         "Prince William Forest Park",
         "Redwood National and State Parks",
         "Rocky Mountain National Park",
         "Roosevelt Campobello International Park",
         "Saguaro National Park",
         "Saint-Gaudens National Historical Park",
         "Shenandoah National Park",
         "Theodore Roosevelt National Park",
         "Thomas Edison National Historical Park",
         "Valley Forge National Historical Park",
         "Virgin Islands National Park",
         "Voyageurs National Park",
         "White Sands National Park",
         "Wind Cave National Park",
         "Yellowstone National Park",
         "Yosemite National Park",
         "Zion National Park"

         ]
  return render_template("name.html", names=names)

# route to find visitation 
@app.route("/visitation")
def visitation(): 

 
  return render_template("visitation.html", visit= visits)

# route to find nearby hotels
#@app.route("/hotel")
#def hotel():

 #results = list(client.parks_db.find())
 #for parks in park:
 #return render_template("hotel.html", names=names)


if __name__ == "__main__":
 app.run(debug=True)