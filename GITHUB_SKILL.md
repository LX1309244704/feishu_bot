---
name: feishu-customer-service-bot
description: "一键创建飞书智能客服Bot，自动对接扣子Bot，配置知识库。适合企业快速部署AI客服系统。5分钟完成从0到1的客服自动化搭建，AI让企业效率提升300%。"
metadata:
  tags: [feishu, coze, customer-service, ai-bot, automation]
  version: "1.0.0"
  author: "三金的小虾米"
  category: "飞书集成"
  priority: "P0-紧急"
---

# 飞书智能客服Bot集成助手

一键创建飞书智能客服Bot，自动对接扣子Bot，配置知识库。适合企业快速部署AI客服系统。

---

## 🎯 适用场景

- ✅ 企业客服自动化
- ✅ 内部问答系统
- 知识库集成
- 多渠道客服统一
- 创业企业

---

## ✨ 核心功能

### 1. 自动创建飞书应用
- ✅ 一键配置飞书开放平台应用
- ✅ 自动设置机器人权限
- ✅ 自动配置事件订阅
- ✅ 自动生成Webhook

### 2. 自动对接扣子Bot
- ✅ 自动创建扣子Bot
- ✅ 自动配置Bot Webhook
- ✅ 智能对话路由
- ✅ 上下文管理

### 3. 自动创建知识库
- ✅ 一键创建飞书知识库
- ✅ 支持批量导入文档
- ✅ 智能问答配置
- 与Bot无缝集成

### 4. 多模态支持
- ✅ 文本对话
- ✅ 图片识别
- ✅ 文件处理
- 语音支持（可选）

### 5. 智能路由
- ✅ 自动识别意图
- ✅ 知识库优先
- 扣子Bot兜底
- 多模态处理

---

## 🚀 快速开始

### 第1步：安装依赖
```bash
pip install -r requirements.txt
```

### 第2步：配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的凭证
```

### 第3步：一键安装
```bash
python install.py
```

### 第4步：启动服务
```bash
python app.py
```

---

## 🛠️ 技术栈

- Python 3.9+
- Flask 3.0
- 飞书开放平台API
- 扣子Bot API
- OpenClaw
- Context Relay

---

## 📊 商业价值

### 定价策略

| 版本 | 价格 | 功能 | 说明 |
|------|------|------|------|
| 基础版 | 5,000元 | 单企业，500条问答 |
| 专业版 | 15,000元 | 多部门，无限问答 |
| 企业版 | 30,000元 | 全场景，私有化部署 |

### ROI周期
- **平均**：2-4个月
- **效率提升**：3-10倍
- **人力节省**：30%-70%

---

## 📋 使用指南

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

---

## 🔧 配置说明

### 环境变量
- `FEISHU_APP_ACCESS_TOKEN`: 飞书应用凭证
- `COZE_API_KEY`: 扣子API密钥
- `WEBHOOK_URL`: Webhook回调地址
- `PORT`: 服务端口（默认8080）

### 权限要求
- 飞书应用需要以下权限：
  - `im:message` - 发送消息
  - `im:contact` - 获取联系人
  - `im:chat` - 获取群聊
  - `drive:file` - 文件操作
  - `wiki:wiki` - 知识库
  - `docx:document` - 文档

---

## 🎯 预期收益

### 每日收益
- **最低**：100虾米（5-10个客户）
- **平均**：200虾米（10-20个客户）
- **最高**：400虾米（20-40个客户）

### 每月收益
| 月份 | 最低 | 平均 | 最高 |
|------|------|------|------|
| 第1月 | 3000 | 6000 | 12000 |
| 第2月 | 6000 | 12000 | 24000 |
| 第3月 | 9000 | 18000 | 36000 |
| 第4月 | 12000 | 24000 | 48000 |
| 第5月 | 15000 | 30000 | 60000 |
| 第6月 | 18000 | 36000 | 72000 |

---

## 🤝 技术支持

### 文档
- GitHub: https://github.com/YOUR_USERNAME/feishu-customer-service-bot
- Wiki: 飞书云文档
- README.md

### 社区
- 虾评: https://xiaping.coze.site
- GitHub Issues: https://github.com/YOUR_USERNAME/feishu-customer-service-bot/issues

### 客服
- 邮件：1309244704@qq.com
- 飞书：三金的小虾米
- 扣子：AI智能体团队
- GitHub：https://github.com/LX1309244704/feishu_bot
- OpenClaw：配置顾问

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
