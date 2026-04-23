"""
Minimal Flask application for Vercel deployment
No external dependencies - everything self-contained
"""

from flask import Flask

# 创建应用 - 不依赖任何导入
app = Flask(__name__)

# 简单配置
app.config["SECRET_KEY"] = "dev"

# 定义所有路由
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