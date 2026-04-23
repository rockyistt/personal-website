"""
Personal Website - Luqi Dong
Vercel Serverless Function Entry Point
"""

from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-for-vercel"

# Projects data
PROJECTS = [
    {"id": 1, "title": "Shared Mobility User Behavior Analysis", "category": "Data Science & GIS", "location": "University of Twente", "date": "2021 - Present", "excerpt": "Analyzed 100,000+ GPS trajectories from shared e-scooter and bike systems", "icon": "📍", "description": "<h3>Project Overview</h3><p>Understanding shared mobility user behavior through large-scale GPS trajectory data analysis.</p><h4>Key Achievements:</h4><ul><li>Processed 100,000+ GPS trajectories</li><li>Developed data cleaning pipelines</li><li>Implemented clustering algorithms</li><li>Created interactive visualizations</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>Python</span><span>GeoPandas</span><span>Folium</span><span>DBSCAN</span><span>PostGIS</span></div>"},
    {"id": 2, "title": "Travel Mode Choice Prediction", "category": "Machine Learning", "location": "Research Project", "date": "2022 - 2023", "excerpt": "ML models for predicting transportation mode preferences with 85% accuracy", "icon": "🚗", "description": "<h3>Project Overview</h3><p>Built advanced ML models to predict transportation mode choice.</p><h4>Key Achievements:</h4><ul><li>Developed Random Forest and Neural Network models</li><li>Achieved 85% prediction accuracy</li><li>Feature engineering from raw trip data</li><li>Hyperparameter optimization</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>Python</span><span>Scikit-learn</span><span>XGBoost</span><span>TensorFlow</span><span>SHAP</span></div>"},
    {"id": 3, "title": "GPS Trajectory Data Pipeline", "category": "Data Engineering", "location": "Technical Infrastructure", "date": "2023 - Present", "excerpt": "ETL pipeline for processing GPS trajectory data at scale", "icon": "🔄", "description": "<h3>Project Overview</h3><p>Developed robust ETL pipeline for processing GPS trajectory data.</p><h4>Key Achievements:</h4><ul><li>Handles data from 50+ cities</li><li>Processes 10+ million GPS points daily</li><li>Automatic data quality checks</li><li>Interactive visualizations</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>Apache Airflow</span><span>Python</span><span>PostgreSQL</span><span>PostGIS</span><span>Docker</span></div>"},
    {"id": 4, "title": "ArcGIS Test Automation Framework", "category": "QA & Automation", "location": "Accenture", "date": "2025 - Present", "excerpt": "Comprehensive test automation framework for GIS applications with 90% coverage", "icon": "🧪", "description": "<h3>Project Overview</h3><p>Designed test automation framework for enterprise GIS applications.</p><h4>Key Achievements:</h4><ul><li>Achieved 90% test coverage</li><li>Reduced manual testing by 70%</li><li>Integrated with CI/CD pipeline</li><li>Implemented visual regression testing</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>Python</span><span>Selenium</span><span>ArcGIS API</span><span>pytest</span><span>Jenkins</span></div>"},
    {"id": 5, "title": "LLM Fine-tuning for Transport Domain", "category": "AI & NLP", "location": "Research", "date": "2025 - Present", "excerpt": "Fine-tuning large language models for transport-specific NLP tasks", "icon": "🤖", "description": "<h3>Project Overview</h3><p>Adapting LLMs to understand transport domain-specific text.</p><h4>Current Work:</h4><ul><li>Fine-tuning Llama 2 and Mistral models</li><li>Using LoRA and QLoRA for efficient training</li><li>Building RAG system for transport Q&A</li><li>Domain-specific vocabulary and embeddings</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>PyTorch</span><span>Hugging Face</span><span>LoRA</span><span>LangChain</span><span>FAISS</span></div>"},
    {"id": 6, "title": "Interactive Dashboard Platform", "category": "Data Visualization", "location": "Multiple Projects", "date": "2022 - Present", "excerpt": "Real-time dashboards for stakeholder reporting and KPI tracking", "icon": "📊", "description": "<h3>Project Overview</h3><p>Developed interactive dashboards for data visualization across multiple projects.</p><h4>Key Achievements:</h4><ul><li>Built 10+ interactive dashboards</li><li>Real-time data refresh every 5 minutes</li><li>Custom KPI calculations</li><li>Mobile-responsive design</li></ul><h4>Technologies:</h4><div class='tech-tags'><span>Power BI</span><span>Plotly</span><span>Dash</span><span>Python</span><span>PostgreSQL</span></div>"},
]

