@echo off
REM Windows 快速启动脚本

echo ========================================
echo 个人网站 - Windows 快速启动脚本
echo ========================================
echo.

REM 检查 Python 是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: Python 未安装或不在 PATH 中
    echo 请安装 Python 3.8+ 版本
    pause
    exit /b 1
)

echo ✓ Python 已检测到

REM 创建虚拟环境
if not exist "venv" (
    echo.
    echo 正在创建虚拟环境...
    python -m venv venv
    echo ✓ 虚拟环境已创建
)

REM 激活虚拟环境
echo.
echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

REM 升级 pip
echo ✓ 虚拟环境已激活
echo.
echo 正在升级 pip...
python -m pip install --upgrade pip

REM 安装依赖
echo.
echo 正在安装依赖...
pip install -r requirements.txt
echo ✓ 依赖已安装

REM 初始化数据库
echo.
echo 正在初始化数据库...
flask --app run init-db
echo ✓ 数据库已初始化

REM 添加示例数据
echo.
echo 正在添加真实数据...
flask --app run seed-db
echo ✓ 数据添加完成

REM 启动应用
echo.
echo ========================================
echo ✅ 所有准备完成！
echo ========================================
echo.
echo 正在启动 Flask 应用...
echo.
echo 🌐 访问地址: http://127.0.0.1:5000
echo.
echo 按 Ctrl+C 停止服务器
echo.

python run.py

pause
