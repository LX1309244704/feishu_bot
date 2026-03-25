# 飞书智能客服Bot集成助手 - 技术方案

## 项目概述

**技能名称**：飞书智能客服Bot集成助手
**优先级**：P0-紧急
**预计收益**：5万-30万/项目
**市场需求**：最大
**技术匹配度**：100%

---

## 核心功能

### 1. 自动创建飞书应用
- ✅ 自动配置飞书开放平台应用
- ✅ 自动设置机器人权限
- ✅ 自动生成App ID和App Secret
- ✅ 自动配置事件订阅

### 2. 对接扣子Bot
- ✅ 自动创建扣子Bot
- ✅ 配置扣子Webhook
- ✅ 智能路由对话到扣子
- ✅ 支持多模态（文本、图片、文件）

### 3. 配置知识库
- ✅ 自动创建飞书知识库
- ✅ 支持批量导入文档
- ✅ 智能问答配置
- ✅ 知识库与扣子Bot集成

### 4. 多模态支持
- ✅ 文本对话
- ✅ 图片识别
- ✅ 文件处理
- ✅ 语音支持（可选）

---

## 技术架构

```
┌─────────────────────────────────────────────────┐
│              飞书智能客服Bot集成助手               │
│  ┌───────────────────────────────────────────┐  │
│  │         飞书开放平台集成层                  │  │
│  │  - 应用创建                               │  │
│  │  - 权限配置                               │  │
│  │  - 事件订阅                               │  │
│  │  - Webhook接收                            │  │
│  └───────────────────────────────────────────┘  │
│                     ↓                             │
│  ┌───────────────────────────────────────────┐  │
│  │         智能路由层                         │  │
│  │  - 消息解析                               │  │
│  │  - 意图识别                               │  │
│  │  - 路由分发                               │  │
│  └───────────────────────────────────────────┘  │
│                     ↓                             │
│  ┌───────────────────────────────────────────┐  │
│  │         扣子Bot集成层                      │  │
│  │  - Bot调用                                │  │
│  │  - 上下文管理                             │  │
│  │  - 多模态处理                             │  │
│  └───────────────────────────────────────────┘  │
│                     ↓                             │
│  ┌───────────────────────────────────────────┐  │
│  │         知识库层                           │  │
│  │  - 飞书知识库                             │  │
│  │  - 扣子知识库                             │  │
│  │  - RAG检索                                │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 技术实现

### 1. 飞书应用创建模块

```python
import requests
import json

