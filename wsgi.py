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
    app.run(debug=False)