import random

"""This class is responsible for determining the secret word. It gets pulled from a catalog of 5 letter words"""
class Hidden_Word:
    def __init__(self):

        """creates list within word class called word_catalog"""

        word_catalog = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis",
                        "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Brain",
                        "Bread", "Break", "Break", "Brown", "Buyer", "Cause", "Chain",
                        "Chair", "Chest", "Cheif", "Child", "Dream", "Dress", "Depth",
                        "Drive", "Drink", "Event", "Final", "Force", "Floor", "Focus", 
                        "Frame", "Guide", "Heart", "Henry", "Hotel", "House", "Image", 
                        "Index", "Input", "Judge", "Knife", "Lunch", "Limit", "Model", 
                        "Motor", "Mouth", "Month", "Money", "Music", "Night", "Noise", 
                        "North", "Novel", "Nurse", "Offer", "Order", "Phase", "Peace", 
                        "Pilot", "Pitch", "Place", "Plane", "Plate", "Point", "Pound"]

        """randomly selects word form list"""
        self._secret_word = random.choice(word_catalog).lower()

#  def __init__(self):
#             word_catalog = ["agars"]

#             self._secret_word = str(word_catalog[0])