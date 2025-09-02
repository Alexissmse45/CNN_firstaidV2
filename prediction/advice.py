def get_advice(injury_class,  confidence):
    advice_dict = {
        "bleeding": "Apply pressure to the wound with a clean cloth and seek help if bleeding doesn't stop.",
        "fracture": "Immobilize the injured area and seek medical attention immediately.",
        "burn": "Cool the burn under running water and cover with a clean cloth.",
        "allergic reaction": "Take an antihistamine if available and seek medical help.",
        "choking": "Perform the Heimlich maneuver if trained, and call emergency services.",
        "dog bite": "Wash the bite with soap and water, apply antiseptic, and seek medical care.",
        "electrical injuries": "Turn off the power source and call emergency services immediately.",
        "cat claw scratch": "Clean the wound with soap and water, apply antiseptic cream.",
        "mosquito bite": "Apply anti-itch cream and avoid scratching.",
        "normal": "No visible injury detected. You seem fine, but monitor your condition and seek help if you feel unwell."
    }

    if confidence < 0.5:
         return "⚠️ I'm not confident about this prediction. Please seek professional medical help."
    return advice_dict.get(injury_class, "No advice available for this injury.")
