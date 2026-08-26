def create_observation(species, confidence, date, location, image, obs_id):
    observation = {"species": species,
                   "confidence": confidence,
                   "date": date,
                   "location": location,
                   "image": image,
                   "obs_id": obs_id}
    return observation

def print_observations(observations):
    print("Your observations:\n\n")
    for obs in observations:
        print("ID:", obs["obs_id"], "\nSpecies:", obs["species"], f'\nConfidence: ${obs["confidence"]:.0f}%')
        print("\nDate:", obs["date"], "\nLocation:", obs["location"], "\nImage:", obs["image"], "\n")