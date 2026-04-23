"""
Personal Website - Luqi Dong
Multi-page Flask Application with Project Details
"""

from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

# ===== 项目数据 =====
PROJECTS = [
    {
        "id": 1,
        "title": "Shared Mobility User Behavior Analysis",
        "category": "Data Science & GIS",
        "location": "University of Twente",
        "date": "2021 - Present",
        "excerpt": "Analyzed 100,000+ GPS trajectories from shared e-scooter and bike systems",
        "icon": "📍",
        "image_url": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>This project focuses on understanding shared mobility user behavior through large-scale GPS trajectory data analysis.</p>
        
        <h4>Key Achievements:</h4>
        <ul>
            <li>Processed and analyzed 100,000+ GPS trajectories from e-scooter and e-bike systems</li>
            <li>Developed data cleaning pipelines to handle noisy GPS data</li>
            <li>Implemented clustering algorithms to identify trip patterns</li>
            <li>Created interactive visualizations showing usage hotspots</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>Python</span>
            <span>GeoPandas</span>
            <span>Shapely</span>
            <span>Folium</span>
            <span>DBSCAN Clustering</span>
            <span>PostGIS</span>
            <span>PostgreSQL</span>
        </div>
        
        <h4>Impact:</h4>
        <p>The insights from this analysis have been used to optimize bike station placement and improve operational efficiency of shared mobility operators in Europe.</p>
        """,
        "links": [
            {"label": "Research Paper", "url": "#"},
            {"label": "GitHub Code", "url": "https://github.com/rockyistt"},
            {"label": "Live Dashboard", "url": "#"}
        ]
    },
    {
        "id": 2,
        "title": "Travel Mode Choice Prediction",
        "category": "Machine Learning",
        "location": "Research Project",
        "date": "2022 - 2023",
        "excerpt": "ML models for predicting transportation mode preferences with 85% accuracy",
        "icon": "🚗",
        "image_url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>Built advanced machine learning models to predict which transportation mode (car, public transit, bike, walk) a person would choose for a trip.</p>
        
        <h4>Key Achievements:</h4>
        <ul>
            <li>Developed Random Forest and Neural Network models</li>
            <li>Achieved 85% prediction accuracy on test dataset</li>
            <li>Feature engineering from raw trip data (time, distance, weather, etc.)</li>
            <li>Hyperparameter optimization using GridSearchCV</li>
            <li>Model interpretability analysis using SHAP values</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>Python</span>
            <span>Scikit-learn</span>
            <span>XGBoost</span>
            <span>TensorFlow</span>
            <span>SHAP</span>
            <span>Jupyter</span>
        </div>
        
        <h4>Key Findings:</h4>
        <p>Trip distance, time of day, and weather conditions were the most influential factors in mode choice. The model successfully captured non-linear relationships between features.</p>
        """,
        "links": [
            {"label": "Paper (Submitted)", "url": "#"},
            {"label": "Dataset", "url": "#"},
            {"label": "Code Repository", "url": "https://github.com/rockyistt"}
        ]
    },
    {
        "id": 3,
        "title": "GPS Trajectory Data Pipeline",
        "category": "Data Engineering",
        "location": "Technical Infrastructure",
        "date": "2023 - Present",
        "excerpt": "ETL pipeline for processing GPS trajectory data at scale",
        "icon": "🔄",
        "image_url": "https://images.unsplash.com/photo-1460925895917-aaf4e88b6e5f?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>Developed a robust ETL (Extract, Transform, Load) pipeline for processing GPS trajectory data from multiple sources at scale.</p>
        
        <h4>Key Achievements:</h4>
        <ul>
            <li>Handles data from 50+ cities with different data formats</li>
            <li>Processes 10+ million GPS points daily</li>
            <li>Automatic data quality checks and anomaly detection</li>
            <li>Interactive visualizations with Folium and Matplotlib</li>
            <li>Scalable architecture for real-time processing</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>Apache Airflow</span>
            <span>Python</span>
            <span>PostgreSQL</span>
            <span>PostGIS</span>
            <span>Docker</span>
            <span>Folium</span>
            <span>Matplotlib</span>
        </div>
        
        <h4>Technical Details:</h4>
        <p>The pipeline includes data validation, deduplication, map-matching, and spatial indexing. It can handle edge cases like GPS noise, gaps in data, and sensor failures.</p>
        """,
        "links": [
            {"label": "Architecture Diagram", "url": "#"},
            {"label": "GitHub Repository", "url": "https://github.com/rockyistt"},
            {"label": "Technical Blog", "url": "#"}
        ]
    },
    {
        "id": 4,
        "title": "ArcGIS Test Automation Framework",
        "category": "QA & Automation",
        "location": "Accenture",
        "date": "2025 - Present",
        "excerpt": "Comprehensive test automation framework for GIS applications with 90% coverage",
        "icon": "🧪",
        "image_url": "https://images.unsplash.com/photo-1516534775068-bb6c2dc8a755?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>Designed and implemented a comprehensive test automation framework for enterprise GIS applications at Accenture.</p>
        
        <h4>Key Achievements:</h4>
        <ul>
            <li>Achieved 90% test coverage across critical features</li>
            <li>Reduced manual testing time by 70%</li>
            <li>Integrated with CI/CD pipeline for continuous testing</li>
            <li>Created reusable test libraries for GIS operations</li>
            <li>Implemented visual regression testing</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>Python</span>
            <span>Selenium</span>
            <span>ArcGIS API</span>
            <span>pytest</span>
            <span>Jenkins</span>
            <span>Docker</span>
            <span>Git</span>
        </div>
        
        <h4>Business Impact:</h4>
        <p>The automation framework improved code quality, reduced bugs in production, and enabled faster release cycles.</p>
        """,
        "links": [
            {"label": "Internal Documentation", "url": "#"},
            {"label": "Test Reports", "url": "#"},
            {"label": "Framework Guide", "url": "#"}
        ]
    },
    {
        "id": 5,
        "title": "LLM Fine-tuning for Transport Domain",
        "category": "AI & NLP",
        "location": "Research",
        "date": "2025 - Present",
        "excerpt": "Fine-tuning large language models for transport-specific NLP tasks",
        "icon": "🤖",
        "image_url": "https://images.unsplash.com/photo-1677442d019cecf3d69f4a2ce457dcb3acf3a5340?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>Working on adapting large language models to understand and analyze transport-domain-specific text and documents.</p>
        
        <h4>Current Work:</h4>
        <ul>
            <li>Fine-tuning Llama 2 and Mistral models on transport documents</li>
            <li>Using LoRA and QLoRA for efficient training</li>
            <li>Building RAG (Retrieval-Augmented Generation) system for transport Q&A</li>
            <li>Creating domain-specific vocabulary and embeddings</li>
            <li>Benchmark testing against baseline models</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>PyTorch</span>
            <span>Hugging Face</span>
            <span>Llama 2</span>
            <span>LoRA</span>
            <span>Transformers</span>
            <span>LangChain</span>
            <span>FAISS</span>
        </div>
        
        <h4>Expected Outcomes:</h4>
        <p>A fine-tuned LLM capable of analyzing transport data, answering domain-specific questions, and assisting in research document analysis.</p>
        """,
        "links": [
            {"label": "Project Proposal", "url": "#"},
            {"label": "Progress Notes", "url": "#"},
            {"label": "Code (GitHub)", "url": "https://github.com/rockyistt"}
        ]
    },
    {
        "id": 6,
        "title": "Interactive Dashboard Platform",
        "category": "Data Visualization",
        "location": "Multiple Projects",
        "date": "2022 - Present",
        "excerpt": "Real-time dashboards for stakeholder reporting and KPI tracking",
        "icon": "📊",
        "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=300&fit=crop",
        "description": """
        <h3>Project Overview</h3>
        <p>Developed multiple interactive dashboards for data visualization and stakeholder reporting across various projects.</p>
        
        <h4>Key Achievements:</h4>
        <ul>
            <li>Built 10+ interactive dashboards using Power BI and Python</li>
            <li>Real-time data refresh every 5 minutes</li>
            <li>Custom KPI calculations and business logic</li>
            <li>User-friendly filtering and drill-down capabilities</li>
            <li>Mobile-responsive design</li>
        </ul>
        
        <h4>Technologies Used:</h4>
        <div class="tech-tags">
            <span>Power BI</span>
            <span>Plotly</span>
            <span>Dash</span>
            <span>Python</span>
            <span>PostgreSQL</span>
            <span>Matplotlib</span>
            <span>Seaborn</span>
        </div>
        
        <h4>Use Cases:</h4>
        <p>Dashboards track shared mobility usage patterns, transport efficiency metrics, travel demand forecasts, and operational KPIs for multiple stakeholder groups.</p>
        """,
        "links": [
            {"label": "Dashboard Gallery", "url": "#"},
            {"label": "Case Studies", "url": "#"},
            {"label": "Tableau Public", "url": "#"}
        ]
    }
]

# ===== HTML模板 =====
BASE_STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #2c3e50;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
    }
    
    .wrapper {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* 导航栏 */
    nav {
        background: rgba(255, 255, 255, 0.95);
        padding: 1rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
        text-decoration: none;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
        list-style: none;
    }
    
    .nav-links a {
        text-decoration: none;
        color: #2c3e50;
        font-weight: 500;
        transition: color 0.3s;
    }
    
    .nav-links a:hover, .nav-links a.active {
        color: #667eea;
    }
    
    /* 主容器 */
    .container {
        background: white;
        border-radius: 16px;
        padding: 4rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        animation: slideUp 0.6s ease-out;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .back-btn {
        display: inline-block;
        margin-bottom: 2rem;
        padding: 0.8rem 1.5rem;
        background: #f0f0f0;
        color: #667eea;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .back-btn:hover {
        background: #667eea;
        color: white;
    }
    
    h1 {
        font-size: 2.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-size: 2rem;
        color: #667eea;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 3px solid #667eea;
    }
    
    h3 {
        font-size: 1.3rem;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h4 {
        font-size: 1rem;
        color: #667eea;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }
    
    p {
        line-height: 1.8;
        color: #555;
        margin-bottom: 1rem;
    }
    
    ul, ol {
        margin-left: 2rem;
        margin-bottom: 1rem;
    }
    
    li {
        margin-bottom: 0.5rem;
        color: #555;
    }
    
    /* 项目卡片 */
    .project-card {
        background: #f9fafb;
        border: 1px solid #e8e8e8;
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.15);
        border-color: #667eea;
    }
    
    .project-card-image {
        width: 100%;
        height: 200px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 60px;
        color: white;
        overflow: hidden;
    }
    
    .project-card-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .project-card-content {
        padding: 2rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
    
    .project-category {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
        width: fit-content;
    }
    
    .project-card h3 {
        margin-top: 0;
        color: #2c3e50;
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    .project-meta {
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
        color: #95a5a6;
        margin-bottom: 1rem;
    }
    
    .project-description {
        color: #555;
        font-size: 0.95rem;
        line-height: 1.6;
        flex-grow: 1;
        margin-bottom: 1.5rem;
    }
    
    .project-link {
        display: inline-block;
        color: #667eea;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s;
    }
    
    .project-link:hover {
        color: #764ba2;
    }
    
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    /* 项目详情页 */
    .project-detail-header {
        display: flex;
        gap: 2rem;
        margin-bottom: 3rem;
        align-items: flex-start;
    }
    
    .project-detail-image {
        width: 300px;
        height: 250px;
        border-radius: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 120px;
        flex-shrink: 0;
        overflow: hidden;
    }
    
    .project-detail-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .project-detail-info h1 {
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }
    
    .project-detail-meta {
        display: flex;
        gap: 2rem;
        margin-bottom: 1.5rem;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .meta-item {
        display: flex;
        flex-direction: column;
    }
    
    .meta-label {
        font-size: 0.9rem;
        color: #95a5a6;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    
    .meta-value {
        font-size: 1.1rem;
        color: #667eea;
        font-weight: 600;
    }
    
    /* 技术标签 */
    .tech-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .tech-tags span {
        background: white;
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        border: 2px solid #667eea;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* 链接 */
    .project-links {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 2px solid #f0f0f0;
    }
    
    .project-links a {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        background: #667eea;
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .project-links a:hover {
        background: #764ba2;
        transform: translateY(-2px);
    }
    
    /* 底部 */
    footer {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 4rem;
        color: #7f8c8d;
    }
    
    footer a {
        color: #667eea;
        text-decoration: none;
    }
    
    footer a:hover {
        text-decoration: underline;
    }
    
    /* 响应式 */
    @media (max-width: 768px) {
        nav { flex-direction: column; gap: 1rem; }
        .nav-links { flex-direction: column; gap: 0.5rem; }
        .container { padding: 2rem; }
        h1 { font-size: 2rem; }
        .project-detail-header { flex-direction: column; }
        .project-detail-image { width: 100%; }
        .projects-grid { grid-template-columns: 1fr; }
    }
</style>
"""

# ===== 首页模板 =====
HOME_TEMPLATE = f"""
<!-- VERSION -->
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luqi Dong - Personal Website</title>
    {BASE_STYLE}
</head>
<body>
<div class="wrapper">
    <div style="background: linear-gradient(135deg, #f39c12, #e67e22); color: white; padding: 15px; border-radius: 12px; margin-bottom: 15px; font-weight: bold; text-align: center; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(243, 156, 18, 0.3);">
        ✨ NEW WEBSITE V3.0 - Projects Now Visible! 🚀
    </div>
    
    <nav>
        <a href="/" class="logo">👨‍💻 Luqi</a>
        <ul class="nav-links">
            <li><a href="/" class="active">Home</a></li>
            <li><a href="/#projects">Projects</a></li>
            <li><a href="/#skills">Skills</a></li>
        </ul>
    </nav>
    
    <div class="container">
        <h1>Luqi Dong</h1>
        <p style="font-size: 1.3rem; color: #7f8c8d; margin-bottom: 2rem;">
            🤖 AI Solutions Engineer | 📊 Data Scientist | 🗺️ GIS Specialist
        </p>
        
        <p style="color: #555; line-height: 1.8; font-size: 1.05rem; margin-bottom: 3rem;">
            PhD Researcher at University of Twente specializing in transport modelling and shared mobility behavior. 
            Passionate about applying AI/LLM and advanced data science techniques to solve real-world problems.
        </p>
        
        <h2 id="projects">🚀 Featured Projects</h2>
        <p style="margin-bottom: 2rem; color: #666;">Click on any project to view detailed information</p>
        
        <div class="projects-grid">
            {''.join(f'''
            <a href="/project/{p["id"]}" style="text-decoration: none;">
                <div class="project-card">
                    <div class="project-card-image">{p["icon"]}</div>
                    <div class="project-card-content">
                        <span class="project-category">{p["category"]}</span>
                        <h3>{p["title"]}</h3>
                        <div class="project-meta">
                            <span>📍 {p["location"]}</span>
                            <span>📅 {p["date"]}</span>
                        </div>
                        <p class="project-description">{p["excerpt"]}</p>
                        <span class="project-link">View Details →</span>
                    </div>
                </div>
            </a>
            ''' for p in PROJECTS)}
        </div>
        
        <h2 id="skills">🔧 Skills & Expertise</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
            <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                <h4>🤖 AI & Machine Learning</h4>
                <div class="tech-tags">
                    <span>LLMs</span>
                    <span>Fine-tuning</span>
                    <span>RAG</span>
                    <span>PyTorch</span>
                    <span>Hugging Face</span>
                </div>
            </div>
            <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                <h4>📊 Data Science</h4>
                <div class="tech-tags">
                    <span>Python</span>
                    <span>SQL</span>
                    <span>Scikit-learn</span>
                    <span>Statistics</span>
                    <span>R</span>
                </div>
            </div>
            <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                <h4>🗺️ GIS & Spatial</h4>
                <div class="tech-tags">
                    <span>ArcGIS</span>
                    <span>GeoPandas</span>
                    <span>Folium</span>
                    <span>PostGIS</span>
                </div>
            </div>
        </div>
    </div>
    
    <footer>
        <p>Made with ❤️ by Luqi Dong | © 2026 | 
            <a href="https://github.com/rockyistt" target="_blank">GitHub</a>
        </p>
    </footer>
</div>
</body>
</html>
"""

# ===== 项目详情模板 =====
PROJECT_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${{title}} - Luqi Dong</title>
    {BASE_STYLE}
</head>
<body>
<div class="wrapper">
    <nav>
        <a href="/" class="logo">👨‍💻 Luqi</a>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/#projects">Projects</a></li>
            <li><a href="/#skills">Skills</a></li>
        </ul>
    </nav>
    
    <div class="container">
        <a href="/" class="back-btn">← Back to Home</a>
        
        <div class="project-detail-header">
            <div class="project-detail-image">${{icon}}</div>
            <div class="project-detail-info">
                <h1>${{title}}</h1>
                <div class="project-detail-meta">
                    <div class="meta-item">
                        <span class="meta-label">Category</span>
                        <span class="meta-value">${{category}}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Location</span>
                        <span class="meta-value">${{location}}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Duration</span>
                        <span class="meta-value">${{date}}</span>
                    </div>
                </div>
            </div>
        </div>
        
        ${{description}}
        
        <div class="project-links">
            {f'''${{links_html}}''' if "${{links_html}}" else ""}
        </div>
    </div>
    
    <footer>
        <p>Made with ❤️ by Luqi Dong | © 2026</p>
    </footer>
</div>
</body>
</html>
"""

# ===== Flask路由 =====
@app.route("/")
def home():
    # Version marker - force Vercel to recognize new deployment
    return HOME_TEMPLATE.replace("<!-- VERSION -->", "<!-- Version 3.0: Multi-page with projects -->")

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    
    if not project:
        return "<h1>Project not found</h1>", 404
    
    links_html = "".join(f'''<a href="{link['url']}" target="_blank">{link['label']}</a>''' 
                         for link in project.get("links", []))
    
    html = PROJECT_TEMPLATE
    html = html.replace("${title}", project["title"])
    html = html.replace("${category}", project["category"])
    html = html.replace("${location}", project["location"])
    html = html.replace("${date}", project["date"])
    html = html.replace("${icon}", project["icon"])
    html = html.replace("${description}", project["description"])
    html = html.replace("${links_html}", links_html)
    
    return html

@app.route("/health")
def health():
    return {"status": "ok", "message": "Server is running"}, 200

if __name__ == "__main__":
    app.run(debug=False)
"""
Personal Website - Luqi Dong
Modern Multi-page Flask Application
"""

from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luqi Dong - Personal Website</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .wrapper {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* 导航栏 */
        nav {
            background: rgba(255, 255, 255, 0.95);
            padding: 1rem 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #667eea;
            text-decoration: none;
        }
        
        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }
        
        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover, .nav-links a.active {
            color: #667eea;
        }
        
        /* 主容器 */
        .container {
            background: white;
            border-radius: 16px;
            padding: 4rem;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            animation: slideUp 0.6s ease-out;
        }
        
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* 英雄部分 */
        .hero {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
            margin-bottom: 4rem;
            padding-bottom: 3rem;
            border-bottom: 2px solid #f0f0f0;
        }
        
        .hero-content h1 {
            font-size: 3.5rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            line-height: 1.2;
        }
        
        .hero-content .subtitle {
            font-size: 1.3rem;
            color: #7f8c8d;
            margin-bottom: 1.5rem;
        }
        
        .badges {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }
        
        .badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }
        
        .avatar {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            padding: 3px;
            aspect-ratio: 1;
        }
        
        .avatar-placeholder {
            width: 100%;
            height: 100%;
            border-radius: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 80px;
            color: white;
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
        }
        
        .social-links a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            background: #f0f0f0;
            border-radius: 50%;
            text-decoration: none;
            color: #667eea;
            transition: all 0.3s;
            font-size: 1.5rem;
        }
        
        .social-links a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-3px);
        }
        
        /* 标题 */
        h2 {
            font-size: 2rem;
            color: #667eea;
            margin-bottom: 2rem;
            margin-top: 3rem;
            padding-bottom: 1rem;
            border-bottom: 3px solid #667eea;
        }
        
        h3 {
            font-size: 1.3rem;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        /* 卡片网格 */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .card {
            background: #f9fafb;
            border-left: 4px solid #667eea;
            padding: 2rem;
            border-radius: 12px;
            transition: all 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.1);
            background: white;
        }
        
        .card-label {
            color: #667eea;
            font-weight: 600;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
        }
        
        .card-title {
            font-size: 1.15rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        .card-date {
            color: #95a5a6;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        
        .card p {
            color: #555;
            line-height: 1.6;
        }
        
        .card ul {
            margin-left: 1rem;
            margin-top: 0.5rem;
        }
        
        .card li {
            margin-bottom: 0.3rem;
            color: #555;
        }
        
        /* 技能网格 */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .skill-category {
            background: #f9fafb;
            padding: 2rem;
            border-radius: 12px;
            border-top: 3px solid #667eea;
        }
        
        .skill-category h4 {
            color: #667eea;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        
        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
        }
        
        .skill-tag {
            background: white;
            color: #667eea;
            padding: 0.6rem 1.2rem;
            border-radius: 20px;
            border: 2px solid #667eea;
            font-size: 0.9rem;
            transition: all 0.3s;
        }
        
        .skill-tag:hover {
            background: #667eea;
            color: white;
        }
        
        /* 底部 */
        footer {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 4rem;
            color: #7f8c8d;
        }
        
        footer a {
            color: #667eea;
            text-decoration: none;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        /* 响应式 */
        @media (max-width: 768px) {
            nav { flex-direction: column; gap: 1rem; }
            .nav-links { flex-direction: column; gap: 0.5rem; }
            .container { padding: 2rem; }
            .hero { grid-template-columns: 1fr; }
            h1 { font-size: 2.5rem; }
            h2 { font-size: 1.5rem; }
        }
    </style>
</head>
<body>
<div class="wrapper">
    <!-- 导航 -->
    <nav>
        <a href="/" class="logo">👨‍💻 Luqi</a>
        <ul class="nav-links">
            <li><a href="/" class="active">Home</a></li>
            <li><a href="/#experiences">Experience</a></li>
            <li><a href="/#projects">Projects</a></li>
            <li><a href="/#skills">Skills</a></li>
        </ul>
    </nav>
    
    <!-- 主容器 -->
    <div class="container">
        <!-- 英雄部分 -->
        <div class="hero">
            <div class="hero-content">
                <h1>Luqi Dong</h1>
                <p class="subtitle">AI Solutions Engineer & Data Scientist</p>
                <div class="badges">
                    <span class="badge">🤖 LLM & AI</span>
                    <span class="badge">🗺️ GIS</span>
                    <span class="badge">📊 Data Science</span>
                    <span class="badge">🚗 Transport Modeling</span>
                </div>
                <p style="color: #555; line-height: 1.8; margin-bottom: 1.5rem;">
                    PhD Researcher at University of Twente specializing in transport modelling and shared mobility behavior. 
                    Passionate about applying AI/LLM and advanced data science techniques to solve real-world problems.
                </p>
                <div class="social-links">
                    <a href="https://github.com/rockyistt" target="_blank" title="GitHub">🐙</a>
                    <a href="https://linkedin.com/in/luqi-dong" target="_blank" title="LinkedIn">💼</a>
                    <a href="mailto:l.dong@utwente.nl" target="_blank" title="Email">✉️</a>
                </div>
            </div>
            <div class="avatar">
                <div class="avatar-placeholder">🎓</div>
            </div>
        </div>
        
        <!-- 工作经历 -->
        <h2 id="experiences">💼 Experience</h2>
        <div class="cards-grid">
            <div class="card">
                <div class="card-label">Accenture NL</div>
                <h3 class="card-title">Data & NLP Engineer</h3>
                <p class="card-date">Nov 2025 - Mar 2026</p>
                <p>Industry X Division - Developing enterprise AI solutions with focus on:</p>
                <ul>
                    <li>GIS test automation and integration</li>
                    <li>LLM fine-tuning and RAG implementation</li>
                    <li>Production-grade ML deployment</li>
                </ul>
            </div>
            
            <div class="card">
                <div class="card-label">University of Twente</div>
                <h3 class="card-title">PhD Researcher</h3>
                <p class="card-date">Oct 2021 - Present</p>
                <p>Transport Engineering & Management Department:</p>
                <ul>
                    <li>Shared mobility user behavior analysis</li>
                    <li>Mode choice modeling with ML</li>
                    <li>GPS trajectory data analysis</li>
                </ul>
            </div>
            
            <div class="card">
                <div class="card-label">Beijing Jiaotong University</div>
                <h3 class="card-title">Research Assistant</h3>
                <p class="card-date">2018 - 2021</p>
                <p>Transport Planning Research:</p>
                <ul>
                    <li>Urban transport modelling</li>
                    <li>Travel behavior studies</li>
                    <li>Data visualization & analysis</li>
                </ul>
            </div>
        </div>
        
        <!-- 教育背景 -->
        <h2>🎓 Education</h2>
        <div class="cards-grid">
            <div class="card">
                <div class="card-label">University of Twente, Netherlands</div>
                <h3 class="card-title">PhD Transport Engineering</h3>
                <p class="card-date">Oct 2021 - Present (Ongoing)</p>
                <p>Research on shared mobility systems and travel behavior modeling using advanced data science and machine learning techniques.</p>
            </div>
            
            <div class="card">
                <div class="card-label">Beijing Jiaotong University, China</div>
                <h3 class="card-title">Master's in Transport Planning</h3>
                <p class="card-date">Sep 2018 - Jun 2021</p>
                <p>Specialized in urban transport systems, travel demand modeling, and transportation data analysis.</p>
            </div>
        </div>
        
        <!-- 项目 -->
        <h2 id="projects">🚀 Projects</h2>
        <div class="cards-grid">
            <div class="card">
                <h3 class="card-title">Shared Mobility User Behavior Analysis</h3>
                <p class="card-date">University of Twente</p>
                <p>Analyzed 100,000+ GPS trajectories from shared e-scooter and bike systems using Python (GeoPandas, PyTorch). 
                Developed machine learning models to predict usage patterns and optimize system operations.</p>
            </div>
            
            <div class="card">
                <h3 class="card-title">Travel Mode Choice Prediction</h3>
                <p class="card-date">Research Project</p>
                <p>Built predictive models using Random Forest and Neural Networks to forecast transportation mode preferences. 
                Achieved 85% accuracy with feature engineering and hyperparameter optimization.</p>
            </div>
            
            <div class="card">
                <h3 class="card-title">GPS Trajectory Data Pipeline</h3>
                <p class="card-date">Data Engineering</p>
                <p>Developed ETL pipeline for processing and analyzing GPS trajectory data at scale. 
                Created interactive visualizations using Folium and Matplotlib for spatial analysis.</p>
            </div>
            
            <div class="card">
                <h3 class="card-title">ArcGIS Test Automation Framework</h3>
                <p class="card-date">Accenture Project</p>
                <p>Designed and implemented comprehensive test automation framework for GIS applications. 
                Integrated with CI/CD pipelines and achieved 90% test coverage.</p>
            </div>
            
            <div class="card">
                <h3 class="card-title">LLM Fine-tuning for Domain Tasks</h3>
                <p class="card-date">In Progress</p>
                <p>Working on fine-tuning large language models for transport domain-specific tasks. 
                Using LoRA and QLoRA techniques for efficient training on consumer hardware.</p>
            </div>
            
            <div class="card">
                <h3 class="card-title">Interactive Dashboard Platform</h3>
                <p class="card-date">Multiple Projects</p>
                <p>Built interactive dashboards using Power BI and Python (Plotly, Dash) for stakeholder reporting. 
                Real-time data visualization and KPI tracking.</p>
            </div>
        </div>
        
        <!-- 技能 -->
        <h2 id="skills">🔧 Skills & Expertise</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h4>🤖 AI & Machine Learning</h4>
                <div class="skill-tags">
                    <span class="skill-tag">LLMs (GPT, Llama)</span>
                    <span class="skill-tag">RAG Systems</span>
                    <span class="skill-tag">Fine-tuning</span>
                    <span class="skill-tag">PyTorch</span>
                    <span class="skill-tag">Hugging Face</span>
                    <span class="skill-tag">LoRA/QLoRA</span>
                    <span class="skill-tag">Transformers</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h4>📊 Data Science</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">Pandas</span>
                    <span class="skill-tag">NumPy</span>
                    <span class="skill-tag">Scikit-learn</span>
                    <span class="skill-tag">Statistical Modeling</span>
                    <span class="skill-tag">SQL</span>
                    <span class="skill-tag">R</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h4>🗺️ GIS & Spatial Analysis</h4>
                <div class="skill-tags">
                    <span class="skill-tag">ArcGIS Pro</span>
                    <span class="skill-tag">GeoPandas</span>
                    <span class="skill-tag">Shapely</span>
                    <span class="skill-tag">Folium</span>
                    <span class="skill-tag">GPS Trajectory</span>
                    <span class="skill-tag">Spatial Statistics</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h4>📈 Visualization & BI</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Power BI</span>
                    <span class="skill-tag">Matplotlib</span>
                    <span class="skill-tag">Plotly</span>
                    <span class="skill-tag">Seaborn</span>
                    <span class="skill-tag">Dash</span>
                    <span class="skill-tag">Interactive Dashboards</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h4>🛠️ Development</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Flask</span>
                    <span class="skill-tag">Git</span>
                    <span class="skill-tag">CI/CD</span>
                    <span class="skill-tag">Docker</span>
                    <span class="skill-tag">REST APIs</span>
                    <span class="skill-tag">Linux</span>
                </div>
            </div>
            
            <div class="skill-category">
                <h4>🚗 Domain Knowledge</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Transport Modeling</span>
                    <span class="skill-tag">Mobility Systems</span>
                    <span class="skill-tag">Travel Behavior</span>
                    <span class="skill-tag">Mode Choice</span>
                    <span class="skill-tag">Urban Planning</span>
                </div>
            </div>
        </div>
        
        <!-- 其他信息 -->
        <h2 style="margin-top: 4rem;">📚 Languages & Interests</h2>
        <div class="cards-grid">
            <div class="card">
                <h3 class="card-title">Languages</h3>
                <ul>
                    <li>🇨🇳 Chinese (Native)</li>
                    <li>🇬🇧 English (Fluent)</li>
                    <li>🇳🇱 Dutch (Intermediate)</li>
                </ul>
            </div>
            
            <div class="card">
                <h3 class="card-title">Research Interests</h3>
                <ul>
                    <li>Shared mobility systems</li>
                    <li>Travel behavior modeling</li>
                    <li>AI applications in transport</li>
                    <li>Smart cities & mobility</li>
                </ul>
            </div>
            
            <div class="card">
                <h3 class="card-title">Certifications & Awards</h3>
                <ul>
                    <li>PhD Researcher, University of Twente</li>
                    <li>AI/ML Specialist, Accenture</li>
                    <li>GIS Professional</li>
                </ul>
            </div>
        </div>
    </div>
    
    <!-- 底部 -->
    <footer>
        <p>Made with ❤️ by Luqi Dong | © 2026 | 
            <a href="https://github.com/rockyistt/personal-website" target="_blank">View Source</a>
        </p>
    </footer>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML_TEMPLATE

@app.route("/health")
def health():
    return {"status": "ok", "message": "Server is running"}, 200

if __name__ == "__main__":
    app.run(debug=False)
"""
Personal Website - Luqi Dong
Modern, Multi-page Flask Application
"""

from flask import Flask, render_template_string
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

# ===== 页面模板和样式 =====
BASE_STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c3e50;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
    }
    
    .wrapper {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* 导航栏 */
    nav {
        background: rgba(255, 255, 255, 0.95);
        padding: 1rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
        backdrop-filter: blur(10px);
    }
    
    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: #667eea;
        text-decoration: none;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
        list-style: none;
    }
    
    .nav-links a {
        text-decoration: none;
        color: #2c3e50;
        font-weight: 500;
        transition: color 0.3s;
        position: relative;
    }
    
    .nav-links a:hover {
        color: #667eea;
    }
    
    .nav-links a.active {
        color: #667eea;
    }
    
    .nav-links a::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: #667eea;
        transition: width 0.3s;
    }
    
    .nav-links a.active::after {
        width: 100%;
    }
    
    /* 主容器 */
    .container {
        background: white;
        border-radius: 16px;
        padding: 4rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        animation: slideUp 0.6s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* 英雄部分 */
    .hero {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: center;
        margin-bottom: 4rem;
        padding-bottom: 3rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .hero-content h1 {
        font-size: 3.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-content .subtitle {
        font-size: 1.3rem;
        color: #7f8c8d;
        margin-bottom: 1.5rem;
    }
    
    .hero-badges {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    
    .badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .avatar {
        width: 100%;
        max-width: 350px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 3px;
        aspect-ratio: 1;
    }
    
    .avatar img {
        width: 100%;
        height: 100%;
        border-radius: 14px;
        background: #f0f0f0;
        object-fit: cover;
    }
    
    /* 社交链接 */
    .social-links {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .social-links a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 50px;
        height: 50px;
        background: #f0f0f0;
        border-radius: 50%;
        text-decoration: none;
        color: #667eea;
        transition: all 0.3s;
        font-size: 1.5rem;
    }
    
    .social-links a:hover {
        background: #667eea;
        color: white;
        transform: translateY(-3px);
    }
    
    /* 章节标题 */
    h2 {
        font-size: 2rem;
        color: #667eea;
        margin-bottom: 2rem;
        margin-top: 3rem;
        padding-bottom: 1rem;
        border-bottom: 3px solid #667eea;
    }
    
    h3 {
        font-size: 1.3rem;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    /* 卡片网格 */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .card {
        background: #f9fafb;
        border-left: 4px solid #667eea;
        padding: 2rem;
        border-radius: 12px;
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.1);
        background: white;
    }
    
    .card .company, .card .institution {
        color: #667eea;
        font-weight: 600;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .card .title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .card .date {
        color: #95a5a6;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .card p {
        color: #555;
        line-height: 1.6;
    }
    
    /* 技能标签 */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .skill-category {
        background: #f9fafb;
        padding: 2rem;
        border-radius: 12px;
        border-top: 3px solid #667eea;
    }
    
    .skill-category h4 {
        color: #667eea;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
    }
    
    .skill-tag {
        background: white;
        color: #667eea;
        padding: 0.6rem 1.2rem;
        border-radius: 20px;
        border: 2px solid #667eea;
        font-size: 0.9rem;
        transition: all 0.3s;
    }
    
    .skill-tag:hover {
        background: #667eea;
        color: white;
    }
    
    /* 底部 */
    footer {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 4rem;
        color: #7f8c8d;
    }
    
    footer a {
        color: #667eea;
        text-decoration: none;
    }
    
    footer a:hover {
        text-decoration: underline;
    }
    
    /* 响应式设计 */
    @media (max-width: 768px) {
        nav {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-links {
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .container {
            padding: 2rem;
        }
        
        .hero {
            grid-template-columns: 1fr;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
        
        .cards-grid, .skills-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
"""

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luqi Dong - Personal Website</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                max-width: 900px;
                background: white;
                padding: 60px;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                margin: 20px;
            }
            h1 {
                color: #667eea;
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #666;
                font-size: 1.3em;
                margin-bottom: 30px;
            }
            .section {
                margin: 30px 0;
                padding-bottom: 20px;
                border-bottom: 1px solid #eee;
            }
            .section h2 {
                color: #667eea;
                margin-bottom: 15px;
                font-size: 1.5em;
            }
            .section:last-child {
                border-bottom: none;
            }
            ul {
                list-style: none;
                padding-left: 0;
            }
            li {
                padding: 8px 0;
                padding-left: 20px;
                position: relative;
            }
            li:before {
                content: "▸";
                position: absolute;
                left: 0;
                color: #667eea;
            }
            .job {
                margin: 15px 0;
                padding: 15px;
                background: #f8f9fa;
                border-left: 4px solid #667eea;
                border-radius: 4px;
            }
            .job strong {
                color: #667eea;
                display: block;
                margin-bottom: 5px;
            }
            .job p {
                font-size: 0.95em;
                color: #666;
            }
            .links {
                margin-top: 30px;
                text-align: center;
            }
            .links a {
                display: inline-block;
                margin: 0 15px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                transition: background 0.3s;
            }
            .links a:hover {
                background: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>👋 Luqi Dong</h1>
            <p class="subtitle">AI Solutions Engineer & Data Scientist</p>
            
            <div class="section">
                <h2>📍 About Me</h2>
                <p>I'm a passionate data scientist and AI engineer specializing in:</p>
                <ul>
                    <li><strong>Large Language Models (LLMs)</strong> - Fine-tuning, LoRA, RAG</li>
                    <li><strong>GIS & Spatial Analysis</strong> - ArcGIS, GeoPandas, GPS trajectory analysis</li>
                    <li><strong>Machine Learning</strong> - Predictive modeling, behavioral analysis</li>
                    <li><strong>Transport Modelling</strong> - User behavior, mode choice analysis</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>💼 Current Experience</h2>
                <div class="job">
                    <strong>Accenture NL - Industry X</strong>
                    <p>Data & NLP Intern / AI/LLM Engineer (Nov 2025 - Mar 2026)</p>
                    <p>Developing enterprise-level AI solutions with focus on GIS test automation</p>
                </div>
                <div class="job">
                    <strong>University of Twente</strong>
                    <p>PhD Researcher - Transport Engineering (Oct 2021 - Present)</p>
                    <p>Researching shared mobility user behavior and mode choice modeling</p>
                </div>
            </div>
            
            <div class="section">
                <h2>🎓 Education</h2>
                <div class="job">
                    <strong>PhD in Transport Engineering</strong>
                    <p>University of Twente, Netherlands (2021 - Present)</p>
                </div>
                <div class="job">
                    <strong>Master's in Transport Planning</strong>
                    <p>Beijing Jiaotong University, China (2018 - 2021)</p>
                </div>
            </div>
            
            <div class="section">
                <h2>🔧 Key Skills</h2>
                <ul>
                    <li><strong>AI/ML:</strong> LLMs, RAG, Fine-tuning, PyTorch, Hugging Face</li>
                    <li><strong>Data Science:</strong> Python, R, SQL, Machine Learning, Statistical Modeling</li>
                    <li><strong>GIS:</strong> ArcGIS, GeoPandas, Spatial Analysis, GPS Trajectory</li>
                    <li><strong>Visualization:</strong> Power BI, Matplotlib, Interactive Dashboards</li>
                </ul>
            </div>
            
            <div class="links">
                <a href="https://github.com/rockyistt" target="_blank">🐙 GitHub</a>
                <a href="https://linkedin.com" target="_blank">💼 LinkedIn</a>
                <a href="mailto:luqi.dong@example.com">✉️ Email</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok", "message": "Server is running"}

if __name__ == "__main__":
    app.run(debug=False)#   F o r c e   r e b u i l d   a t   2 0 2 6 - 0 4 - 2 3   1 6 : 0 5 : 3 9  
 