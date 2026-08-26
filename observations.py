def create_observation(species, confidence, date, location, image):
    observation = {"species": species,
                   "confidence": confidence,
                   "date": date,
                   "location": location,
                   "image": image}
    return observation

def print_observations(observations):
    print("Your observations:\n\n")
    for obs in observations:
        print("ID:", obs["obs_id"], "\nSpecies:", obs["species"], f'\nConfidence: {obs["confidence"]:.0f}%')
        print("Date:", obs["date"], "\nLocation:", obs["location"], "\nImage:", obs["image"], "\n")