#!/bin/bash

# macOS/Linux 快速启动脚本

echo "========================================"
echo "个人网站 - macOS/Linux 快速启动脚本"
echo "========================================"
echo ""

# 检查 Python 是否已安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: Python 未安装"
    echo "请安装 Python 3.8+ 版本"
    exit 1
fi

echo "✓ Python 已检测到: $(python3 --version)"

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo ""
    echo "正在创建虚拟环境..."
    python3 -m venv venv
    echo "✓ 虚拟环境已创建"
fi

# 激活虚拟环境
echo ""
echo "正在激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo "✓ 虚拟环境已激活"
echo ""
echo "正在升级 pip..."
python -m pip install --upgrade pip

# 安装依赖
echo ""
echo "正在安装依赖..."
pip install -r requirements.txt
echo "✓ 依赖已安装"

# 初始化数据库
echo ""
echo "正在初始化数据库..."
flask --app run init-db
echo "✓ 数据库已初始化"

# 添加示例数据
echo ""
echo "正在添加真实数据..."
flask --app run seed-db
echo "✓ 数据添加完成"

# 启动应用
echo ""
echo "========================================"
echo "✅ 所有准备完成！"
echo "========================================"
echo ""
echo "正在启动 Flask 应用..."
echo ""
echo "🌐 访问地址: http://127.0.0.1:5000"
echo ""
echo "按 Ctrl+C 停止服务器"
echo ""

python run.py
