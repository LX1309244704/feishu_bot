#!/usr/bin/env python3
"""
测试脚本 - 验证代码是否可以正常运行
"""

import sys
import os

def test_imports():
    """测试导入"""
    print("🦞 测试导入...")
    try:
        from services.feishu_service import FeishuService
        from services.coze_service import CozeService
        from services.webhook_service import WebhookService
        from models.router import IntelligentRouter
        print("✅ 导入成功")
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False

def test_services():
    """测试服务"""
    print("\n🦞 测试服务...")
    try:
        from services.feishu_service import FeishuService
        from services.coze_service import CozeService

        feishu = FeishuService()
        coze = CozeService()

        # 测试创建应用
        app_info = feishu.create_application("测试应用", "这是一个测试应用")
        print(f"✅ 飞书应用创建测试通过: {app_info['app_name']}")

        # 测试创建Bot
        bot_info = coze.create_bot("测试Bot", "测试Bot描述", "测试指令")
        print(f"✅ 扣子Bot创建测试通过: {bot_info['name']}")

        return True
    except Exception as e:
        print(f"❌ 服务测试失败: {e}")
        return False

def test_router():
    """测试路由器"""
    print("\n🦞 测试路由器...")
    try:
        from models.router import IntelligentRouter
        from services.feishu_service import FeishuService
        from services.coze_service import CozeService

        router = IntelligentRouter(FeishuService(), CozeService())

        # 测试消息路由
        test_message = {
            "message_id": "om_test",
            "chat_id": "oc_test",
            "content": "你好",
            "msg_type": "text",
            "sender_id": "ou_test"
        }

        result = router.route_message(test_message)
        print(f"✅ 路由测试通过: {result['source']}")

        return True
    except Exception as e:
        print(f"❌ 路由测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("🦞 飞书智能客服Bot集成助手 - 测试")
    print("=" * 50)

    results = []

    # 测试导入
    results.append(test_imports())

    # 测试服务
    results.append(test_services())

    # 测试路由器
    results.append(test_router())

    # 总结
    print("\n" + "=" * 50)
    print("🦞 测试总结")
    print("=" * 50)
    print(f"总测试数: {len(results)}")
    print(f"通过数: {sum(results)}")
    print(f"失败数: {len(results) - sum(results)}")

    if all(results):
        print("\n🎉 所有测试通过！")
        return 0
    else:
        print("\n❌ 部分测试失败")
        return 1

if __name__ == '__main__':
    sys.exit(main())
