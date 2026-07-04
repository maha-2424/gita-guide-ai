def get_action(mood):

    actions = {
        "Stress": "🧘 Take 10 deep breaths and spend 15 minutes meditating or sitting quietly.",

        "Career": "💼 Spend 30 minutes learning a new skill or applying for one internship/job today.",

        "Education": "📚 Study one topic for 45 minutes without checking your phone.",

        "Relationship": "❤️ Talk calmly with someone you care about and listen without interrupting.",

        "General": "🌟 Write down three things you're grateful for today."
    }

    return actions.get(mood, actions["General"])