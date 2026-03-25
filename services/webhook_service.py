"""
Webhook服务模块
"""

import os
import json
from models.router import IntelligentRouter

class WebhookService:
    """Webhook处理服务"""

    def __init__(self, feishu_service, coze_service):
        self.feishu = feishu_service
        self.coze = coze_service
        self.router = IntelligentRouter(feishu_service, coze_service)

    def handle_message(self, data):
        """处理Webhook消息"""
        print("🦞 收到Webhook消息")

        # 1. 解析消息
        message = self._parse_message(data)

        # 2. 路由处理
        result = self.router.route_message(message)

        # 3. 发送回复
        if result.get("answer"):
            self.feishu.send_message(
                message["chat_id"],
                result["answer"]
            )

        return {
            "status": "success",
            "message_id": message.get("message_id"),
            "result": result
        }

    def _parse_message(self, data):
        """解析飞书消息"""
        event = data.get("event", {})

        # 解析内容
        content = event.get("message", {}).get("content", "")
        if isinstance(content, str):
            try:
                content = json.loads(content)
            except:
                pass

        return {
            "message_id": event.get("message", {}).get("message_id"),
            "chat_id": event.get("message", {}).get("chat_id"),
            "content": content.get("text", "") if isinstance(content, dict) else str(content),
            "msg_type": event.get("message", {}).get("msg_type", "text"),
            "sender_id": event.get("sender", {}).get("sender_id"),
            "conversation_id": event.get("message", {}).get("chat_id")
        }

    def install_bot(self):
        """一键安装Bot"""
        print("🦞 开始一键安装Bot...")

        # 1. 创建飞书应用
        app_info = self.feishu.create_application(
            name="智能客服Bot",
            description="基于AI的智能客服系统"
        )

        # 2. 配置权限
        self.feishu.configure_permissions(app_info['app_id'])

        # 3. 配置事件订阅
        webhook_url = os.getenv('WEBHOOK_URL', 'https://your-server.com/webhook')
        self.feishu.configure_event_subscription(app_info['app_id'], webhook_url)

        # 4. 创建扣子Bot
        bot_info = self.coze.create_bot(
            name="智能客服助手",
            description="专业的客服问答助手",
            instructions="你是一个专业的客服助手，能够回答用户的各种问题..."
        )

        # 5. 配置Bot Webhook
        self.coze.configure_webhook(bot_info['bot_id'], webhook_url)

        # 6. 创建知识库
        kb_info = self.feishu.create_knowledge_base(
            name="客服知识库",
            description="客户常见问题解答库"
        )

        # 7. 生成配置
        config = {
            "feishu": {
                "app_id": app_info['app_id']
            },
            "coze": {
                "bot_id": bot_info['bot_id']
            },
            "knowledge_base": {
                "space_id": kb_info['space_id']
            }
        }

        # 保存配置
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)

        print("🎉 Bot安装完成！")
        print(f"配置文件已保存: config.json")

        return {
            "status": "success",
            "config": config
        }
