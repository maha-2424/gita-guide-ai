def get_reflection(mood):

    questions = {
        "Stress": "❓ What is one thing causing you stress that you can let go of today?",

        "Career": "❓ What small step can you take today that brings you closer to your dream career?",

        "Education": "❓ What is one concept you truly understood today?",

        "Relationship": "❓ How can you show kindness to someone today?",

        "General": "❓ What is one positive thing that happened today?"
    }

    return questions.get(mood, questions["General"])