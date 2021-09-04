# Alternative to using python notebooks of original code.
# Follow instructions, replace specific elements and run

## Common Errors
#    VaueError: Images do not match
#    Fix: your images all need to be of the same size.  If the background is 1000x1000 and a trait layer is 500x500 this error will be thrown.

from PIL import Image
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue", "Orange", "Purple", "Red", "Yellow"]
background_weights = [30, 40, 15, 5, 10]

circle = ["Blue", "Green", "Orange", "Red", "Yellow"]
circle_weights = [30, 40, 15, 5, 10]

square = ["Blue", "Green", "Orange", "Red", "Yellow"]
square_weights = [30, 40, 15, 5, 10]

# Dictionary variable for each trait.
# Eech trait corresponds to its file name
# Rename the dictionaries, adding or removing, as desired:

background_files = {
    "Blue": "blue",
    "Orange": "orange",
    "Purple": "purple",
    "Red": "red",
    "Yellow": "yellow",
}

circle_files = {
    "Blue": "blue-circle",
    "Green": "green-circle",
    "Orange": "orange-circle",
    "Red": "red-circle",
    "Yellow": "yellow-circle"
}

square_files = {
    "Blue": "blue-square",
    "Green": "green-square",
    "Orange": "orange-square",
    "Red": "red-square",
    "Yellow": "yellow-square"

}

## Generate Traits
# Number of random unique images we want to generate.
# Start small (3) to make sure the generation process is working
# Once it's working, replace to a higher value (3000)
TOTAL_IMAGES = 3

all_images = []

# A recursive function to generate unique image combinations
def create_new_image():
    new_image = {}  #

    # REPLACE: Background, Circle, Square with the categories you're working with
    # ADD/RREMOVE: as needed.  If you have 10 traits, duplicate a line multiple times, changing the value in brackets to the designated category
    # Examole: new_image["My_New_Thing"]
    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Circle"] = random.choices(circle, circle_weights)[0]
    new_image["Square"] = random.choices(square, square_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))


# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

# This collects and reports back all the traits created:
# RRENAME: for consistency, rename each count with the trait you use.
# ADD/REMOVE: a count as needed. If you have 10 traits, duplicate a block defined below.
# The last for loop combines all counts into a dictionary of all_images:
#    This last for loop needs to be updated to have the correct categories you're using. Add, remove as needed.
# Finally, the print statements need to be updated to the counts defined here.

## Start of a Block
background_count = {}
for item in background:
    background_count[item] = 0
## End of a Block

circle_count = {}
for item in circle:
    circle_count[item] = 0

square_count = {}
for item in square:
    square_count[item] = 0

## Last block: rename what is in quotes, and add or remove lines as needed:
for image in all_images:
    background_count[image["Background"]] += 1
    circle_count[image["Circle"]] += 1
    square_count[image["Square"]] += 1

## change the variables in output:
print(background_count)
print(circle_count)
print(square_count)


#### Generate Metadata for all Traits
METADATA_FILE_NAME = './metadata/all-traits.json';
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#### Generate Images
### REPLACE: replace the categories in quotes with your own categories
##     Example: change circle_files[item["Circle"]] to my_trait(item["My Trait"]]
##     If you are using a file type other than png, change it here as well
### ADD or Remove as necessary.  If you have 10 traits, duplicate im3 multiple types but incriment im3 each time.
##     Example, if you hadd a 4th trait, name the variable im4.
for item in all_images:
    im1 = Image.open(f'./trait-layers/backgrounds/{background_files[item["Background"]]}.jpg').convert('RGBA')
    im2 = Image.open(f'./trait-layers/circles/{circle_files[item["Circle"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/squares/{square_files[item["Square"]]}.png').convert('RGBA')

    # This calls PIL to make a composite of two images
    # If you add more traits you'll need to add a new variable for each composite
    # Example: lets say you need 2 more layers made into a composite, you would create com3 = Image.alpha_composite(com2, im4) and com4 = Image.alpha.composite(com3, im5)
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)

    # Convert to RGB
    rgb_im = com2.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)


#### Generate Metadata for each Image
## In this section you need to replace the BASE URI and PROJECT_NAME for your needs
## REPLACE, ADD or REMOVE categories in the for loop

f = open('./metadata/all-traits.json',)
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    ### REPLACE the categories with your own.
    ### If necessary add or remove lines:
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Circle", i["Circle"]))
    token["attributes"].append(getAttribute("Square", i["Square"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()

## At this point genorated images should be created in the /images folder