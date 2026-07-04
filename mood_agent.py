def detect_mood(user_input):

    text = user_input.lower()

    # Career first
    career_words = [
        "career", "job", "placement", "placements",
        "interview", "interviews", "internship", "resume"
    ]

    if any(word in text for word in career_words):
        return "Career"

    # Education
    education_words = [
        "exam", "study", "college", "marks",
        "semester", "subject", "assignment"
    ]

    if any(word in text for word in education_words):
        return "Education"

    # Relationship
    relationship_words = [
        "love", "relationship", "family",
        "friend", "friends"
    ]

    if any(word in text for word in relationship_words):
        return "Relationship"

    # Stress
    stress_words = [
        "stress", "stressed", "anxiety",
        "pressure", "tension", "panic"
    ]

    if any(word in text for word in stress_words):
        return "Stress"

    return "General"