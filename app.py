#!/usr/bin/env python3
"""
飞书智能客服Bot集成助手 - 主应用
"""

import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from services.feishu_service import FeishuService
from services.coze_service import CozeService
from services.webhook_service import WebhookService
from models.router import IntelligentRouter

# 加载环境变量
load_dotenv()

app = Flask(__name__)

# 初始化服务
feishu_service = FeishuService()
coze_service = CozeService()
webhook_service = WebhookService(feishu_service, coze_service)

# 路由器初始化
router = IntelligentRouter(feishu_service, coze_service)

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查"""
    return jsonify({
        "status": "healthy",
        "service": "飞书智能客服Bot集成助手",
        "version": "1.0.0"
    })

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """处理飞书Webhook"""
    try:
        data = request.json
        result = webhook_service.handle_message(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/install', methods=['POST'])
def install_bot():
    """一键安装Bot"""
    try:
        result = webhook_service.install_bot()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/config', methods=['GET'])
def get_config():
    """获取配置"""
    try:
        config = {
            "feishu": {
                "app_id": os.getenv('FEISHU_APP_ID'),
                "webhook_url": os.getenv('WEBHOOK_URL')
            },
            "coze": {
                "bot_id": os.getenv('COZE_BOT_ID')
            }
        }
        return jsonify(config)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    debug = os.getenv('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