STYLES = """
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #2c3e50; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
.wrapper { max-width: 1200px; margin: 0 auto; }
nav { background: rgba(255, 255, 255, 0.95); padding: 1rem 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 1.5rem; font-weight: 700; color: #667eea; text-decoration: none; }
.nav-links { display: flex; gap: 2rem; list-style: none; }
.nav-links a { text-decoration: none; color: #2c3e50; font-weight: 500; transition: color 0.3s; }
.nav-links a:hover, .nav-links a.active { color: #667eea; }
.banner { background: linear-gradient(135deg, #f39c12, #e67e22); color: white; padding: 15px; border-radius: 12px; margin-bottom: 15px; font-weight: bold; text-align: center; font-size: 1.1rem; }
.container { background: white; border-radius: 16px; padding: 4rem; box-shadow: 0 20px 60px rgba(0,0,0,0.15); animation: slideUp 0.6s ease-out; }
@keyframes slideUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
h1 { font-size: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
h2 { font-size: 2rem; color: #667eea; margin-top: 2rem; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 3px solid #667eea; }
h3 { font-size: 1.3rem; color: #2c3e50; }
p { line-height: 1.8; color: #555; }
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; margin-bottom: 2rem; }
.project-card { background: #f9fafb; border: 1px solid #e8e8e8; border-radius: 12px; overflow: hidden; transition: all 0.3s; text-decoration: none; display: flex; flex-direction: column; }
.project-card:hover { transform: translateY(-8px); box-shadow: 0 15px 35px rgba(102, 126, 234, 0.15); border-color: #667eea; }
.project-icon { width: 100%; height: 150px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; font-size: 60px; color: white; }
.project-content { padding: 2rem; flex-grow: 1; }
.project-category { display: inline-block; background: #667eea; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; margin-bottom: 1rem; }
.project-title { font-size: 1.2rem; font-weight: 600; color: #2c3e50; margin-bottom: 0.5rem; }
.project-meta { display: flex; justify-content: space-between; font-size: 0.9rem; color: #95a5a6; margin-bottom: 1rem; }
.project-desc { color: #555; font-size: 0.95rem; line-height: 1.6; }
.project-link { display: inline-block; color: #667eea; font-weight: 600; text-decoration: none; margin-top: 1rem; }
.project-link:hover { color: #764ba2; }
.back-btn { display: inline-block; margin-bottom: 2rem; padding: 0.8rem 1.5rem; background: #f0f0f0; color: #667eea; text-decoration: none; border-radius: 8px; font-weight: 500; }
.back-btn:hover { background: #667eea; color: white; }
footer { background: rgba(255, 255, 255, 0.9); padding: 2rem; border-radius: 12px; text-align: center; margin-top: 4rem; color: #7f8c8d; }
footer a { color: #667eea; text-decoration: none; }
.tech-tags { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0; }
.tech-tags span { background: white; color: #667eea; padding: 0.5rem 1rem; border-radius: 20px; border: 2px solid #667eea; font-size: 0.9rem; }
@media (max-width: 768px) { nav { flex-direction: column; gap: 1rem; } .nav-links { flex-direction: column; } .container { padding: 2rem; } h1 { font-size: 2rem; } .projects-grid { grid-template-columns: 1fr; } }
</style>
"""

