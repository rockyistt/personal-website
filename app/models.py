from app import db
from datetime import datetime

class Project(db.Model):
    """作品/项目模型"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500))  # 逗号分隔
    image_url = db.Column(db.String(500))
    project_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    featured = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Project {self.title}>'
    
    def get_technologies(self):
        """返回技术列表"""
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Experience(db.Model):
    """工作经验模型"""
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50))
    description = db.Column(db.Text)
    current = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Experience {self.position} at {self.company}>'


class Skill(db.Model):
    """技能模型"""
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)  # 如: Python, Data Analysis, etc.
    name = db.Column(db.String(200), nullable=False)
    proficiency = db.Column(db.Integer)  # 1-5 级
    
    def __repr__(self):
        return f'<Skill {self.name}>'
