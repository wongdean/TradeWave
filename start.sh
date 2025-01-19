#!/bin/bash

# 获取conda的基础路径
if [[ -z "${CONDA_EXE}" ]]; then
    if command -v conda >/dev/null 2>&1; then
        CONDA_PATH=$(conda info --base)
    else
        echo "Error: conda not found. Please install conda first."
        exit 1
    fi
else
    CONDA_PATH=$(dirname $(dirname ${CONDA_EXE}))
fi

# 初始化conda
source "${CONDA_PATH}/etc/profile.d/conda.sh"

# 检查并创建环境
if ! conda env list | grep -q "^tradewave "; then
    echo "Creating conda environment 'tradewave'..."
    conda create -n tradewave python=3.12 -y
fi

# 激活环境
echo "Activating tradewave environment..."
conda activate tradewave

# 验证Python环境
if ! command -v python &> /dev/null || ! command -v pip &> /dev/null; then
    echo "Error: Python or pip not found in current environment"
    echo "Please check your conda installation and environment"
    exit 1
fi

# 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -e .

# 运行项目
python run.py 