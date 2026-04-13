def classify_ph(ph):
    if ph < 6.5:
        return "Acidic"
    elif ph <= 8.5:
        return "Neutral"
    return "Alkaline"


def get_suggestions(inputs):
    ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity = inputs

    tips = []

    if ph < 6.5:
        tips.append("Increase pH using alkaline filters")
    elif ph > 8.5:
        tips.append("Reduce pH level")

    if hardness > 200:
        tips.append("Install water softener")

    if solids > 10000:
        tips.append("Use RO filtration")

    if turbidity > 5:
        tips.append("Use sediment filters")

    if chloramines > 10:
        tips.append("Reduce chlorine content")

    return tips