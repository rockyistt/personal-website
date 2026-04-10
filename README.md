# 个人网站项目 - Flask

一个使用 Flask、SQLAlchemy 和现代 CSS 构建的专业个人网站，展示简历、作品集和技能。

## 项目特点

- 📱 响应式设计，支持所有设备
- 🎨 现代化、专业的用户界面
- 📊 数据库支持（SQLAlchemy）
- 🚀 快速加载和高性能
- 🔍 SEO 友好
- 📝 完整的简历和作品集展示
- 🏆 技能展示和专业评分

## 项目结构

```
personal-website/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # 主样式文件
│   │   ├── js/
│   │   │   └── main.js        # 主 JavaScript
│   │   └── images/            # 图片文件夹
│   ├── templates/
│   │   ├── base.html          # 基础模板
│   │   ├── index.html         # 首页
│   │   ├── about.html         # 关于页面
│   │   ├── portfolio.html     # 作品集页面
│   │   ├── project_detail.html # 项目详情页
│   │   └── resume.html        # 简历页面
│   ├── __init__.py            # Flask 应用初始化
│   ├── models.py              # 数据库模型
│   └── routes.py              # 路由定义
├── instance/                  # 实例文件夹（数据库等）
├── run.py                     # 启动脚本
├── requirements.txt           # 项目依赖
├── config.py                  # 配置文件（可选）
├── .env                       # 环境变量（可选）
└── README.md                  # 项目说明

```

## 安装和运行

### 1. 创建虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 创建数据库并添加示例数据

```bash
# 初始化数据库
flask --app run init-db

# 添加示例数据
flask --app run seed-db
```

### 4. 运行应用

```bash
python run.py
```

访问 http://127.0.0.1:5000 查看网站。

## 配置说明

### 数据库配置

数据库文件默认位于 `instance/app.db`，可在 `app/__init__.py` 中修改：

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
```

### 环境变量

创建 `.env` 文件来配置敏感信息：

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
```

## 页面功能

### 首页 (`/`)
- 英雄部分 (Hero section)
- 精选项目展示
- 快速统计
- 行动号召 (CTA)

### 关于页面 (`/about`)
- 个人简介
- 工作经验时间线
- 技能展示（带评分）
- 教育背景

### 简历页面 (`/resume`)
- 个人信息
- 专业摘要
- 完整工作经历
- 技能列表
- 教育背景
- 证书和认证

### 作品集 (`/portfolio`)
- 项目网格展示
- 技术标签
- 项目详情链接
- GitHub 和项目链接

### 项目详情 (`/portfolio/<project_id>`)
- 项目完整描述
- 技术栈展示
- 外部链接（项目 URL、GitHub）

## API 端点

### 获取所有项目
```
GET /api/projects
```

响应示例：
```json
[
    {
        "id": 1,
        "title": "项目标题",
        "description": "项目描述",
        "technologies": ["Python", "Flask"],
        "image_url": "/static/images/project.jpg",
        "project_url": "https://example.com",
        "github_url": "https://github.com/user/project",
        "featured": true
    }
]
```

### 获取所有技能
```
GET /api/skills
```

响应示例：
```json
[
    {
        "id": 1,
        "category": "编程语言",
        "name": "Python",
        "proficiency": 5
    }
]
```

## 数据库模型

### Project（项目）
- id: 主键
- title: 项目标题
- description: 项目描述
- technologies: 技术栈（逗号分隔）
- image_url: 项目图片 URL
- project_url: 项目链接
- github_url: GitHub 链接
- date_created: 创建时间
- featured: 是否为精选项目

### Experience（工作经验）
- id: 主键
- company: 公司名称
- position: 职位
- start_date: 开始日期
- end_date: 结束日期
- description: 工作描述
- current: 是否为当前工作

### Skill（技能）
- id: 主键
- category: 技能类别
- name: 技能名称
- proficiency: 熟练度（1-5）

## 自定义指南

### 修改颜色方案

编辑 `app/static/css/style.css` 中的 CSS 变量：

```css
:root {
    --primary-color: #2563eb;      /* 主色 */
    --secondary-color: #64748b;    /* 次色 */
    --accent-color: #f59e0b;       /* 强调色 */
    /* ... 其他颜色 ... */
}
```

### 添加页面

1. 在 `app/templates/` 中创建新 HTML 模板
2. 在 `app/routes.py` 中创建新路由
3. 根据需要在导航栏中添加链接

### 添加项目或经验

使用 Flask shell 或编写脚本添加数据：

```python
from app import create_app, db
from app.models import Project, Experience, Skill

app = create_app()
with app.app_context():
    project = Project(
        title='新项目',
        description='项目描述',
        technologies='Python, Flask',
        featured=True
    )
    db.session.add(project)
    db.session.commit()
```

## 部署建议

### Vercel
1. 将代码推送到 GitHub
2. 连接 GitHub 仓库到 Vercel
3. 配置环境变量
4. 部署

### Heroku
1. 创建 Procfile：
   ```
   web: gunicorn run:app
   ```
2. 创建 runtime.txt：
   ```
   python-3.11.0
   ```
3. 部署到 Heroku

### 自有服务器
1. 安装 Python 和 pip
2. 克隆项目，创建虚拟环境
3. 使用 Gunicorn 等 WSGI 服务器运行
4. 使用 Nginx 作为反向代理
5. 配置 SSL 证书

## 技术栈

- **后端**: Flask（Python）
- **数据库**: SQLite（出产环境建议使用 PostgreSQL）
- **前端**: HTML5、CSS3、JavaScript
- **模板引擎**: Jinja2
- **ORM**: SQLAlchemy

## 浏览器兼容性

- Chrome（最新）
- Firefox（最新）
- Safari（最新）
- Edge（最新）
- 移动浏览器（iOS Safari、Chrome Mobile）

## 许可证

MIT License

## 作者

你的名字 - 联系方式

## 下一步

- [ ] 添加实际内容和真实项目
- [ ] 上传个人照片和项目图片
- [ ] 配置联系表单（后端处理）
- [ ] 添加 GA 或其他分析工具
- [ ] 优化 SEO（添加 meta 标签等）
- [ ] 配置域名和 HTTPS
- [ ] 设置邮件通知（项目查询等）
- [ ] 添加博客功能（可选）
- [ ] 实现深色主题（可选）

---

如有问题或建议，欢迎提交 Issue 或 Pull Request！
