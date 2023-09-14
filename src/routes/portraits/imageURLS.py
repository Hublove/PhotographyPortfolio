# import required module
import json
from PIL import Image
# import required module
import os
# assign directory
# Portraits Events Travel Street
category = "Street" #CHANGE THIS
directory = 'static/' + category
images = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if filename != "favicon.png" and filename != category + ".json":
            # get image
            print(f)

            img = Image.open(f)

            # get width and height
            width = img.width
            height = img.height

            # display width and height
            images.append({
                "img": "/"+category+"/"+filename,
                "thumb": "/"+category+"/thumbnails/"+filename,
                "alt": '',
                "height": height,
                "width": width,
                "element": None
            })
    print(images)
            
        
with open("src/" + category + ".json", "w") as outfile:
    json.dump(images, outfile)
    print("DONE")


