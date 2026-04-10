# 🚀 快速开始指南

## 步骤 1: 创建虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## 步骤 2: 安装依赖

```bash
pip install -r requirements.txt
```

## 步骤 3: 初始化数据库和添加示例数据

```bash
# 初始化数据库
flask --app run init-db

# 添加真实数据（从 Luqi Dong 的简历）
flask --app run seed-db
```

## 步骤 4: 运行应用

```bash
python run.py
```

访问 **http://127.0.0.1:5000** 查看你的网站！

---

## 📖 项目内容

### 🏠 首页 (/)
- 英雄部分展示专业形象
- 精选项目展示（AI/LLM、GIS、数据科学项目）
- 快速统计（经验、项目、论文、专利）
- 行动号召按钮

### 👤 关于页面 (/about)
- 个人简介
- 工作经验时间线（Accenture NL、University of Twente、Beijing Jiaotong）
- 30+ 项技能展示（AI/LLM、数据科学、GIS、编程语言等）
- 教育背景

### 📄 简历页面 (/resume)
- 个人信息和联系方式
- 专业摘要
- 完整工作经历
- 核心技能分类
- 教育背景
- 奖项与认证

### 🎨 作品集 (/portfolio)
- 5 个主要项目
- 项目描述、技术栈、链接
- 响应式网格展示
- 项目详情页面

### 🔗 API 端点
- `GET /api/projects` - 获取所有项目
- `GET /api/skills` - 获取所有技能

---

## 💡 内容已包含

✅ **个人信息**
- 姓名: Luqi Dong
- 邮箱: l.rockydong@outlook.com
- 电话: +31-616667957
- 位置: Enschede, Netherlands

✅ **真实项目**
1. AI/LLM 在 GIS 测试自动化中的应用（Accenture NL）
2. 共享微出行用户行为建模研究（PhD）
3. 基于 GPS 轨迹的城市可达性时空模型（Master）
4. 城市交通可达性分析
5. 个人网站项目

✅ **真实工作经验**
1. Accenture NL - Data & NLP Intern (2025.11 - 现在)
2. University of Twente - PhD Researcher (2021.10 - 现在)
3. Beijing Jiaotong University - Master Student (2018.09 - 2021.06)

✅ **30+ 项真实技能**
- AI & Generative AI (LLM, RAG, PyTorch, Transformers)
- Data Science & ML (Predictive Modeling, Machine Learning, Behavioral Modeling)
- GIS & Spatial Analysis (ArcGIS, GeoPandas, GPS Trajectory Analysis)
- Programming (Python, R, SQL, Git)
- Data Visualization (Power BI, Matplotlib, Interactive Dashboards)
- Statistical Methods (Latent Class Models, Regression, A/B Testing)

---

## 🎯 下一步建议

### 立即优先级
- [ ] 上传个人头像照片（替换占位符）
- [ ] 添加项目缩图和 GitHub 链接
- [ ] 完善社交媒体链接，设置联系表单

### 部署相关
- [ ] 选择部署平台（推荐 Vercel）
- [ ] 配置域名
- [ ] 设置 HTTPS/SSL
- [ ] SEO 优化

### 功能增强
- [ ] 添加博客功能
- [ ] 实现暗色主题
- [ ] 添加多语言支持
- [ ] 集成 Google Analytics

---

## 🔧 常见命令

### 进入 Flask Shell（调试数据）
```bash
flask --app run shell
```

### 查看所有项目
```bash
Project.query.all()
```

### 添加新项目
```python
new_project = Project(
    title='项目名称',
    description='项目描述',
    technologies='Python, Flask, etc.',
    featured=True
)
db.session.add(new_project)
db.session.commit()
```

### 导出数据库
```bash
# SQLite 数据库文件位置
instance/app.db
```

---

## 📚 文件结构

```
personal-website/
├── app/
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/main.js
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── portfolio.html
│   │   ├── project_detail.html
│   │   └── resume.html
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── instance/
│   └── app.db (创建后存在)
├── run.py
├── config.py
├── requirements.txt
├── README.md
├── QUICKSTART.md
└── .gitignore
```

---

## ❓ 遇到问题？

### 数据库错误
如果遇到数据库问题，删除 `instance/` 文件夹然后重新运行：
```bash
rmdir /s instance
flask --app run init-db
flask --app run seed-db
```

### 导入错误
确保虚拟环境已激活并安装了所有依赖：
```bash
pip install -r requirements.txt
```

### 端口被占用
如果 5000 端口被占用，修改 `run.py` 中的端口号：
```python
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
```

---

## 📞 联系信息

**Luqi Dong**
- Email: l.rockydong@outlook.com
- Phone: +31-616667957
- Location: Enschede, Netherlands

---

**祝你网站使用愉快！** 🎉
