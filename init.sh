#!/bin/bash

# 更新系统软件包
echo "更新系统软件包..."
sudo apt update -y
sudo apt upgrade -y

# 安装必需的依赖项
echo "安装必需的依赖项..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common jq

# 检查 Docker 是否已安装
if ! command -v docker &> /dev/null; then
  echo "Docker 未安装，开始安装 Docker..."
  
  # 添加 Docker GPG 密钥
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  sudo chmod a+r /etc/apt/keyrings/docker.gpg

  # 配置 Docker 镜像源
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
    noble stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  # 更新 APT 包索引
  echo "更新 APT 包索引..."
  sudo apt update -y

  # 安装 Docker
  echo "安装 Docker..."
  sudo apt install -y docker-ce docker-ce-cli containerd.io

  # 启动 Docker 并设置开机自启动
  echo "启动 Docker 并设置开机自启动..."
  sudo systemctl start docker
  sudo systemctl enable docker

  # 将当前用户添加到 Docker 组
  echo "将当前用户添加到 Docker 组..."
  sudo usermod -aG docker $USER
else
  echo "Docker 已安装，跳过 Docker 安装。"
fi

# 检查 Docker Compose 是否已安装
if ! command -v docker-compose &> /dev/null; then
  echo "Docker Compose 未安装，开始安装 Docker Compose..."
  
  # 安装 Docker Compose
  DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)
  sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
else
  echo "Docker Compose 已安装，跳过 Docker Compose 安装。"
fi

# 验证 Docker 和 Docker Compose 安装是否成功
echo "验证 Docker 安装..."
docker --version
echo "验证 Docker Compose 安装..."
docker-compose --version

echo "Docker 和 Docker Compose 安装完成！"