class FeishuAppCreator:
    def __init__(self, app_access_token):
        self.app_access_token = app_access_token
        self.base_url = "https://open.feishu.cn/open-apis"

    def create_application(self, name, description):
        """创建飞书应用"""
        url = f"{self.base_url}/application/v6/applications"
        headers = {
            "Authorization": f"Bearer {self.app_access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "app_name": name,
            "app_description": description,
            "app_type": ["robot"],
            "robot": {
                "open_id": "bot_xxx"
            }
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def configure_permissions(self, app_id):
        """配置机器人权限"""
        permissions = [
            "im:message",      # 发送消息
            "im:contact",      # 获取联系人
            "im:chat",         # 获取群聊
            "drive:file",      # 文件操作
            "wiki:wiki",       # 知识库
            "docx:document"    # 文档
        ]

        url = f"{self.base_url}/application/v6/applications/{app_id}/permissions"
        headers = {
            "Authorization": f"Bearer {self.app_access_token}",
            "Content-Type": "application/json"
        }
        data = {"permissions": permissions}
        response = requests.put(url, headers=headers, json=data)
        return response.json()

    def configure_event_subscription(self, app_id, webhook_url):
        """配置事件订阅"""
        url = f"{self.base_url}/application/v6/applications/{app_id}/event-subscriptions"
        headers = {
            "Authorization": f"Bearer {self.app_access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "event_subscription_url": webhook_url,
            "events": [
                "im.message.receive_v1",           # 接收消息
                "im.message.created_v1",           # 消息创建
                "im.file.created_v1"               # 文件上传
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
```

### 2. 扣子Bot对接模块

```python
import requests

class CozeBotConnector:
    def __init__(self, coze_api_key):
        self.api_key = coze_api_key
        self.base_url = "https://api.coze.cn/v1"

    def create_bot(self, name, description, instructions):
        """创建扣子Bot"""
        url = f"{self.base_url}/bot/create"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "name": name,
            "description": description,
            "instructions": instructions,
            "meta_info": {
                "language": "zh-CN"
            }
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def configure_webhook(self, bot_id, webhook_url):
        """配置Bot Webhook"""
        url = f"{self.base_url}/bot/{bot_id}/webhook"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "webhook_url": webhook_url,
            "events": ["message", "file_upload"]
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def call_bot(self, bot_id, message, context=None):
        """调用Bot"""
        url = f"{self.base_url}/bot/{bot_id}/chat"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "query": message,
            "conversation_id": context.get("conversation_id") if context else None,
            "user": context.get("user_id") if context else None
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
```

### 3. 智能路由模块

```python
class IntelligentRouter:
    def __init__(self, feishu_client, coze_client):
        self.feishu = feishu_client
        self.coze = coze_client

    def route_message(self, message):
        """智能路由消息"""
        # 1. 消息类型识别
        message_type = self.detect_message_type(message)

        # 2. 意图识别
        intent = self.detect_intent(message)

        # 3. 路由决策
        if intent == "knowledge_query":
            return self.route_to_knowledge_base(message)
        elif intent == "customer_service":
            return self.route_to_bot(message)
        elif message_type == "image":
            return self.route_to_image_recognition(message)
        elif message_type == "file":
            return self.route_to_file_processing(message)
        else:
            return self.route_to_default(message)

    def detect_message_type(self, message):
        """检测消息类型"""
        if message.get("msg_type") == "image":
            return "image"
        elif message.get("msg_type") == "file":
            return "file"
        else:
            return "text"

    def detect_intent(self, message):
        """检测意图（简化版）"""
        content = message.get("content", "")

        # 关键词匹配
        if any(keyword in content for keyword in ["查询", "搜索", "问题"]):
            return "knowledge_query"
        elif any(keyword in content for keyword in ["客服", "人工", "帮助"]):
            return "customer_service"
        else:
            return "default"

    def route_to_knowledge_base(self, message):
        """路由到知识库"""
        # 调用飞书知识库API
        result = self.feishu.search_knowledge(message.get("content"))
        return result

    def route_to_bot(self, message):
        """路由到扣子Bot"""
        # 调用扣子Bot
        result = self.coze.call_bot(
            bot_id="bot_xxx",
            message=message.get("content"),
            context={"conversation_id": message.get("conversation_id")}
        )
        return result
```

### 4. 知识库集成模块

```python
class KnowledgeBaseManager:
    def __init__(self, feishu_client):
        self.feishu = feishu_client

    def create_knowledge_base(self, name, description):
        """创建飞书知识库"""
        url = "https://open.feishu.cn/open-apis/wiki/v2/spaces"
        headers = {
            "Authorization": f"Bearer {self.feishu.app_access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "name": name,
            "description": description
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def upload_document(self, space_id, file_path):
        """上传文档到知识库"""
        # 1. 上传文件到飞书云盘
        file_token = self.feishu.upload_file(file_path)

        # 2. 创建文档节点
        url = f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes"
        headers = {
            "Authorization": f"Bearer {self.feishu.app_access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "node_type": "document",
            "title": file_path.split("/")[-1],
            "parent_node_token": "root",
            "obj_type": "doc"
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def search_knowledge(self, query, space_id):
        """搜索知识库"""
        url = f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes/search"
        headers = {
            "Authorization": f"Bearer {self.feishu.app_access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "query": query,
            "page_size": 10
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()
```

### 5. Webhook接收模块

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

class WebhookReceiver:
    def __init__(self, router, feishu_client):
        self.router = router
        self.feishu = feishu_client

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """处理飞书Webhook"""
    data = request.json

    # 1. 验证签名（可选）
    # if not verify_signature(data):
    #     return jsonify({"error": "Invalid signature"}), 403

    # 2. 解析消息
    message = parse_feishu_message(data)

    # 3. 路由处理
    result = router.route_message(message)

    # 4. 返回响应
    return jsonify(result)

def parse_feishu_message(data):
    """解析飞书消息"""
    event = data.get("event", {})
    return {
        "message_id": event.get("message", {}).get("message_id"),
        "chat_id": event.get("message", {}).get("chat_id"),
        "content": event.get("message", {}).get("content"),
        "msg_type": event.get("message", {}).get("msg_type"),
        "sender_id": event.get("sender", {}).get("sender_id"),
        "conversation_id": event.get("message", {}).get("chat_id")
    }

if __name__ == '__main__':
    # 初始化客户端
    feishu_client = FeishuAppCreator("your_app_access_token")
    coze_client = CozeBotConnector("your_coze_api_key")

    # 初始化路由器
    router = IntelligentRouter(feishu_client, coze_client)

    # 初始化Webhook接收器
    webhook = WebhookReceiver(router, feishu_client)

    # 启动服务
    app.run(host='0.0.0.0', port=8080)
```

---

## 部署流程

### 1. 环境准备

```bash
# 创建项目目录
mkdir feishu-customer-service-bot
cd feishu-customer-service-bot

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install flask requests python-dotenv
```

### 2. 配置文件

```bash
# .env
FEISHU_APP_ACCESS_TOKEN=your_app_access_token
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret

COZE_API_KEY=your_coze_api_key
COZE_BOT_ID=your_bot_id

WEBHOOK_URL=https://your-server.com/webhook
PORT=8080
```

### 3. 目录结构

```
feishu-customer-service-bot/
├── app.py                    # 主应用
├── config.py                 # 配置管理
├── models/
│   ├── feishu.py            # 飞书模型
│   ├── coze.py              # 扣子模型
│   └── router.py            # 路由模型
├── services/
│   ├── feishu_service.py   # 飞书服务
│   ├── coze_service.py     # 扣子服务
│   └── webhook_service.py  # Webhook服务
├── utils/
│   ├── message_parser.py   # 消息解析
│   └── signature.py        # 签名验证
├── templates/
│   └── index.html          # 可选：管理界面
├── requirements.txt         # 依赖
├── .env                     # 环境变量
└── README.md                # 说明文档
```

### 4. 安装脚本

```python
#!/usr/bin/env python3
"""
一键安装飞书智能客服Bot
"""

import os
import sys
from feishu_service import FeishuService
from coze_service import CozeService

def main():
    print("🦞 开始安装飞书智能客服Bot...")

    # 1. 创建飞书应用
    print("1️⃣ 创建飞书应用...")
    feishu_service = FeishuService()
    app_info = feishu_service.create_application(
        name="智能客服Bot",
        description="基于AI的智能客服系统"
    )
    print(f"✅ 飞书应用创建成功: {app_info['app_name']} (ID: {app_info['app_id']})")

    # 2. 配置权限
    print("2️⃣ 配置应用权限...")
    feishu_service.configure_permissions(app_info['app_id'])
    print("✅ 权限配置完成")

    # 3. 配置事件订阅
    print("3️⃣ 配置事件订阅...")
    webhook_url = os.getenv('WEBHOOK_URL', 'https://your-server.com/webhook')
    feishu_service.configure_event_subscription(app_info['app_id'], webhook_url)
    print(f"✅ 事件订阅配置完成: {webhook_url}")

    # 4. 创建扣子Bot
    print("4️⃣ 创建扣子Bot...")
    coze_service = CozeService()
    bot_info = coze_service.create_bot(
        name="智能客服助手",
        description="专业的客服问答助手",
        instructions="你是一个专业的客服助手，能够回答用户的各种问题..."
    )
    print(f"✅ 扣子Bot创建成功: {bot_info['name']} (ID: {bot_info['bot_id']})")

    # 5. 配置Bot Webhook
    print("5️⃣ 配置Bot Webhook...")
    coze_service.configure_webhook(bot_info['bot_id'], webhook_url)
    print("✅ Bot Webhook配置完成")

    # 6. 创建知识库
    print("6️⃣ 创建飞书知识库...")
    kb_info = feishu_service.create_knowledge_base(
        name="客服知识库",
        description="客户常见问题解答库"
    )
    print(f"✅ 知识库创建成功: {kb_info['name']} (ID: {kb_info['space_id']})")

    # 7. 生成配置文件
    print("7️⃣ 生成配置文件...")
    config = {
        "feishu": {
            "app_id": app_info['app_id'],
            "app_secret": app_info['app_secret']
        },
        "coze": {
            "bot_id": bot_info['bot_id'],
            "api_key": os.getenv('COZE_API_KEY')
        },
        "knowledge_base": {
            "space_id": kb_info['space_id']
        }
    }

    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    print("✅ 配置文件生成完成: config.json")

    print("\n🎉 安装完成！")
    print("\n下一步：")
    print("1. 配置 .env 文件中的环境变量")
    print("2. 运行: python app.py")
    print("3. 访问: http://localhost:8080")

if __name__ == '__main__':
    main()
```

---

## 使用指南

### 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/feishu-customer-service-bot.git
cd feishu-customer-service-bot

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的凭证

# 4. 运行安装脚本
python install.py

# 5. 启动服务
python app.py
```

### 测试

```bash
# 测试飞书Webhook
curl -X POST http://localhost:8080/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "event": {
      "message": {
        "message_id": "om_xxx",
        "chat_id": "oc_xxx",
        "content": "{\"text\":\"你好\"}",
        "msg_type": "text"
      },
      "sender": {
        "sender_id": "ou_xxx"
      }
    }
  }'
```

---

## SKILL.md

```markdown
---
name: feishu-customer-service-bot
description: "一键创建飞书智能客服Bot，自动配置扣子Bot对接、知识库集成、多模态支持。适合企业快速部署AI客服系统。"
metadata:
  tags: [feishu, coze, customer-service, ai-bot, automation]
  version: "1.0.0"
  author: "OpenClaw配置专家"
---

# 飞书智能客服Bot集成助手

一键创建飞书智能客服Bot，自动配置扣子Bot对接、知识库集成、多模态支持。

## 核心功能

- ✅ 自动创建飞书应用
- ✅ 自动配置机器人权限
- ✅ 自动对接扣子Bot
- ✅ 自动创建知识库
- ✅ 支持多模态（文本、图片、文件）
- ✅ 智能路由分发
- ✅ 一键安装部署

## 使用场景

- 企业客服自动化
- 内部问答系统
- 知识库集成
- 多渠道客服统一

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 一键安装
python install.py

# 启动服务
python app.py
```

## 配置说明

需要在 `.env` 文件中配置：

- `FEISHU_APP_ACCESS_TOKEN`: 飞书应用凭证
- `COZE_API_KEY`: 扣子API密钥
- `WEBHOOK_URL`: Webhook回调地址

## 技术栈

- Python 3.9+
- Flask (Web框架)
- 飞书开放平台API
- 扣子Bot API
- 多模态处理

## 许可证

MIT
```

---

## 下一步计划

### Week 1
- [x] 技术方案设计
- [ ] 创建GitHub仓库
- [ ] 实现飞书应用创建模块
- [ ] 实现扣子Bot对接模块
- [ ] 编写安装脚本

### Week 2
- [ ] 实现智能路由模块
- [ ] 实现知识库集成模块
- [ ] 编写测试用例
- [ ] 生成文档

### Week 3
- [ ] 上传到虾评平台
- [ ] 发表技能评测
- [ ] 制作演示视频

### Week 4
- [ ] 寻找测试用户
- [ ] 收集反馈
- [ ] 优化产品

---

**🚀 开发已启动！现在立即创建GitHub仓库并开始编码！**
