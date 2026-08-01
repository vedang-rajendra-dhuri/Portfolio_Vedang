import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import re

# Page configuration
st.set_page_config(
    page_title="Vedang Dhuri | AI & Automation Engineer - SaaS Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Comprehensive Technology Knowledge Dictionary
TECH_DESCRIPTIONS = {
    "Python": "Modern, high-level programming language renowned for clean syntax and a massive ecosystem of libraries for AI/ML, data processing, FastAPI, and rapid automation.",
    "FastAPI": "High-performance, asynchronous Python web framework built for fast REST API development, automatic OpenAPI documentation, and high-concurrency microservices.",
    "Generative AI": "Artificial Intelligence paradigm focused on creating original content (text, code, synthetic data, images) using transformer-based foundation models.",
    "Large Language Models (LLMs)": "Deep learning foundation models trained on massive text corpora capable of natural language reasoning, translation, summarization, and code generation.",
    "Agentic AI": "Next-generation AI systems capable of autonomous planning, goal decomposition, environment reflection, and multi-agent task execution.",
    "AI Agents": "Autonomous software entities powered by LLMs that make decisions, execute multi-step plans, and interact with external APIs to complete complex objectives.",
    "Prompt Engineering": "The art and science of structuring, optimizing, and safety-guarding inputs to LLMs to produce accurate, context-aware, and structured outputs.",
    "RAG (Retrieval-Augmented Generation)": "Architecture that pairs external vector database search with LLM generation, eliminating hallucinations and grounding responses in real company data.",
    "LangChain": "Leading open-source framework designed for building LLM-powered applications with memory, prompt templates, and vector retriever chains.",
    "LangGraph": "Advanced framework for building stateful, multi-actor LLM applications with cyclical graph flows, state persistence, and human-in-the-loop control.",
    "CrewAI": "Cutting-edge agent orchestration framework designed to deploy collaborative teams of specialized, role-playing AI agents.",
    "MCP (Model Context Protocol)": "Universal open protocol for connecting AI agents and models securely to enterprise databases, tools, APIs, and file systems.",
    "n8n": "Enterprise workflow automation platform enabling seamless integration of REST webhooks, AI nodes, databases, and custom Python/JS logic.",
    "React": "Industry-standard frontend JavaScript library for constructing responsive, component-driven user interfaces and dynamic single-page web apps.",
    "PostgreSQL": "Advanced open-source relational database management system featuring enterprise SQL compliance, vector extensions (pgvector), and JSON support.",
    "MySQL": "Widely deployed, reliable relational database management system optimized for high-speed read operations and web application backends.",
    "SQLAlchemy": "The gold-standard Python SQL toolkit and Object-Relational Mapper (ORM) providing full power, flexibility, and clean database abstraction.",
    "Docker": "Containerization platform that packages applications into lightweight, isolated containers for seamless deployment across dev, staging, and cloud environments.",
    "Git": "Distributed version control system tracking code history, enabling parallel feature branching, and powering collaborative software development.",
    "OpenAI API": "Enterprise API suite providing direct access to state-of-the-art GPT-4, Embeddings, and Vision models for reasoning and text generation.",
    "Gemini API": "Google's multimodal AI API offering high-speed reasoning, vision processing, long-context windows, and structured JSON output generation.",
    "Explainable AI (XAI)": "Suite of machine learning techniques (like SHAP and LIME) that make model predictions transparent, interpretable, and audit-friendly.",
    "REST APIs": "Architectural style for network applications using standard HTTP methods (GET, POST, PUT, DELETE) to transfer structured data.",
    "Java": "Object-oriented, strongly typed programming language built for enterprise scale, high performance, and cross-platform reliability.",
    "JavaScript": "The foundational scripting language of the Web, powering client-side interactivity, dynamic UI rendering, and Node.js backend services.",
    "SQL": "Standardized domain-specific language used for managing, querying, and manipulating data stored in relational database management systems."
}

# Master Profile Data
PROFILE = {
    "name": "VEDANG RAJENDRA DHURI",
    "title": "AI & Automation Engineer",
    "headline": "Architecting Enterprise AI Agents, RAG Workflows & Scalable Intelligent Automation",
    "email": "dhurivedang4104@gmail.com",
    "phone": "+91 9404137976",
    "location": "Sindhudurg, Maharashtra, India",
    "linkedin": "https://linkedin.com/in/vedanggg",
    "github": "https://github.com/Vedang07-eng",
    "summary": (
        "Results-driven AI & Automation Engineer specializing in building enterprise-grade Generative AI applications," 
        "Large Language Model (LLM) agents, and autonomous RAG architectures. Proficient in Python, FastAPI, n8n, and Prompt Engineering, "
        "with hands-on expertise in LangChain, LangGraph, CrewAI, and Model Context Protocol (MCP). Proven track record of designing "
        "end-to-end automation pipelines that reduce manual overhead by over 50% and transform raw data into intelligent operational systems."
    ),
    "stats": [
        {"label": "Degree CGPA", "val": "7.5 / 10", "sub": "B.E. IT (Data Science)"},
        {"label": "AI Systems Built", "val": "5+", "sub": "GenAI, RAG & Agents"},
        {"label": "Certifications", "val": "7", "sub": "Python, AI & Governance"},
        {"label": "Research Paper", "val": "ETTS-2026", "sub": "Explainable AI (XAI)"}
    ],
    "skills": {
        "🤖 AI & LLM Architecture": [
            "Generative AI", "Large Language Models (LLMs)", "Agentic AI", "AI Agents", 
            "Prompt Engineering", "RAG (Retrieval-Augmented Generation)", "LangChain", 
            "LangGraph", "MCP (Model Context Protocol)"
        ],
        "💻 Core Development": ["Python", "Java", "JavaScript", "SQL"],
        "⚡ Web Services & APIs": ["FastAPI", "REST APIs", "React"],
        "🔄 Workflow & Automation": ["n8n"],
        "🗄️ Databases & ORM": ["PostgreSQL", "MySQL", "SQLAlchemy"],
        "🛠️ DevOps & AI Tools": ["Docker", "Git", "OpenAI API", "Gemini API", "Explainable AI (XAI)"]
    },
    "radar_skills": {
        "Agentic AI & LLMs": 95,
        "Python & FastAPI": 92,
        "RAG Systems & LangChain": 90,
        "n8n Workflow Automation": 88,
        "PostgreSQL & Databases": 84,
        "React & Frontend APIs": 82,
        "Docker & DevOps": 80
    },
    "projects": [
        {
            "title": "Intervexa — AI-Powered Interview Platform",
            "category": "GenAI & SaaS Platform",
            "tech": ["React", "FastAPI", "Large Language Models (LLMs)", "REST APIs", "Python"],
            "summary": "An intelligent simulation platform providing real-time adaptive technical and HR mock interviews with automated performance diagnostics.",
            "points": [
                "Architected an AI-driven interview practice platform to simulate real-world technical and HR interview rounds.",
                "Integrated Large Language Models (LLMs) to generate role-specific, context-aware, and dynamically adaptive interview questions.",
                "Implemented AI-based multi-metric response evaluation delivering personalized feedback, score breakdowns, and improvement path recommendations.",
                "Built a sleek, responsive React frontend coupled with FastAPI backend microservices for low-latency question streaming."
            ]
        },
        {
            "title": "Crop Recommendation System — ML & Agricultural Intelligence",
            "category": "RAG & Machine Learning",
            "tech": ["RAG (Retrieval-Augmented Generation)", "Python", "Explainable AI (XAI)"],
            "summary": "Precision agricultural decision engine combining machine learning ensemble models with Retrieval-Augmented Generation (RAG).",
            "points": [
                "Engineered a machine learning recommendation pipeline utilizing RAG to suggest optimal crop selection based on soil NPK ratios, rainfall, and climate data.",
                "Applied advanced data preprocessing, outlier filtering, and feature engineering to maximize prediction accuracy.",
                "Deployed an explainable AI (XAI) analytics module enabling farmers to understand crop yield drivers and resource optimization."
            ]
        },
        {
            "title": "Healthcare Doctor Appointment Management System",
            "category": "Intelligent Workflow Automation",
            "tech": ["Python", "PostgreSQL", "REST APIs", "SQLAlchemy"],
            "summary": "Automated healthcare scheduling platform that reduced administrative booking overhead by 50%.",
            "points": [
                "Designed a multi-tenant healthcare appointment booking platform with real-time doctor availability tracking.",
                "Implemented automated notification pipelines and automated schedule sync to eliminate double-booking.",
                "Reduced manual scheduling overhead by 50%, improved patient confirmation speed, and streamlined clinic operations using Python backend services."
            ]
        },
        {
            "title": "Roadmap Manager — AI-Powered Career Planning Engine",
            "category": "Agentic AI & EdTech",
            "tech": ["Generative AI", "FastAPI", "AI Agents", "Prompt Engineering"],
            "summary": "Intelligent learning platform utilizing AI Agents to generate dynamic, milestone-driven career roadmaps.",
            "points": [
                "Built a career navigation tool powered by Generative AI agents that creates customized skill acquisition roadmaps.",
                "Utilized specialized Prompt Engineering to break down complex technical disciplines into step-by-step actionable milestones.",
                "Integrated progress tracking widgets and real-time path adjustment features for continuous skill mastery."
            ]
        },
        {
            "title": "AURA AI — Intelligent Smart Chatbot Assistant",
            "category": "LLM Conversational Assistant",
            "tech": ["Large Language Models (LLMs)", "Prompt Engineering", "Python"],
            "summary": "Enterprise natural language chatbot assistant for context-aware query processing and automated task execution.",
            "points": [
                "Developed a smart chatbot assistant capable of understanding complex multi-turn natural language queries.",
                "Integrated leading LLM APIs with custom prompt guardrails for accurate, brand-aligned, and secure user interactions.",
                "Engineered webhook & REST API integrations to allow the chatbot to perform external task automations."
            ]
        }
    ],
    "experience": [
        {
            "role": "Cybersecurity Analyst",
            "company": "Tata Consultancy Services (TCS) — Virtual Experience Program",
            "period": "Virtual Simulation Program",
            "details": [
                "Executed hands-on cybersecurity simulations centered around real-world threat analysis, vulnerability identification, and incident response strategies.",
                "Evaluated enterprise security risks, enforced cybersecurity best practices, and authored technical documentation to fortify organizational defense postures."
            ]
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Engineering (B.E.), Information Technology",
            "honors": "Honors in Data Science",
            "institution": "University of Mumbai",
            "period": "2023 – 2027",
            "grade": "CGPA: 7.5 / 10"
        },
        {
            "degree": "Higher Secondary Certificate (HSC)",
            "institution": "B.M. Gogate Jr. College of Science, Commerce & Arts",
            "period": "2021 – 2023",
            "grade": "First Class "
        },
        {
            "degree": "Secondary School Certificate (SSC)",
            "institution": "Asoli Highschool, Vengurla",
            "period": "2018 – 2021",
            "grade": "First Class"
        }
    ],
    "publication": {
        "title": "GreenGuide: An Explainable, Profit-Aware, and Rotation-Guided Stacking Ensemble Framework for Integrated Crop Recommendation",
        "conference": "National Conference on Emerging Trends in Technology and Science (ETTS-2026)",
        "year": "2026",
        "abstract": "Presents a novel Machine Learning & Explainable AI (XAI) stacking ensemble framework that incorporates profit metrics and crop rotation guidelines to maximize agricultural yield sustainability."
    },
    "certifications": [
        {"name": "Advanced Python", "desc": "Mastery in Python data structures, object-oriented design, async paradigms, and AI/ML solution architectures."},
        {"name": "Essential Generative AI Professional", "desc": "Specialized expertise in Large Language Models (LLMs), prompt engineering strategies, and GenAI workflows."},
        {"name": "AI & Automation", "desc": "Foundational and advanced mastery of AI-driven process automation, workflow optimization, and agent design."},
        {"name": "AI Security & Governance", "desc": "Comprehensive knowledge of AI safety standards, ethical AI frameworks, vulnerability mitigation, and governance."},
        {"name": "AI Database Administration", "desc": "Expertise in AI-integrated data systems, PostgreSQL, SQLAlchemy ORM, and high-concurrency database setups."},
        {"name": "Data Mining with Python", "desc": "Applied data science techniques for pattern extraction, predictive modeling, and feature engineering."},
        {"name": "Business Communication", "desc": "Professional executive communication, technical presentation, project coordination, and cross-functional team leadership."}
    ],
    "soft_skills": [
        "Problem-Solving & Analytical Thinking",  "Technical Documentation",
        "Project Coordination", "System Architecture & API Design",
        "Team Collaboration", "Executive Communication & Presentation", "Continuous Learning"
    ],
    "languages": [
        {"lang": "English", "proficiency": "Fluent / Professional"},
        {"lang": "Marathi", "proficiency": "Native / Fluent"},
        {"lang": "Hindi", "proficiency": "Fluent"}
    ],
    "declaration": {
        "text": "I hereby declare that all the information furnished above is true, complete, and correct to the best of my knowledge.",
        "name": "Vedang Dhuri",
        "place": "Vengurla",
        "date": "01/08/2026"
    }
}

# Ultra-Bold SaaS CSS Overrides (fixing Pills contrast & text visibility 100%)
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #ffffff !important;
    }
    
    /* Background Deep Slate Gradient */
    .stApp {
        background: radial-gradient(circle at 12% 18%, #030712 0%, #090d16 45%, #0f172a 85%, #020617 100%);
        color: #ffffff !important;
    }
    
    /* Refined High-Contrast Hero Typography */
    .hero-name {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        letter-spacing: -1.2px;
        background: linear-gradient(135deg, #ffffff 0%, #38bdf8 60%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 8px;
    }
    
    .hero-subhead {
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.4;
        margin-top: 4px;
        margin-bottom: 20px;
    }

    /* Status Pill */
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(16, 185, 129, 0.2);
        border: 1.5px solid #10b981;
        color: #34d399 !important;
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 0.9rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.4px;
        box-shadow: 0 0 16px rgba(16, 185, 129, 0.3);
    }
    .status-dot {
        width: 10px;
        height: 10px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
    }
    
    /* SaaS Glassmorphism Card Container */
    .saas-card {
        background: rgba(15, 23, 42, 0.92) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1.5px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 24px;
        box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.65);
    }
    
    /* Refined Bold Text Visibility */
    p, li, span, label, div {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        line-height: 1.7 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    /* Counter Stat Cards */
    .stat-card {
        background: rgba(15, 23, 42, 0.9) !important;
        border: 1.5px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 18px;
        padding: 22px 14px;
        text-align: center;
    }

    /* CRITICAL FIX: STREAMLIT PILLS STYLING TO OVERRIDE WHITE BLANK PILLS */
    div[data-testid="stPills"] button, 
    div[data-testid="stPills"] [role="option"],
    .stPills button,
    [data-baseweb="button-group"] button {
        background-color: #1e293b !important;
        background: #1e293b !important;
        border: 1.5px solid #38bdf8 !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        border-radius: 30px !important;
    }

    div[data-testid="stPills"] button *, 
    div[data-testid="stPills"] [role="option"] *,
    .stPills button * {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 0.92rem !important;
    }

    div[data-testid="stPills"] button[aria-selected="true"],
    div[data-testid="stPills"] [aria-selected="true"] {
        background: linear-gradient(135deg, #38bdf8 0%, #6366f1 100%) !important;
        border-color: #ffffff !important;
        color: #ffffff !important;
        box-shadow: 0 0 14px rgba(56, 189, 248, 0.6) !important;
    }
    
    div[data-testid="stPills"] button[aria-selected="true"] * {
        color: #ffffff !important;
        font-weight: 900 !important;
    }

    /* Standard Button Styling */
    .stButton button {
        background: #1e293b !important;
        border: 1.5px solid #38bdf8 !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #38bdf8 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.5) !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: rgba(3, 7, 18, 0.98) !important;
        border-right: 1.5px solid rgba(56, 189, 248, 0.2) !important;
    }

    /* Streamlit Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(15, 23, 42, 0.9);
        padding: 8px;
        border-radius: 16px;
        border: 1.5px solid rgba(56, 189, 248, 0.2);
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 12px;
        color: #cbd5e1 !important;
        font-weight: 800 !important;
        font-size: 0.98rem !important;
        border: none !important;
        padding: 0 20px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 18px rgba(79, 70, 229, 0.6) !important;
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3.5rem;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Session State for Selected Tech Description
if 'selected_tech_desc' not in st.session_state:
    st.session_state['selected_tech_desc'] = "Python"

# Sidebar Info
with st.sidebar:
    st.image("https://api.dicebear.com/7.x/bottts/svg?seed=VedangUltra", width=105)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"**{PROFILE['title']}**")
    st.caption(f"📍 {PROFILE['location']}")
    
    st.divider()
    
    st.markdown("#### 📬 Direct Links")
    st.markdown(f"📧 [{PROFILE['email']}](mailto:{PROFILE['email']})")
    st.markdown(f"📞 `{PROFILE['phone']}`")
    st.markdown(f"💼 [LinkedIn Profile]({PROFILE['linkedin']})")
    st.markdown(f"💻 [GitHub Repository]({PROFILE['github']})")
    
    st.divider()
    
    st.subheader("📄 Resume Upload")
    uploaded_file = st.file_uploader("Upload PDF or Word Resume", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.success("Resume synchronized!")

# Hero Section
col_hero_text, col_hero_badge = st.columns([2.5, 1])

with col_hero_text:
    st.markdown(
        f'''
        <div class="status-pill" style="margin-bottom: 14px;">
            <div class="status-dot"></div>
            <span>OPEN FOR FULL-TIME AI & AUTOMATION ROLES</span>
        </div>
        <h1 class="hero-name">{PROFILE["name"]}</h1>
        <div class="hero-subhead">{PROFILE["headline"]}</div>
        ''',
        unsafe_allow_html=True
    )

with col_hero_badge:
    st.markdown(
        f'''
        <div class="saas-card" style="text-align: center; padding: 22px;">
            <p style="margin: 0; font-weight: 800; color: #38bdf8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.2px;">Core Discipline</p>
            <h3 style="margin: 6px 0 12px 0; color: #ffffff; font-weight: 900;">Agentic AI & FastAPI</h3>
            <p style="color: #38bdf8; font-size: 0.9rem; font-weight: 700;">Python • RAG • LangChain • n8n</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

# Summary Card
st.markdown(
    f'''
    <div class="saas-card">
        <p style="font-size: 1.15rem !important; line-height: 1.8 !important; margin: 0; color: #ffffff !important; font-weight: 600;">
            {PROFILE["summary"]}
        </p>
    </div>
    ''',
    unsafe_allow_html=True
)

# Stat Counters Row
cols = st.columns(len(PROFILE["stats"]))
for idx, stat in enumerate(PROFILE["stats"]):
    with cols[idx]:
        st.markdown(
            f'''
            <div class="stat-card">
                <h2 style="margin: 0; font-size: 2.3rem; font-weight: 900; color: #38bdf8;">{stat["val"]}</h2>
                <p style="margin-top: 4px; margin-bottom: 2px; color: #ffffff; font-weight: 800; font-size: 0.95rem;">{stat["label"]}</p>
                <p style="margin: 0; color: #cbd5e1; font-size: 0.82rem; font-weight: 600;">{stat["sub"]}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# 1. Define your categorized technologies

# 2. Track currently selected skill in st.session_state
if 'selected_tech_desc' not in st.session_state:
    st.session_state['selected_tech_desc'] = "Python"

st.markdown("### 📌 Skill Categories (Click button to view description):")

# 3. Render categories and place the description dynamically under the active category
for category, tech_list in PROFILE["skills"].items():
    st.markdown(f"#### {category}")
    
    # Render pill buttons for this category
    selected_pill = st.pills(
        f"Select {category}:",
        options=tech_list,
        default=st.session_state['selected_tech_desc'] if st.session_state['selected_tech_desc'] in tech_list else None,
        key=f"pill_{category}",
        label_visibility="collapsed"
    )
    
    # Update global selection when a pill in this category is clicked
    if selected_pill:
        st.session_state['selected_tech_desc'] = selected_pill

    # Display description HERE directly under the category if the selected tech belongs to it
    if st.session_state['selected_tech_desc'] in tech_list:
        current_tech = st.session_state['selected_tech_desc']
        st.markdown(
            f'''
            <div class="saas-card" style="border-left: 6px solid #38bdf8; background: #0f172a !important; margin-top: 12px; margin-bottom: 20px; box-shadow: 0 8px 30px rgba(56,189,248,0.25);">
                <h3 style="margin: 0; color: #38bdf8 !important; font-weight: 900; font-size: 1.25rem;">🔹 {current_tech}</h3>
                <p style="margin-top: 8px; margin-bottom: 0; color: #ffffff !important; font-size: 1.05rem !important; line-height: 1.6 !important; font-weight: 600;">
                    {TECH_DESCRIPTIONS.get(current_tech, '')}
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
# Main SaaS Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "⚡ AI & System Architecture",
    "🚀 Product Portfolio",
    "🎯 AI Job Description Matcher",
    "💼 Experience & Education",
    "📜 Research & Certifications",
    "📬 Work With Vedang"
])

# TAB 1: AI & SYSTEM ARCHITECTURE
with tab1:
    st.markdown("<h3 style='text-align: center;'>⚡ AI Agent & Engineering Competency Architecture</h3>", unsafe_allow_html=True)
    
    # Wrap in centered 3-column layout
    _, col_chart, _ = st.columns([1, 3, 1])
    
    with col_chart:
        st.markdown("<h4 style='text-align: center; color: #38bdf8; font-weight: 900;'>Radar Analysis of Core Engineering Skills</h4>", unsafe_allow_html=True)
        
        df_radar = pd.DataFrame({
            'Competency': list(PROFILE["radar_skills"].keys()),
            'Proficiency': list(PROFILE["radar_skills"].values())
        })
        
        fig = px.line_polar(
            df_radar, r='Proficiency', theta='Competency', line_close=True,
            template="plotly_dark"
        )
        fig.update_traces(
            fill='toself', 
            line_color='#818cf8', 
            fillcolor='rgba(99, 102, 241, 0.45)'
        )
        
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=40, r=40, t=30, b=30),
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], color="#cbd5e1"),
                angularaxis=dict(color="#ffffff", tickfont=dict(size=12, color="#ffffff")),
                bgcolor="rgba(15, 23, 42, 0.8)"
            )
        )
        st.plotly_chart(fig, width="stretch")
    # with col_skills_grid:
    #     st.markdown("##### 📌 Skill Categories (Click button to view description):")
    #     for cat_name, skill_list in PROFILE["skills"].items():
    #         st.markdown(f"<strong style='color: #38bdf8; font-size: 1.1rem;'>{cat_name}</strong>", unsafe_allow_html=True)
            
    #         b_cols = st.columns(min(len(skill_list), 3))
    #         for idx, skill in enumerate(skill_list):
    #             with b_cols[idx % 3]:
    #                 if st.button(skill, key=f"btn_skill_{cat_name}_{skill}"):
    #                     st.session_state['selected_tech_desc'] = skill
    #                     st.rerun()
    #         st.markdown("<br>", unsafe_allow_html=True)

# TAB 2: PROJECTS
with tab2:
    st.markdown("### 🚀 Featured Systems & Case Studies")
    
    search_query = st.text_input("🔍 Filter Projects by Keyword (e.g. FastAPI, RAG, React, Healthcare)...")
    
    for proj in PROFILE["projects"]:
        match_search = (
            not search_query.strip() or 
            search_query.lower() in proj["title"].lower() or 
            search_query.lower() in proj["summary"].lower() or 
            any(search_query.lower() in t.lower() for t in proj["tech"])
        )
        
        if match_search:
            bullet_points = "".join([f'<li style="color: #ffffff !important; margin-bottom: 8px; line-height: 1.7; font-weight: 600;">{pt}</li>' for pt in proj["points"]])
            
            st.markdown(
                f'''
                <div class="saas-card">
                    <span style="font-size: 0.85rem; font-weight: 900; text-transform: uppercase; letter-spacing: 1.2px; color: #38bdf8;">{proj["category"]}</span>
                    <h3 style="margin-top: 4px; margin-bottom: 6px; color: #ffffff !important; font-weight: 900; font-size: 1.4rem;">{proj["title"]}</h3>
                    <p style="color: #ffffff !important; font-size: 1.08rem !important; margin-top: 4px; margin-bottom: 14px; font-weight: 600;">{proj["summary"]}</p>
                </div>
                ''',
                unsafe_allow_html=True
            )
            
            # Interactive Tech Stack Buttons for each project
            st.markdown("**Tech Stack:**")
            p_cols = st.columns(min(len(proj["tech"]), 4))
            for p_idx, t_name in enumerate(proj["tech"]):
                with p_cols[p_idx % 4]:
                    if st.button(t_name, key=f"btn_proj_{proj['title'][:6]}_{t_name}"):
                        st.session_state['selected_tech_desc'] = t_name
                        st.rerun()
            
            st.markdown(
                f'''
                <details style="cursor: pointer; color: #38bdf8; font-weight: 800; font-size: 1.02rem; margin-top: 12px;">
                    <summary>View Complete Technical Architecture & Key Deliverables ▼</summary>
                    <ul style="padding-left: 20px; margin-top: 12px; margin-bottom: 0;">
                        {bullet_points}
                    </ul>
                </details>
                <br>
                ''',
                unsafe_allow_html=True
            )

# TAB 3: AI JOB DESCRIPTION MATCHER
with tab3:
    st.markdown("### 🎯 Real-Time AI Job Description Skill Matcher")
    st.write("Recruiters & Hiring Managers: Paste your Job Description (JD) below to instantly evaluate skill match compatibility against Vedang's profile!")
    
    jd_input = st.text_area("Paste Job Description (JD) Content", height=180, placeholder="We are looking for an AI & Automation Engineer skilled in Python, FastAPI, LangChain, RAG, Docker, and PostgreSQL...")
    
    if st.button("⚡ Calculate Match Score", type="primary"):
        if jd_input.strip():
            all_profile_skills = list(TECH_DESCRIPTIONS.keys())
            matched = [s for s in all_profile_skills if re.search(r'\b' + re.escape(s) + r'\b', jd_input, re.IGNORECASE)]
            unmatched = [s for s in all_profile_skills if s not in matched]
            
            match_score = min(100, int((len(matched) / max(len(matched) + 3, 5)) * 100))
            
            st.markdown(
                f'''
                <div class="saas-card" style="text-align: center; background: #0f172a !important;">
                    <h2 style="font-size: 3.4rem; margin: 0; font-weight: 900; color: #34d399 !important;">{match_score}% Skill Alignment</h2>
                    <p style="color: #ffffff !important; font-weight: 800; margin-top: 6px; font-size: 1.15rem;">High Compatibility with Vedang Dhuri's Technical Background!</p>
                </div>
                ''',
                unsafe_allow_html=True
            )
            
            col_m, col_um = st.columns(2)
            with col_m:
                st.markdown("#### ✅ Matching Requirements Found")
                for s in matched:
                    if st.button(f"✅ {s}", key=f"btn_match_{s}"):
                        st.session_state['selected_tech_desc'] = s
                        st.rerun()
            with col_um:
                st.markdown("#### 💡 Additional Profile Capabilities")
                for s in unmatched[:6]:
                    if st.button(f"🔹 {s}", key=f"btn_unmatch_{s}"):
                        st.session_state['selected_tech_desc'] = s
                        st.rerun()

import textwrap

# TAB 4: EXPERIENCE & EDUCATION
with tab4:
    col_exp, col_edu = st.columns(2)
    
    with col_exp:
        st.markdown("### 💼 Experience")
        for exp in PROFILE["experience"]:
            exp_bullets = "".join([f'<li style="color: #cbd5e1 !important; font-size: 0.95rem !important; line-height: 1.6; margin-bottom: 4px;">{b}</li>' for b in exp["details"]])
            
            # String starts strictly flush without any tabs/spaces inside
            html_exp = f"""<div style="border-left: 4px solid #38bdf8; padding-left: 20px; margin-left: 8px; margin-bottom: 22px;">
<h4 style="margin: 0; color: #38bdf8 !important; font-weight: 900;">{exp["role"]}</h4>
<p style="margin: 2px 0 8px 0; color: #818cf8 !important; font-weight: 800;">{exp["company"]}</p>
<ul style="padding-left: 18px; margin: 0;">
{exp_bullets}
</ul>
</div>"""
            st.markdown(html_exp, unsafe_allow_html=True)

    with col_edu:
        st.markdown("### 🎓 Education")
        for edu in PROFILE["education"]:
            honors_html = f'<p style="margin: 4px 0 2px 0; color: #c084fc !important; font-weight: 800; font-size: 0.95rem;">{edu["honors"]}</p>' if "honors" in edu else ''
            
            # String starts strictly flush without any tabs/spaces inside
            html_edu = f"""<div style="background-color: #0f172a; border: 1px solid #1e293b; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<h4 style="margin: 0; color: #38bdf8 !important; font-weight: 900;">{edu["degree"]}</h4>
{honors_html}
<p style="margin: 2px 0 10px 0; color: #f8fafc !important; font-weight: 600; font-size: 0.95rem;">{edu["institution"]}</p>
<div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #1e293b; padding-top: 8px; margin-top: 8px;">
<span style="color: #818cf8 !important; font-weight: 800; font-size: 0.90rem;">📅 {edu["period"]}</span>
<span style="color: #38bdf8 !important; font-weight: 800; font-size: 0.90rem;">{edu["grade"]}</span>
</div>
</div>"""
            st.markdown(html_edu, unsafe_allow_html=True)
# TAB 5: PUBLICATIONS & CERTIFICATIONS
with tab5:
    st.markdown("### 📜 Research & Publications")
    pub = PROFILE["publication"]
    st.markdown(
        f'''
        <div class="saas-card">
            <span style="color: #38bdf8 !important; font-weight: 900; font-size: 0.9rem;">National Conference Paper (ETTS-2026)</span>
            <h3 style="margin-top: 12px; margin-bottom: 6px; color: #ffffff !important; font-weight: 900;">{pub["title"]}</h3>
            <p style="color: #818cf8 !important; font-weight: 800; margin-bottom: 12px;">🏛️ {pub["conference"]}</p>
            <p style="color: #ffffff !important; line-height: 1.7; margin-bottom: 0; font-weight: 600;">{pub["abstract"]}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    st.markdown("### 🏆 Professional Certifications & Achievements")
    for cert in PROFILE["certifications"]:
        st.markdown(
            f'''
            <div class="saas-card" style="padding: 20px; margin-bottom: 14px;">
                <h4 style="margin: 0; color: #38bdf8 !important; font-weight: 900;">🥇 {cert["name"]}</h4>
                <p style="margin-top: 6px; margin-bottom: 0; color: #ffffff !important; font-size: 1rem !important; line-height: 1.6; font-weight: 600;">{cert["desc"]}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

# TAB 6: WORK WITH VEDANG
with tab6:
    st.markdown("### 📬 Schedule a Technical Discussion / Project Inquiry")
    
    col_info, col_form = st.columns([1, 1.1])
    
    with col_info:
        st.markdown(
            f'''
            <div class="saas-card">
                <h3 style="color: #ffffff !important; font-weight: 900; margin-top: 0;">Vedang Rajendra Dhuri</h3>
                <p style="color: #38bdf8 !important; font-weight: 800; font-size: 1.1rem;">AI & Automation Engineer</p>
                <p style="color: #ffffff !important; font-weight: 600;">Specializing in AI Agents, RAG Architectures, FastAPI Microservices & n8n Enterprise Workflows.</p>
                <hr style="border-color: rgba(255,255,255,0.15); margin: 16px 0;">
                <p>📍 <strong>Location:</strong> {PROFILE["location"]}</p>
                <p>📧 <strong>Email:</strong> <a href="mailto:{PROFILE['email']}" style="color: #38bdf8 !important; font-weight: 800;">{PROFILE["email"]}</a></p>
                <p>📞 <strong>Phone:</strong> {PROFILE["phone"]}</p>
                <p>💼 <strong>LinkedIn:</strong> <a href="{PROFILE['linkedin']}" target="_blank" style="color: #818cf8 !important; font-weight: 800;">linkedin.com/in/vedanggg</a></p>
                <p>💻 <strong>GitHub:</strong> <a href="{PROFILE['github']}" target="_blank" style="color: #818cf8 !important; font-weight: 800;">github.com/Vedang07-eng</a></p>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
    with col_form:
        with st.form("contact_form_saas_final_v3"):
            st.markdown("#### Initiate Contact / Engagement")
            s_name = st.text_input("Your Full Name / Organization")
            s_email = st.text_input("Your Business Email")
            topic = st.selectbox("Engagement Type", ["Full-Time AI Engineering Role", "AI Agent / RAG System Consulting", "Workflow Automation Project", "General Technical Inquiry"])
            s_msg = st.text_area("Project / Role Details", height=110)
            submitted = st.form_submit_button("🚀 Submit Inquiry", type="primary")
            if submitted:
                st.success(f"Thank you {s_name}! Your inquiry regarding '{topic}' has been dispatched to Vedang Dhuri.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f'''
        <div class="saas-card" style="border-style: dashed; border-color: rgba(56, 189, 248, 0.4);">
            <h4 style="margin-top: 0; color: #38bdf8 !important; font-weight: 800;">📌 Formal Declaration</h4>
            <p style="color: #ffffff !important; font-style: italic; font-size: 1rem !important; font-weight: 600;">"{PROFILE['declaration']['text']}"</p>
            <div style="display: flex; justify-content: space-between; margin-top: 12px; color: #818cf8 !important; font-weight: 800; font-size: 0.95rem;">
                <span>📍 Place: {PROFILE['declaration']['place']}</span>
                <span>📅 Date: {PROFILE['declaration']['date']}</span>
                <span>✍️ Signature: {PROFILE['declaration']['name']}</span>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# Footer
st.divider()
st.markdown(
    '<p style="text-align: center; color: #cbd5e1; font-size: 0.9rem; font-weight: 700;">Vedang Rajendra Dhuri • AI & Automation Engineer • </p>',
    unsafe_allow_html=True
)
