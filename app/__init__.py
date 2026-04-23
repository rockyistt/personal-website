from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
    
    # 简单配置
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-key'
    
    db.init_app(app)
    
    # 注册一个简单的测试路由
    @app.route('/')
    def home():
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Luqi Dong - Personal Website</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }
                h1 { color: #333; }
                .intro { background: #f5f5f5; padding: 20px; border-radius: 8px; }
                .section { margin: 30px 0; }
            </style>
        </head>
        <body>
            <h1>👋 Luqi Dong</h1>
            <p>AI Solutions Engineer & Data Scientist</p>
            
            <div class="intro">
                <h2>About Me</h2>
                <p>Welcome to my personal website! I'm a data scientist and AI engineer with expertise in:</p>
                <ul>
                    <li>Large Language Models (LLMs) and RAG</li>
                    <li>GIS and Spatial Analysis</li>
                    <li>Machine Learning and Data Science</li>
                    <li>Transport Modelling and Behavioral Analysis</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>Experience</h2>
                <p><strong>Accenture NL</strong> - Data & NLP Engineer (2025-2026)</p>
                <p><strong>University of Twente</strong> - PhD Researcher (2021-Present)</p>
                <p><strong>Beijing Jiaotong University</strong> - Master's (2018-2021)</p>
            </div>
            
            <div class="section">
                <p><a href="https://github.com/rockyistt">GitHub</a> | 
                   <a href="https://linkedin.com">LinkedIn</a></p>
            </div>
        </body>
        </html>
        '''
    
    return app

        projects = [
            Project(
                title='AI/LLM 在 GIS 测试自动化中的应用',
                description='在 Accenture NL 开发企业级 AI 和 NLP 解决方案。设计两阶段模块化框架，使用 CodeLlama-7B 与 LoRA 技术实现从需求到原子步骤的映射。',
                technologies='Python, PyTorch, Hugging Face, CodeLlama, LoRA, PEFT, RAG, LangChain, ArcGIS',
                featured=True
            ),
            Project(
                title='共享微出行用户行为建模研究',
                description='PhD 研究项目：对共享微出行服务用户行为进行综合研究。设计可扩展数据收集框架，应用隐性类模型发现用户细分，构建预测模型。',
                technologies='Python, R, SQL, ArcGIS, Power BI, GeoPandas, Scikit-learn, Statistical Modeling',
                featured=True
            ),
            Project(
                title='基于 GPS 轨迹的城市可达性时空模型',
                description='Master 论文项目：分析 136GB GPS 轨迹数据建立城市可达性模型。提取出行时间，应用聚类算法，构建空间可达性模型。',
                technologies='Python, Pandas, GeoPandas, ArcGIS, SQL, Gaode Map API, Clustering algorithms',
                featured=True
            ),
            Project(
                title='城市交通可达性分析',
                description='医疗设施可达性分析案例研究。在公共卫生紧急情况下分析交通网络城市可达性的时空特征。',
                technologies='Python, ArcGIS, Network Analysis, Spatial Statistics',
                featured=False
            ),
            Project(
                title='个人网站项目',
                description='使用现代 Flask 框架构建的专业个人网站。展示简历、作品集、技能和研究成果。包含响应式设计、数据库集成和 API 端点。',
                technologies='Flask, SQLAlchemy, Python, HTML5, CSS3, JavaScript, Jinja2',
                featured=True,
                github_url='https://github.com/rockyistt/personal-website'
            )
        ]
        
        experiences = [
            Experience(
                company='Accenture NL - Industry X',
                position='Data & NLP Intern / AI/LLM Engineer',
                start_date='2025-11',
                end_date='2026-03',
                description='开发企业级 AI 和 NLP 解决方案，专注于 GIS 测试自动化。实现使用 CodeLlama-7B 从 GIS 脚本反向工程的管道。',
                current=True
            ),
            Experience(
                company='University of Twente - Department of Civil Engineering',
                position='PhD Researcher - Transport Engineering',
                start_date='2021-10',
                end_date=None,
                description='进行共享微出行用户行为建模的 PhD 研究。应用先进统计建模和机器学习技术。与 30+ 行业利益相关者互动。',
                current=True
            ),
            Experience(
                company='Beijing Jiaotong University',
                position='Master Student - Transport Planning',
                start_date='2018-09',
                end_date='2021-06',
                description='完成 Master 论文：基于 GPS 轨迹的城市可达性时空模型分析。处理 136GB GPS 轨迹数据。',
                current=False
            )
        ]
        
        skills_data = [
            ('AI & Generative AI', 'Large Language Models (Fine-tuning, LoRA, PEFT)', 5),
            ('AI & Generative AI', 'Retrieval-Augmented Generation (RAG)', 5),
            ('AI & Generative AI', 'Hugging Face Transformers', 5),
            ('AI & Generative AI', 'Natural Language Processing', 4),
            ('AI & Generative AI', 'PyTorch', 4),
            ('Data Science', 'Predictive Modeling', 5),
            ('Data Science', 'Machine Learning', 5),
            ('Data Science', 'Behavioral Modeling', 5),
            ('Data Science', 'Causal Inference', 4),
            ('Data Science', 'Feature Engineering', 5),
            ('GIS & Spatial Analysis', 'ArcGIS', 5),
            ('GIS & Spatial Analysis', 'GeoPandas', 5),
            ('GIS & Spatial Analysis', 'GPS Trajectory Analysis', 5),
            ('GIS & Spatial Analysis', 'Spatial Modeling', 5),
            ('GIS & Spatial Analysis', 'ArcPy', 4),
            ('Programming & Databases', 'Python', 5),
            ('Programming & Databases', 'R', 4),
            ('Programming & Databases', 'SQL', 5),
            ('Programming & Databases', 'Git', 4),
            ('Programming & Databases', 'API Integration', 4),
            ('Data Visualization', 'Power BI', 4),
            ('Data Visualization', 'Matplotlib/Seaborn', 5),
            ('Data Visualization', 'Spatial Visualization', 5),
            ('Data Visualization', 'Interactive Dashboards', 4),
            ('Statistical Methods', 'Latent Class Models', 4),
            ('Statistical Methods', 'Regression Analysis', 5),
            ('Statistical Methods', 'A/B Testing', 4),
            ('Statistical Methods', 'ANOVA', 4),
        ]
        
        skills = [Skill(category=cat, name=name, proficiency=prof) for cat, name, prof in skills_data]
        
        db.session.add_all(projects + experiences + skills)
        db.session.commit()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"⚠️ Error initializing database: {e}")
        db.session.rollback()
