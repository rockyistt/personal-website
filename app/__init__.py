from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import tempfile

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 配置 - 检测是否在 Vercel 环境
    if os.environ.get('VERCEL'):
        # Vercel 环境：使用 /tmp 目录
        db_path = os.path.join(tempfile.gettempdir(), 'app.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    else:
        # 本地开发环境
        basedir = os.path.abspath(os.path.dirname(__file__))
        db_path = os.path.join(basedir, '../instance/app.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # 初始化数据库
    db.init_app(app)
    
    # 创建数据库表并初始化数据
    with app.app_context():
        db.create_all()
        init_db()
    
    # 注册路由
    from app.routes import main_bp, portfolio_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(portfolio_bp)
    
    return app

def init_db():
    """初始化数据库种子数据"""
    from app.models import Project, Experience, Skill
    
    # 如果项目表已有数据，则跳过
    if Project.query.first() is not None:
        return
    
    try:
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
