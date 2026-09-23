import pandas as pd


def get_required_skills(job_role, file_path="data/job_roles.csv"):
    """Get required skills for a selected job role."""

    df = pd.read_csv(file_path)

    role_data = df[df["job_role"] == job_role]

    if role_data.empty:
        return []

    skills_text = role_data.iloc[0]["required_skills"]

    required_skills = [
        skill.strip()
        for skill in skills_text.split(",")
    ]

    return required_skills


def analyze_skill_gap(
    found_skills,
    job_role,
    file_path="data/job_roles.csv"
):
    """Compare resume skills with job-role requirements."""

    required_skills = get_required_skills(
        job_role,
        file_path
    )

    found_lower = {
        skill.lower()
        for skill in found_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in found_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


def generate_learning_roadmap(missing_skills):
    """Generate a basic learning roadmap."""

    roadmap = []

    for week, skill in enumerate(
        missing_skills[:4],
        start=1
    ):
        roadmap.append(
            f"Week {week}: Learn {skill} fundamentals "
            f"and complete a small practical project."
        )

    return roadmap