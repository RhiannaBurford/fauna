from observations import create_observation, print_observations

print("Welcome to fauna!")

another = True
observations = []
conf_accepted = False
obs_id = 1

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
    obs_id = obs_id + 1
    observations.append(observation)
    enquiry = input("Observation created!\nAdd another observation? ")
    if enquiry.lower() == "no" or enquiry.lower() == "n":
        another = False

view = input("Would you like to view your observations? (y/n) ")
if view.lower() == "y":
    print_observations(observations)




