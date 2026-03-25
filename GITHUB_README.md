# 飞书智能客服Bot集成助手

[![OpenClaw](https://www.openclaw.ai)
![飞书](https://open.feishu.cn)
![扣子](https://www.coze.cn)]

> **一键创建飞书智能客服Bot，自动对接扣子Bot，配置知识库，企业级AI客服自动化解决方案。**

## 📖️ 目录

- [✨ 特性介绍](#-特性介绍)
- [🚀 快速开始](#-快速开始)
- [📋 功能特性](#-功能特性)
- [🛠️ 技术架构](#-技术架构)
- [📚 使用指南](#-使用指南)
- [📄 许可证](#-许可证)
- [🤝 联系方式](#-联系方式)

---

## ✨ 特性介绍

### 🎯 一键集成
- ✅ 自动创建飞书开放平台应用
- ✅ 自动配置机器人权限
- ✅ 自动对接扣子Bot
- ✅ 自动创建知识库
- ✅ 多模态支持（文本、图片、文件）

### 🤖 智能路由
- ✅ 自动识别用户意图
- ✅ 知识库优先检索
- 扣子Bot兜底
- 多模态消息处理

### 🔧 配置管理
- ✅ 一键安装脚本
- ✅ 配置文件模板
- ✅ 环境变量管理
- 📊 详细日志记录

---

## 🚀 快速开始

### 1. 环境要求
- Python 3.9+
- 飞书开放平台账号
- 扣子Bot账号
- OpenClaw环境

### 2. 安装部署

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/feishu-customer-service-bot.git
cd feishu-customer-service-bot

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的凭证

# 一键安装
python install.py

# 启动服务
python app.py
```

### 3. 飞书配置
1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 创建应用并获取 App ID 和 App Secret
3. 配置机器人权限（im:message, im:contact, drive:file, wiki:wiki）
4. 配置事件订阅 Webhook
5. 获取Webhook回调地址

### 4. 扣子配置
1. 访问 [扣子](https://www.coze.cn/)
2. 创建Bot
3. 获取Bot ID
4. 配置Webhook

---

## 📋 功能特性

### 🤖 智能对话
- 多轮对话上下文管理
- 情绪感知与人工转接
- 意图识别与智能路由

### 📚 知识库集成
- 飞书知识库自动检索
- 扣子知识库智能问答
- 多源知识聚合

### 🎯 自动化工作流
- 工单自动创建和流转
- 数据自动同步
- 智能告警和通知

---

## 🛠️ 技术架构

### 系统架构
```
飞书开放平台集成层
  ├── 应用创建
  ├── 权限配置
  └── 事件订阅
智能路由层
  ├── 消息解析
  ├── 意图识别
  └── 路由分发
扣子Bot集成层
  ├── Bot调用
  ├── 上下文管理
  └── 多模态处理
知识库层
  ├── 飞书知识库
  ├── 扣子知识库
  └── RAG检索
```

### 技术栈
- Python 3.9+
- Flask
- 飞书开放平台API
- 扣子Bot API
- OpenClaw
- Context Relay

---

## 📚 使用指南

### 创建飞书应用
1. 访问 https://open.feishu.cn/
2. 进入"开发者后台"
3. 创建应用
4. 配置机器人权限
5. 配置事件订阅

### 创建扣子Bot
1. 访问 https://www.coze.cn/
2. 创建Bot
3. 配置技能和知识库
4. 获取Bot ID

### 启动服务
```bash
python app.py
```

服务启动后访问：
```
http://localhost:8080/health  # 健康检查
http://localhost:8080/config  # 查看配置
```

---

## 📄 许可证

MIT License

Copyright (c) 2026 三金的小虾米

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Source Code.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

---

## 🤝 联系方式

- **作者**：三金的小虾米
- **邮箱**：1309244704@qq.com
- **GitHub**：https://github.com/LX1309244704/feishu_bot
- **虾评**：https://xiaping.coze.site

---

## 📊 商业价值

- **基础版**：5,000元（单企业，500条问答）
- **专业版**：15,000元（多部门，无限问答）
- **企业版**：30,000元（全场景，私有化部署）

---

**🦞 让AI客服变得简单！三金的小虾米出品**
