@echo off
REM 自动推送到 GitHub 的脚本

echo ========================================
echo 自动推送到 GitHub
echo ========================================
echo.

cd /d "c:\UT Journey\Projects for VScode\personal-website"

REM 检查 git 是否已安装
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: Git 未安装
    echo 请从 https://git-scm.com/download/win 下载安装
    pause
    exit /b 1
)

echo ✓ Git 已检测到

REM 检查是否已初始化
if not exist ".git" (
    echo.
    echo 正在初始化 Git 仓库...
    git init
    
    echo.
    echo 请复制以下命令并在此粘贴你的 GitHub 仓库 URL：
    echo 例如: https://github.com/yourusername/personal-website.git
    echo.
    set /p GITHUB_URL="输入你的 GitHub 仓库 URL: "
    
    git remote add origin %GITHUB_URL%
    echo ✓ 远程仓库已设置
)

REM 配置 git 用户（如果未配置）
for /f "delims=" %%i in ('git config --global user.name') do set GIT_USER=%%i
if "%GIT_USER%"=="" (
    echo.
    echo 正在配置 Git 用户...
    set /p USER_NAME="输入你的 GitHub 用户名: "
    set /p USER_EMAIL="输入你的 GitHub 邮箱: "
    git config --global user.name "%USER_NAME%"
    git config --global user.email "%USER_EMAIL%"
)

REM 添加所有文件
echo.
echo 正在暂存所有文件...
git add .
echo ✓ 文件已暂存

REM 提交
echo.
set /p COMMIT_MSG="输入提交信息 (默认: 'Update personal website'): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Update personal website
git commit -m "%COMMIT_MSG%"
echo ✓ 提交完成

REM 推送
echo.
echo 正在推送到 GitHub...
git push -u origin main
if errorlevel 1 (
    echo.
    echo ⚠️ 提示: 如果分支不是 'main'，尝试推送到 'master'
    git push -u origin master
)
echo ✓ 推送完成

echo.
echo ========================================
echo ✅ Git 流程已完成！
echo ========================================
echo.
echo 下一步:
echo 1. 访问 https://vercel.com
echo 2. 使用 GitHub 账户登录
echo 3. 导入你的仓库
echo 4. 部署！
echo.

pause
