# 🚀 Vercel 部署指南

## 部署前检查清单

✅ requirements.txt 已更新（添加了 gunicorn）
✅ vercel.json 配置文件已创建
✅ wsgi.py 入口文件已创建
✅ .vercelignore 忽略文件已创建

---

## 📋 部署步骤

### 步骤 1️⃣: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 创建新仓库名称：`personal-website`
3. 选择：**Public**（公开）
4. 取消勾选 "Initialize this repository with a README"
5. 点击 **Create repository**

---

### 步骤 2️⃣: 初始化 Git 并推送代码

在项目目录中运行这些命令：

```powershell
# 进入项目目录
cd "c:\UT Journey\Projects for VScode\personal-website"

# 初始化 Git
git init

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/personal-website.git

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Personal website with Flask, SQLAlchemy"

# 推送到 GitHub（可能需要输入 GitHub 凭证）
git branch -M main
git push -u origin main
```

💡 **提示**：如果看到认证提示，使用你的 GitHub 用户名和 personal access token（或 SSH key）

---

### 步骤 3️⃣: 在 Vercel 上部署

1. **访问 Vercel：** https://vercel.com
2. **点击** "Sign Up" 并选择 "Continue with GitHub"
3. **授权** Vercel 访问你的 GitHub 账户
4. **点击** "Import Project"
5. **选择** 你刚创建的 `personal-website` 仓库
6. **部署设置**（保持默认即可）：
   - Framework: Other（其他）
   - Root Directory: ./（默认）
7. **点击** "Deploy"

**等待 1-2 分钟，部署完成！** ✨

---

### 步骤 4️⃣: 获取网站 URL

部署完成后，Vercel 会给你一个公网 URL，看起来像：
```
https://personal-website-abc123.vercel.app
```

**这就是你的网站！** 🎉

---

## 🔒 数据库说明

⚠️ **重要**：Vercel 上的数据库是**内存数据库**，每次部署时会重置。

如果你想持久化数据，有两个选项：

### 选项 A：使用外部数据库（推荐）
- MongoDB（MongoDB Atlas - 免费）
- PostgreSQL（Railway、Neon - 免费）

### 选项 B：保持当前方式
- 数据在内存中，每次部署重置
- 但演示和招聘足够了！

---

## 📝 环境变量（可选）

如果需要设置环境变量：

1. 在 Vercel Dashboard 打开项目
2. 进入 Settings → Environment Variables
3. 添加所需变量（例如：API Keys）
4. 重新部署

---

## 🔄 更新网站

每次修改代码后：

```powershell
# 提交更改
git add .
git commit -m "更新描述"

# 推送到 GitHub
git push origin main
```

Vercel 会**自动重新部署**！ 🚀

---

## 🐛 调试

如果部署失败，查看日志：

1. 打开 Vercel Dashboard
2. 选择你的项目
3. 进入 "Deployments" 标签
4. 点击失败的部署查看错误日志

常见问题：
- ❌ Module not found: 检查 requirements.txt
- ❌ Port error: 已自动处理（Gunicorn）
- ❌ Database error: 使用 wsgi.py 中的自动初始化

---

## 💡 下一步优化

| 功能 | 难度 | 描述 |
|------|------|------|
| 自定义域名 | ⭐ | 连接你自己的域名 |
| SSL 证书 | ⭐ | Vercel 自动提供 HTTPS |
| 分析统计 | ⭐⭐ | 添加 Google Analytics |
| 联系表单 | ⭐⭐ | 添加 EmailJS 或 Formspree |
| 数据库持久化 | ⭐⭐⭐ | 使用外部数据库 |

---

## ❓ 常见问题

**Q: 需要付费吗？**
A: 不需要！Vercel 免费层包括无限部署、自动 HTTPS、全球 CDN。

**Q: 可以使用自己的域名吗？**
A: 可以！在 Vercel 设置中连接你的域名。

**Q: 网站会一直在线吗？**
A: 是的！24/7 在线，除非你删除项目。

**Q: 可以预览部署前的更改吗？**
A: 可以！每个 pull request 都会自动生成预览 URL。

---

## 📚 有用的链接

- Vercel 文档: https://vercel.com/docs
- Flask 部署: https://vercel.com/docs/frameworks/flask
- 域名连接: https://vercel.com/docs/concepts/projects/domains

---

**准备好了？让我们开始部署吧！** 🚀

需要我帮你执行这些步骤吗？
