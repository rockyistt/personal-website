from flask import Blueprint, render_template, jsonify
from app.models import Project, Experience, Skill
from app import db

# 创建蓝图
main_bp = Blueprint('main', __name__)
portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@main_bp.route('/')
def index():
    """主页"""
    featured_projects = Project.query.filter_by(featured=True).all()
    return render_template('index.html', projects=featured_projects)


@main_bp.route('/about')
def about():
    """关于页面"""
    experiences = Experience.query.all()
    skills = Skill.query.all()
    return render_template('about.html', experiences=experiences, skills=skills)


@main_bp.route('/resume')
def resume():
    """简历页面"""
    experiences = Experience.query.all()
    skills = Skill.query.all()
    return render_template('resume.html', experiences=experiences, skills=skills)


@portfolio_bp.route('/')
def portfolio():
    """作品集页面"""
    projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('portfolio.html', projects=projects)


@portfolio_bp.route('/<int:project_id>')
def project_detail(project_id):
    """项目详情页"""
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)


@main_bp.route('/api/projects')
def api_projects():
    """API 端点：获取所有项目"""
    projects = Project.query.all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'technologies': p.get_technologies(),
        'image_url': p.image_url,
        'project_url': p.project_url,
        'github_url': p.github_url,
        'featured': p.featured
    } for p in projects])


@main_bp.route('/api/skills')
def api_skills():
    """API 端点：获取所有技能"""
    skills = Skill.query.all()
    return jsonify([{
        'id': s.id,
        'category': s.category,
        'name': s.name,
        'proficiency': s.proficiency
    } for s in skills])
