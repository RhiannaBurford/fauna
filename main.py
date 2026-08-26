print("Welcome to fauna!")


def create_observation(species, confidence, date, location, image):
    observation = {"species": species,
                   "confidence": confidence,
                   "date": date,
                   "location": location,
                   "image": image}
    return observation

another = True
observations = []
conf_accepted = False

while another:
    species = input("Enter a species: ")
    while not conf_accepted:
        try:
            confidence = float(input("Enter a confidence level: "))
            if (confidence < 0 or confidence > 1):
                print("That is not in the range 0 to 1")
            else:
                conf_accepted = True
        except:
            print("That is not a number")
    
    date = input("Enter a date: ")
    location = input("Enter a location: ")
    image = input("Enter the image: ")
    observation = create_observation(species, confidence, date, location, image)
    observations.append(observation)
    enquiry = input("Observation created!\nAdd another observation? ")
    if enquiry.lower() == "no" or enquiry.lower() == "n":
        another = False



print(observations)

