print("Welcome to fauna!")


def create_observation(species, confidence, date, location, image, id):
    observation = {"species": species,
                   "confidence": confidence,
                   "date": date,
                   "location": location,
                   "image": image,
                   "id": id}
    return observation

def print_obs():
    print("Your observations:\n\n")
    for obs in observations:
        print("ID:", obs["id"], "\nSpecies:", obs["species"], "\nConfidence:", obs["confidence"]*100, "%" \
        "\nDate:", obs["date"], "\nLocation:", obs["location"], "\nImage:", obs["image"], "\n")

another = True
observations = []
conf_accepted = False
id = 0

while another:
    species = input("Enter a species: ")
    while not conf_accepted:
        try:
            confidence = float(input("Enter a confidence level: "))
            if (confidence < 0 or confidence > 1):
                print("That is not in the range 0 to 1")
            else:
                conf_accepted = True
        except ValueError:
            print("That is not a number")
    date = input("Enter a date: ")
    location = input("Enter a location: ")
    image = input("Enter the image: ")
    observation = create_observation(species, confidence, date, location, image, id)
    id = id + 1
    observations.append(observation)
    enquiry = input("Observation created!\nAdd another observation? ")
    if enquiry.lower() == "no" or enquiry.lower() == "n":
        another = False

view = input("Would you like to view your observations? (y/n)")
if view.lower() == "y":
    print_obs()




