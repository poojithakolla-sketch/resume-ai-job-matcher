import pandas as pd


def load_skill_dictionary(file_path="data/skill_dictionary.csv"):
    """Load skills from the skill dictionary CSV file."""
    df = pd.read_csv(file_path)

    skills = df["skill"].dropna().tolist()

    return skills


def extract_skills(text, file_path="data/skill_dictionary.csv"):
    """Find skills present in the resume text."""

    skills = load_skill_dictionary(file_path)

    text_lower = text.lower()

    found_skills = []

    for skill in skills:
        skill_lower = skill.lower()

        if skill_lower in text_lower:
            found_skills.append(skill)

    return sorted(found_skills)