import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(file_path="data/job_roles.csv"):
    """Load job roles and required skills."""
    return pd.read_csv(file_path)


def calculate_match_scores(resume_text, job_roles):
    """
    Compare resume text with each job role using
    TF-IDF and cosine similarity.
    """

    documents = [resume_text]

    for skills in job_roles["required_skills"]:
        documents.append(skills)

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    # Compare resume vector with each job-role vector
    resume_vector = vectors[0]

    scores = []

    for i in range(1, len(documents)):
        job_vector = vectors[i]

        similarity = cosine_similarity(
            resume_vector,
            job_vector
        )[0][0]

        score = round(similarity * 100, 2)

        scores.append(score)

    result = job_roles.copy()

    result["match_score"] = scores

    # Highest score first
    result = result.sort_values(
        by="match_score",
        ascending=False
    ).reset_index(drop=True)

    return result


def get_top_roles(resume_text, top_n=3):
    """Return the top matching job roles."""

    job_roles = load_job_roles()

    results = calculate_match_scores(
        resume_text,
        job_roles
    )

    return results.head(top_n)