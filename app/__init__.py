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
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    # 注册路由
    from app.routes import main_bp, portfolio_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(portfolio_bp)
    
    return app
