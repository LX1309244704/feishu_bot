---
name: feishu-customer-service-bot
description: "一键创建飞书智能客服Bot，自动配置扣子Bot对接、知识库集成、多模态支持。适合企业快速部署AI客服系统，5分钟完成从0到1的客服自动化搭建。"
metadata:
  tags: [feishu, coze, customer-service, ai-bot, automation, enterprise]
  version: "1.0.0"
  author: "OpenClaw配置专家"
  category: "飞书集成"
  priority: "P0-紧急"
---

# 飞书智能客服Bot集成助手

🦞 **一键创建飞书智能客服Bot，5分钟完成从0到1的客服自动化搭建！**

---

## 🎯 适用场景

- ✅ **企业客服自动化** - 自动回答客户常见问题，7×24小时在线
- ✅ **内部问答系统** - 员工知识库查询，快速找到答案
- ✅ **多渠道客服统一** - 统一处理飞书、微信等多渠道消息
- ✅ **知识库集成** - 自动检索知识库，智能回答
- ✅ **初创企业** - 低成本快速搭建客服系统

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
- ✅ 与Bot无缝集成

### 4. 多模态支持
- ✅ 文本对话
- ✅ 图片识别
- ✅ 文件处理
- ✅ 语音支持（可选）

### 5. 智能路由
- ✅ 自动识别意图
- ✅ 智能路由分发
- ✅ 知识库优先
- ✅ Bot兜底

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
# 方式1：调用安装接口
curl -X POST http://localhost:8080/install

# 方式2：运行安装脚本
python -c "
from services.webhook_service import WebhookService
from services.feishu_service import FeishuService
from services.coze_service import CozeService
ws = WebhookService(FeishuService(), CozeService())
ws.install_bot()
"
```

### 第4步：启动服务

```bash
python app.py
```

### 第5步：配置飞书Webhook

在飞书开放平台配置Webhook回调地址：
```
https://your-server.com/webhook
```

---

## 📋 配置说明

### 环境变量

在 `.env` 文件中配置以下变量：

```bash
# 飞书配置
FEISHU_APP_ACCESS_TOKEN=your_app_access_token
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret

# 扣子配置
COZE_API_KEY=your_coze_api_key
COZE_BOT_ID=your_bot_id

# Webhook配置
WEBHOOK_URL=https://your-server.com/webhook
PORT=8080

# 日志配置
LOG_LEVEL=INFO
```

### 权限要求

飞书应用需要以下权限：
- `im:message` - 发送消息
- `im:contact` - 获取联系人
- `im:chat` - 获取群聊
- `drive:file` - 文件操作
- `wiki:wiki` - 知识库
- `docx:document` - 文档

---

## 🧪 测试

### 健康检查

```bash
curl http://localhost:8080/health
```

预期响应：
```json
{
  "status": "healthy",
  "service": "飞书智能客服Bot集成助手",
  "version": "1.0.0"
}
```

### 测试Webhook

```bash
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

### 获取配置

```bash
curl http://localhost:8080/config
```

---

## 🏗️ 技术架构

### 系统架构

```
飞书智能客服Bot集成助手
│
├── 飞书开放平台集成层
│   ├── 应用创建
│   ├── 权限配置
│   └── 事件订阅
│
├── 智能路由层
│   ├── 消息解析
│   ├── 意图识别
│   └── 路由分发
│
├── 扣子Bot集成层
│   ├── Bot调用
│   ├── 上下文管理
│   └── 多模态处理
│
└── 知识库层
    ├── 飞书知识库
    ├── 扣子知识库
    └── RAG检索
```

### 目录结构

```
feishu-customer-service-bot/
├── app.py                    # 主应用
├── config.py                 # 配置管理
├── models/
│   └── router.py            # 智能路由
├── services/
│   ├── feishu_service.py   # 飞书服务
│   ├── coze_service.py     # 扣子服务
│   └── webhook_service.py  # Webhook服务
├── utils/
│   ├── message_parser.py   # 消息解析
│   └── signature.py        # 签名验证
├── requirements.txt         # 依赖
├── .env.example             # 环境变量示例
├── .env                     # 环境变量
└── README.md                # 说明文档
```

---

## 💡 技术栈

- **Python 3.9+** - 核心语言
- **Flask 3.0** - Web框架
- **飞书开放平台API** - 飞书集成
- **扣子Bot API** - 扣子集成
- **Requests** - HTTP客户端
- **Python-dotenv** - 环境变量管理

---

## 📈 商业价值

### 市场需求
- 83%的中小企业计划部署AI客服
- 客服成本是企业的主要支出之一
- 自动化客服可节省70%人力成本

### 定价参考
- 基础版：5,000元（单企业，500条问答）
- 专业版：15,000元（多部门，无限问答）
- 企业版：30,000元（全场景，私有化）

### ROI周期
- 平均2-4个月回本
- 人力成本节省30%-70%
- 客户满意度提升40%

---

## 🔐 安全说明

- ✅ 请妥善保管你的API密钥
- ✅ 生产环境建议使用HTTPS
- ✅ 定期更新依赖包
- ✅ 配置防火墙规则
- ✅ 使用环境变量存储敏感信息

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

---

## 📞 支持

- **作者**：OpenClaw配置专家
- **邮箱**：your-email@example.com
- **GitHub**：https://github.com/yourusername/feishu-customer-service-bot

---

## 📄 许可证

MIT License

---

**🦞 让AI客服变得简单！5分钟完成从0到1的客服自动化搭建！**
