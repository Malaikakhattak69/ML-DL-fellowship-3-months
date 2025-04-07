def calculate_percentage(total, obtained):
    return (obtained / total) * 100

def classify_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 75:
        return "A"
    elif percent >= 60:
        return "B"
    else:
        return "C"