@app.route("/")
def home():
    projects_html = ""
    for project in PROJECTS:
        projects_html += f"""
        <a href="/project/{project['id']}" style="text-decoration: none;">
            <div class="project-card">
                <div class="project-icon">{project['icon']}</div>
                <div class="project-content">
                    <div class="project-category">{project['category']}</div>
                    <h3 class="project-title">{project['title']}</h3>
                    <div class="project-meta">
                        <span>📍 {project['location']}</span>
                        <span>📅 {project['date']}</span>
                    </div>
                    <p class="project-desc">{project['excerpt']}</p>
                    <span class="project-link">View Details →</span>
                </div>
            </div>
        </a>
        """
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luqi Dong - Personal Website</title>
        {STYLES}
    </head>
    <body>
    <div class="wrapper">
        <div class="banner">✨ LIVE - Interactive Projects Portfolio! 🚀</div>
        
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
            <p style="font-size: 1.3rem; color: #7f8c8d; margin-bottom: 2rem;">🤖 AI Solutions Engineer | 📊 Data Scientist | 🗺️ GIS Specialist</p>
            
            <p style="color: #555; line-height: 1.8; font-size: 1.05rem; margin-bottom: 3rem;">
                PhD Researcher at University of Twente specializing in transport modelling and shared mobility behavior. 
                Passionate about applying AI/LLM and advanced data science techniques to solve real-world problems.
            </p>
            
            <h2 id="projects">🚀 Featured Projects</h2>
            <p style="margin-bottom: 2rem; color: #666;">Click on any project to view detailed information</p>
            
            <div class="projects-grid">
                {projects_html}
            </div>
            
            <h2 id="skills">🔧 Skills & Expertise</h2>
            <div class="projects-grid">
                <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                    <h3>🤖 AI & Machine Learning</h3>
                    <div class="tech-tags">
                        <span>LLMs</span>
                        <span>Fine-tuning</span>
                        <span>RAG</span>
                        <span>PyTorch</span>
                        <span>Hugging Face</span>
                    </div>
                </div>
                <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                    <h3>📊 Data Science</h3>
                    <div class="tech-tags">
                        <span>Python</span>
                        <span>SQL</span>
                        <span>Scikit-learn</span>
                        <span>Statistics</span>
                        <span>R</span>
                    </div>
                </div>
                <div style="background: #f9fafb; padding: 2rem; border-radius: 12px;">
                    <h3>🗺️ GIS & Spatial</h3>
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
            <p>Made with ❤️ by Luqi Dong | © 2026 | <a href="https://github.com/rockyistt" target="_blank">GitHub</a></p>
        </footer>
    </div>
    </body>
    </html>
    """

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    
    if not project:
        return "<h1>Project not found</h1>", 404
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project['title']} - Luqi Dong</title>
        {STYLES}
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
            
            <h1>{project['title']}</h1>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 100px;">
                    {project['icon']}
                </div>
                <div>
                    <div style="margin-bottom: 2rem;">
                        <div style="color: #667eea; font-weight: 600; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 0.5rem;">Category</div>
                        <div style="color: #667eea; font-weight: 600; font-size: 1.1rem;">{project['category']}</div>
                    </div>
                    <div style="margin-bottom: 2rem;">
                        <div style="color: #667eea; font-weight: 600; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 0.5rem;">Location</div>
                        <div style="color: #667eea; font-weight: 600; font-size: 1.1rem;">{project['location']}</div>
                    </div>
                    <div>
                        <div style="color: #667eea; font-weight: 600; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 0.5rem;">Duration</div>
                        <div style="color: #667eea; font-weight: 600; font-size: 1.1rem;">{project['date']}</div>
                    </div>
                </div>
            </div>
            
            {project['description']}
        </div>
        
        <footer>
            <p>Made with ❤️ by Luqi Dong | © 2026</p>
        </footer>
    </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200
