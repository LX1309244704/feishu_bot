"""
智能路由模块
"""

import os

class IntelligentRouter:
    """智能路由器"""

    def __init__(self, feishu_service, coze_service):
        self.feishu = feishu_service
        self.coze = coze_service

    def route_message(self, message):
        """智能路由消息"""
        print(f"🦞 路由消息: {message.get('content', '')[:50]}...")

        # 1. 检测消息类型
        message_type = self._detect_message_type(message)

        # 2. 检测意图
        intent = self._detect_intent(message)

        # 3. 路由决策
        if intent == "knowledge_query":
            return self._route_to_knowledge_base(message)
        elif intent == "customer_service":
            return self._route_to_bot(message)
        elif message_type == "image":
            return self._route_to_image_recognition(message)
        elif message_type == "file":
            return self._route_to_file_processing(message)
        else:
            return self._route_to_default(message)

    def _detect_message_type(self, message):
        """检测消息类型"""
        msg_type = message.get("msg_type", "text")

        if msg_type == "image":
            return "image"
        elif msg_type == "file":
            return "file"
        elif msg_type == "audio":
            return "audio"
        else:
            return "text"

    def _detect_intent(self, message):
        """检测意图（简化版）"""
        content = message.get("content", "").lower()

        # 关键词匹配
        keywords_knowledge = ["查询", "搜索", "问题", "问", "找"]
        keywords_customer = ["客服", "人工", "帮助", "咨询"]

        if any(keyword in content for keyword in keywords_knowledge):
            return "knowledge_query"
        elif any(keyword in content for keyword in keywords_customer):
            return "customer_service"
        else:
            return "default"

    def _route_to_knowledge_base(self, message):
        """路由到知识库"""
        print("🦞 路由到知识库")

        # 搜索知识库
        result = self.feishu.search_knowledge(
            query=message.get("content"),
            space_id="wiki_xxx"  # 这里应该从配置中读取
        )

        # 如果找到结果，返回第一个
        if result.get("results") and len(result["results"]) > 0:
            return {
                "source": "knowledge_base",
                "answer": result["results"][0].get("content"),
                "confidence": 0.9
            }
        else:
            # 知识库未找到，转Bot
            return self._route_to_bot(message)

    def _route_to_bot(self, message):
        """路由到扣子Bot"""
        print("🦞 路由到扣子Bot")

        # 调用Bot
        result = self.coze.call_bot(
            bot_id=os.getenv('COZE_BOT_ID', 'bot_xxx'),
            message=message.get("content"),
            context={
                "conversation_id": message.get("conversation_id"),
                "user_id": message.get("sender_id")
            }
        )

        return {
            "source": "coze_bot",
            "answer": result.get("answer"),
            "confidence": 0.95
        }

    def _route_to_image_recognition(self, message):
        """路由到图片识别"""
        print("🦞 路由到图片识别")

        # 这里可以集成图片识别服务
        return {
            "source": "image_recognition",
            "answer": "图片已收到，正在分析...",
            "confidence": 0.8
        }

    def _route_to_file_processing(self, message):
        """路由到文件处理"""
        print("🦞 路由到文件处理")

        # 这里可以集成文件处理服务
        return {
            "source": "file_processing",
            "answer": "文件已收到，正在处理...",
            "confidence": 0.8
        }

    def _route_to_default(self, message):
        """默认路由"""
        print("🦞 默认路由到Bot")

        # 默认路由到Bot
        return self._route_to_bot(message)
