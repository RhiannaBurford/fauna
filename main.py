from observations import create_observation, print_observations
from database import get_observations, add_observation, initialise_database
initialise_database()

print("Welcome to Fauna!")

another = True
conf_accepted = False

while another:
    # Gathering user input
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


    observation = create_observation(species, confidence, date, location, image)
    row_id = add_observation(observation) # think i can delete the obs_id returned bit

    # Asking user if they want to input another observation
    enquiry = input("Observation created!\nAdd another observation? ")
    if enquiry.lower() == "no" or enquiry.lower() == "n":
        another = False


view = input("Would you like to view your observations? (y/n) ")
if view.lower() == "y":
    print_observations(get_observations())




