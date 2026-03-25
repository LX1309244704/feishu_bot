# 飞书智能客服Bot集成助手

🦞 一键创建飞书智能客服Bot，自动配置扣子Bot对接、知识库集成、多模态支持。

## ✨ 核心功能

- ✅ **自动创建飞书应用** - 一键配置飞书开放平台应用
- ✅ **自动配置权限** - 自动设置机器人所需权限
- ✅ **自动对接扣子Bot** - 自动创建并配置扣子Bot
- ✅ **自动创建知识库** - 一键创建飞书知识库
- ✅ **多模态支持** - 支持文本、图片、文件等
- ✅ **智能路由** - 自动识别意图，路由到最佳响应
- ✅ **一键安装部署** - 简单5步，快速上线

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的凭证
```

### 3. 一键安装

```bash
python -c "from services.webhook_service import WebhookService; from services.feishu_service import FeishuService; from services.coze_service import CozeService; ws = WebhookService(FeishuService(), CozeService()); ws.install_bot()"
```

或者：

```bash
curl -X POST http://localhost:8080/install
```

### 4. 启动服务

```bash
python app.py
```

服务将在 `http://localhost:8080` 启动

## 📋 使用场景

- **企业客服自动化** - 自动回答常见问题
- **内部问答系统** - 员工知识库查询
- **多渠道客服统一** - 统一处理各渠道消息
- **知识库集成** - 自动检索和回答

## 🔧 配置说明

需要在 `.env` 文件中配置：

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
```

## 🧪 测试

```bash
# 健康检查
curl http://localhost:8080/health

# 测试Webhook
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

# 获取配置
curl http://localhost:8080/config
```

## 🏗️ 技术架构

```
飞书智能客服Bot集成助手
├── 飞书开放平台集成层
│   ├── 应用创建
│   ├── 权限配置
│   └── 事件订阅
├── 智能路由层
│   ├── 消息解析
│   ├── 意图识别
│   └── 路由分发
├── 扣子Bot集成层
│   ├── Bot调用
│   ├── 上下文管理
│   └── 多模态处理
└── 知识库层
    ├── 飞书知识库
    ├── 扣子知识库
    └── RAG检索
```

## 📚 技术栈

- **Python 3.9+** - 核心语言
- **Flask** - Web框架
- **飞书开放平台API** - 飞书集成
- **扣子Bot API** - 扣子集成
- **多模态处理** - 图片、文件等

## 🔐 安全说明

- 请妥善保管你的API密钥
- 生产环境建议使用HTTPS
- 定期更新依赖包
- 配置防火墙规则

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

- 作者：OpenClaw配置专家
- 邮箱：your-email@example.com

---

**🦞 让AI客服变得简单！**
