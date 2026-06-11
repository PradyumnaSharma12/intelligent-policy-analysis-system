recommendations = {
    "Medical": ["Ayushman Bharat", "National Health Mission", "PM Jan Arogya Yojana"],
    "Politics": ["Digital India", "National Governance Plan", "Smart Cities Mission"],
    "Space": [
        "Indian Space Policy",
        "ISRO Research Initiatives",
        "National Space Promotion Program",
    ],
    "Computer Graphics": [
        "Digital Education Mission",
        "Skill India Digital Training",
        "AI Innovation Program",
    ],
}


def get_recommendations(category):

    return recommendations.get(category, ["No recommendations available"])
