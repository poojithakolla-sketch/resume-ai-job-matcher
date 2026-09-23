import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import (
    get_top_roles,
    calculate_match_scores,
    load_job_roles
)
from roadmap_generator import (
    analyze_skill_gap,
    generate_learning_roadmap
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
    color: #1d2939;
}

[data-testid="stAppViewContainer"] {
    background-color: #f5f7fb;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

/* Main Title */

.main-title {
    color: #101828 !important;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    color: #667085 !important;
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
}

/* Headings */

h1, h2, h3, h4 {
    color: #101828 !important;
}

/* Metric Cards */

.metric-card {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e4e7ec;
    text-align: center;
    box-shadow: 0 4px 15px rgba(16, 24, 40, 0.06);
}

.metric-title {
    color: #667085 !important;
    font-size: 14px;
    font-weight: 600;
}

.metric-value {
    color: #101828 !important;
    font-size: 30px;
    font-weight: 800;
    margin-top: 5px;
}

/* Section Titles */

.section-title {
    color: #101828 !important;
    font-size: 25px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Skills */

.skill-badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 20px;
    background-color: #eef4ff;
    color: #175cd3 !important;
    font-weight: 600;
    font-size: 14px;
    border: 1px solid #d1e0ff;
}

/* Role Cards */

.role-card {
    background-color: #ffffff;
    color: #101828 !important;
    padding: 18px;
    margin-bottom: 12px;
    border-radius: 14px;
    border: 1px solid #e4e7ec;
    box-shadow: 0 3px 10px rgba(16, 24, 40, 0.05);
}

.role-card b {
    color: #101828 !important;
}

/* Roadmap */

.roadmap-card {
    background-color: #ffffff;
    color: #344054 !important;
    padding: 18px;
    margin: 10px 0;
    border-left: 5px solid #4f46e5;
    border-radius: 10px;
    border: 1px solid #e4e7ec;
}

.roadmap-card b {
    color: #101828 !important;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #20232d;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #ffffff !important;
}

/* Footer */

.footer {
    color: #667085 !important;
    text-align: center;
    font-size: 13px;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<div class="main-title">🤖 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your resume • Discover your skills • Explore suitable job roles'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ Resume Analysis")

    uploaded_file = st.file_uploader(
        "📄 Upload your Resume",
        type=["pdf", "docx"],
        help="Upload a PDF or DOCX resume."
    )

    st.markdown("---")

    job_roles = load_job_roles()

    role_list = job_roles["job_role"].tolist()

    selected_role = st.selectbox(
        "🎯 Target Job Role",
        role_list
    )

    st.markdown("---")

    st.info(
        "💡 Tip: A resume with clear skills, projects, "
        "education and experience gives better analysis."
    )


# ==========================================================
# WELCOME SCREEN
# ==========================================================

if uploaded_file is None:

    st.markdown(
        '<div class="section-title">🚀 Resume Analysis Dashboard</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-title">📄 Resume Upload</div>'
            '<div class="metric-value">PDF / DOCX</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-title">🎯 Job Roles</div>'
            '<div class="metric-value">5+</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="metric-card">'
            '<div class="metric-title">🧠 Skill Analysis</div>'
            '<div class="metric-value">AI/NLP</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">✨ What this system does</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📄 Resume Analysis")
        st.write(
            "Extract resume text and identify important "
            "technical and job-related skills."
        )

        st.write("### 📊 Match Analysis")
        st.write(
            "Compare your resume against available "
            "job roles and calculate similarity scores."
        )

    with col2:
        st.write("### 💼 Job Recommendations")
        st.write(
            "View the top matching job roles based on "
            "your resume content."
        )

        st.write("### 📚 Skill Gap Roadmap")
        st.write(
            "Identify missing skills and get a simple "
            "learning roadmap."
        )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">💼 Available Job Roles</div>',
        unsafe_allow_html=True
    )

    role_columns = st.columns(3)

    for index, role in enumerate(role_list):

        role_columns[index % 3].markdown(
            f"🔹 **{role}**"
        )


# ==========================================================
# RESUME PROCESSING
# ==========================================================

else:

    st.success(
        f"✅ Resume uploaded: **{uploaded_file.name}**"
    )

    try:

        # --------------------------------------------------
        # Extract text
        # --------------------------------------------------

        resume_text = extract_resume_text(
            uploaded_file
        )

        if not resume_text.strip():

            st.error(
                "❌ No readable text was found in the resume."
            )

            st.stop()


        # --------------------------------------------------
        # Clean text
        # --------------------------------------------------

        cleaned_text = clean_text(
            resume_text
        )


        # --------------------------------------------------
        # Extract skills
        # --------------------------------------------------

        found_skills = extract_skills(
            cleaned_text
        )


        # --------------------------------------------------
        # Calculate job scores
        # --------------------------------------------------

        results = calculate_match_scores(
            cleaned_text,
            job_roles
        )


        # --------------------------------------------------
        # Selected role score
        # --------------------------------------------------

        selected_result = results[
            results["job_role"] == selected_role
        ]

        if not selected_result.empty:

            selected_score = float(
                selected_result.iloc[0]["match_score"]
            )

        else:

            selected_score = 0


        # --------------------------------------------------
        # Skill gap
        # --------------------------------------------------

        matched_skills, missing_skills = (
            analyze_skill_gap(
                found_skills,
                selected_role
            )
        )


        # --------------------------------------------------
        # Roadmap
        # --------------------------------------------------

        roadmap = generate_learning_roadmap(
            missing_skills
        )


        # ==================================================
        # TOP METRICS
        # ==================================================

        st.markdown("---")

        st.markdown(
            '<div class="section-title">📊 Resume Overview</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        🎯 Target Match
                    </div>
                    <div class="metric-value">
                        {selected_score:.1f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        🧠 Skills Found
                    </div>
                    <div class="metric-value">
                        {len(found_skills)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        ❌ Missing Skills
                    </div>
                    <div class="metric-value">
                        {len(missing_skills)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        💼 Roles Analyzed
                    </div>
                    <div class="metric-value">
                        {len(results)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ==================================================
        # TABS
        # ==================================================

        st.markdown("---")

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "📄 Resume",
                "🧠 Skills",
                "💼 Job Roles",
                "❌ Skill Gap",
                "📚 Roadmap"
            ]
        )


        # ==================================================
        # TAB 1
        # ==================================================

        with tab1:

            st.subheader(
                "📄 Extracted Resume Content"
            )

            st.text_area(
                "Resume Text",
                cleaned_text,
                height=450
            )


        # ==================================================
        # TAB 2
        # ==================================================

        with tab2:

            st.subheader(
                "🧠 Skills Detected"
            )

            if found_skills:

                st.write(
                    f"**{len(found_skills)} skills detected**"
                )

                skill_html = ""

                for skill in found_skills:

                    skill_html += (
                        f'<span class="skill-badge">'
                        f'✓ {skill}'
                        f'</span>'
                    )

                st.markdown(
                    skill_html,
                    unsafe_allow_html=True
                )

            else:

                st.warning(
                    "No skills were detected from the resume."
                )


        # ==================================================
        # TAB 3
        # ==================================================

        with tab3:

            st.subheader(
                "💼 Job Role Match Analysis"
            )

            st.write(
                f"Target Role: **{selected_role}**"
            )

            st.metric(
                "🎯 Target Role Match Score",
                f"{selected_score:.1f}%"
            )

            st.markdown("---")

            st.subheader(
                "🏆 Recommended Roles"
            )

            top_roles = get_top_roles(
                cleaned_text,
                top_n=3
            )

            for index, row in top_roles.iterrows():

                st.markdown(
                    f"""
                    <div class="role-card">
                        <b>{index + 1}. {row['job_role']}</b>
                        <br>
                        Match Score:
                        <b>{row['match_score']:.1f}%</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.progress(
                    min(
                        int(row["match_score"]),
                        100
                    )
                )

            st.markdown("---")

            st.subheader(
                "📈 Role Match Chart"
            )

            chart_data = results[
                ["job_role", "match_score"]
            ].set_index("job_role")

            st.bar_chart(
                chart_data
            )


        # ==================================================
        # TAB 4
        # ==================================================

        with tab4:

            st.subheader(
                f"🎯 Skill Gap — {selected_role}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("### ✅ Skills Found")

                if matched_skills:

                    for skill in matched_skills:

                        st.success(
                            f"✓ {skill}"
                        )

                else:

                    st.info(
                        "No matching required skills detected."
                    )

            with col2:

                st.write("### ❌ Missing Skills")

                if missing_skills:

                    for skill in missing_skills:

                        st.error(
                            f"✗ {skill}"
                        )

                else:

                    st.success(
                        "🎉 No missing skills detected!"
                    )


        # ==================================================
        # TAB 5
        # ==================================================

        with tab5:

            st.subheader(
                "📚 Personalized Learning Roadmap"
            )

            if roadmap:

                for index, item in enumerate(
                    roadmap,
                    start=1
                ):

                    st.markdown(
                        f"""
                        <div class="roadmap-card">
                            <b>📌 Step {index}</b>
                            <br><br>
                            {item}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.success(
                    "🎉 No learning gaps detected!"
                )


        # ==================================================
        # DOWNLOAD REPORT
        # ==================================================

        st.markdown("---")

        st.subheader(
            "📥 Download Analysis Report"
        )

        report = f"""
AI RESUME ANALYZER AND JOB RECOMMENDATION SYSTEM
================================================

Resume:
{uploaded_file.name}

Target Job Role:
{selected_role}

Target Role Match Score:
{selected_score:.1f}%

Detected Skills:
{", ".join(found_skills)}

Matched Skills:
{", ".join(matched_skills)}

Missing Skills:
{", ".join(missing_skills)}

Learning Roadmap:
{chr(10).join(roadmap)}
"""

        st.download_button(
            label="📥 Download Full Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )


    except Exception as e:

        st.error(
            "❌ Something went wrong while analyzing the resume."
        )

        st.exception(e)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">
        🤖 AI Resume Analyzer & Job Recommendation System
        <br>
        Educational Project • Match scores are estimates
        and are not automatic hiring decisions.
    </div>
    """,
    unsafe_allow_html=True
)