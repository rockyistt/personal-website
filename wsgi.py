import os
import sys
import traceback
from app import create_app, db
from app.models import Project, Experience, Skill

try:
    # 创建 Flask 应用
    app = create_app()

    # 初始化生产环境数据库
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Database creation error: {e}")
            traceback.print_exc()
        
        # 如果数据库为空，添加示例数据
        try:
            if Project.query.first() is None:
        # ===== 添加真实项目 =====
        project1 = Project(
            title='AI/LLM 在 GIS 测试自动化中的应用',
            description='在 Accenture NL 开发企业级 AI 和 NLP 解决方案。设计了一个两阶段模块化框架，使用微调的 CodeLlama-7B（基于 LoRA 的参数高效微调），实现了从文件级需求到原子步骤的映射。构建了专有的意图提取算法，处理 44,000+ 数据点，实现了加权分词算法来提高 LLM 在 GIS 上下文中的表现。建立了企业级 RAG（检索增强生成）架构，将 LLM 与工业 GIS 标准和空间逻辑相结合。',
            technologies='Python, PyTorch, Hugging Face, CodeLlama, LoRA, PEFT, RAG, LangChain, ArcGIS',
            featured=True
        )
        
        project2 = Project(
            title='共享微出行用户行为建模研究',
            description='PhD 研究项目：对共享微出行服务用户行为进行comprehensive study。设计并实现了包含5个关键数据质量标准的可扩展数据收集框架。从空间和时间数据中提取特征，应用隐性类模型来发现隐藏的用户细分。构建预测模型（binary logit）来解释和预测共享微出行使用。开发交互式 Power BI 仪表板与 30+ 行业利益相关者沟通洞察。',
            technologies='Python, R, SQL, ArcGIS, Power BI, GeoPandas, Scikit-learn, Statistical Modeling',
            featured=True
        )
        
        project3 = Project(
            title='基于 GPS 轨迹的城市可达性时空模型',
            description='Master 论文项目：分析了 136GB GPS 轨迹数据来建立城市可达性模型。从 GPS 轨迹数据中提取出行时间并评估最优拟合分布。应用聚类算法（K-means, DBSCAN）对移动模式进行分类。构建和维护空间数据集（POI、六边形网格）以识别时空变异。开发了纳入 POI 熵和可靠性约束的空间可达性模型。',
            technologies='Python, Pandas, GeoPandas, ArcGIS, SQL, Gaode Map API, Clustering algorithms',
            featured=True
        )
        
        project4 = Project(
            title='城市交通可达性分析 - 考虑旅行时间可靠性',
            description='以医疗保健设施教育可达性为案例研究。在公共卫生紧急情况下分析交通网络中城市可达性的时空特征。采样 1,000 个原点点和 500 个医疗设施目的地。',
            technologies='Python, ArcGIS, Network Analysis, Spatial Statistics',
            featured=False
        )
        
        project5 = Project(
            title='个人网站项目',
            description='使用现代 Flask 框架构建的专业个人网站。展示简历、作品集、技能和研究成果。包含响应式设计、数据库集成和 API 端点。',
            technologies='Flask, SQLAlchemy, Python, HTML5, CSS3, JavaScript, Jinja2',
            featured=True,
            github_url='https://github.com/yourusername/personal-website'
        )
        
        # ===== 添加工作经验 =====
        exp1 = Experience(
            company='Accenture NL - Industry X',
            position='Data & NLP Intern / AI/LLM Engineer',
            start_date='2025-11',
            end_date='2026-03',
            description='开发企业级 AI 和 NLP 解决方案，专注于 GIS 测试自动化。实现了使用 CodeLlama-7B（LoRA 技术）从传统 GIS 测试脚本反向工程的管道。构建了规模化 NLP 管道自动化知识密集型工作流，将 GIS 测试自动化时间减少了 30%+。与跨职能技术和咨询团队合作，将业务需求转化为 AI 系统设计。',
            current=True
        )
        
        exp2 = Experience(
            company='University of Twente - Department of Civil Engineering',
            position='PhD Researcher - Transport Engineering',
            start_date='2021-10',
            end_date=None,
            description='进行关于共享微出行用户行为建模的 PhD 研究。设计多阶段研究项目，进行大规模行为数据分析。应用先进的统计建模、机器学习和因果推理技术。与 30+ 行业利益相关者（包括 Siemens、Hacon、PBL）进行互动，推动数据驱动决策。发表同行评审期刊论文和会议论文。',
            current=True
        )
        
        exp3 = Experience(
            company='Beijing Jiaotong University',
            position='Master Student - Transport Planning',
            start_date='2018-09',
            end_date='2021-06',
            description='完成 Master 论文："基于 GPS 轨迹的城市可达性时空模型分析"。处理和分析 136GB GPS 轨迹数据。应用 Python、R、SQL 和 ArcGIS 进行地理空间分析。开发空间建模模型支持需求预测和服务覆盖优化。',
            current=False
        )
        
        # ===== 添加技能 =====
        ai_skills = [
            Skill(category='AI & Generative AI', name='Large Language Models (Fine-tuning, LoRA, PEFT)', proficiency=5),
            Skill(category='AI & Generative AI', name='Retrieval-Augmented Generation (RAG)', proficiency=5),
            Skill(category='AI & Generative AI', name='Hugging Face Transformers', proficiency=5),
            Skill(category='AI & Generative AI', name='Natural Language Processing', proficiency=4),
            Skill(category='AI & Generative AI', name='PyTorch', proficiency=4),
        ]
        
        ds_skills = [
            Skill(category='Data Science', name='Predictive Modeling', proficiency=5),
            Skill(category='Data Science', name='Machine Learning', proficiency=5),
            Skill(category='Data Science', name='Behavioral Modeling', proficiency=5),
            Skill(category='Data Science', name='Causal Inference', proficiency=4),
            Skill(category='Data Science', name='Feature Engineering', proficiency=5),
        ]
        
        gis_skills = [
            Skill(category='GIS & Spatial Analysis', name='ArcGIS', proficiency=5),
            Skill(category='GIS & Spatial Analysis', name='GeoPandas', proficiency=5),
            Skill(category='GIS & Spatial Analysis', name='GPS Trajectory Analysis', proficiency=5),
            Skill(category='GIS & Spatial Analysis', name='Spatial Modeling', proficiency=5),
            Skill(category='GIS & Spatial Analysis', name='ArcPy', proficiency=4),
        ]
        
        prog_skills = [
            Skill(category='Programming & Databases', name='Python', proficiency=5),
            Skill(category='Programming & Databases', name='R', proficiency=4),
            Skill(category='Programming & Databases', name='SQL', proficiency=5),
            Skill(category='Programming & Databases', name='Git', proficiency=4),
            Skill(category='Programming & Databases', name='API Integration', proficiency=4),
        ]
        
        viz_skills = [
            Skill(category='Data Visualization', name='Power BI', proficiency=4),
            Skill(category='Data Visualization', name='Matplotlib/Seaborn', proficiency=5),
            Skill(category='Data Visualization', name='Spatial Visualization', proficiency=5),
            Skill(category='Data Visualization', name='Interactive Dashboards', proficiency=4),
        ]
        
        stat_skills = [
            Skill(category='Statistical Methods', name='Latent Class Models', proficiency=4),
            Skill(category='Statistical Methods', name='Regression Analysis', proficiency=5),
            Skill(category='Statistical Methods', name='A/B Testing', proficiency=4),
            Skill(category='Statistical Methods', name='ANOVA', proficiency=4),
        ]
        
        db.session.add_all([
            project1, project2, project3, project4, project5,
            exp1, exp2, exp3
        ] + ai_skills + ds_skills + gis_skills + prog_skills + viz_skills + stat_skills)
        
        db.session.commit()
        except Exception as e:
            print(f"Data seeding error: {e}")
            traceback.print_exc()
            db.session.rollback()

except Exception as e:
    print(f"Application initialization error: {e}")
    traceback.print_exc()
    # 创建一个最小的应用以避免完全崩溃
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def error_page():
        return f"<h1>Application Error</h1><p>{str(e)}</p><pre>{traceback.format_exc()}</pre>", 500

if __name__ == '__main__':
    app.run(debug=False)
