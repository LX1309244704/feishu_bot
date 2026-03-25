#!/usr/bin/env python3
"""
一键安装飞书智能客服Bot
"""

import os
import sys

def install_dependencies():
    """安装依赖"""
    print("🦞 安装Python依赖...")
    os.system("pip install -r requirements.txt")
    print("✅ 依赖安装完成")

def configure_environment():
    """配置环境变量"""
    print("\n🦞 配置环境变量...")

    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')
            print("✅ .env 文件已创建（从 .env.example 复制）")
            print("⚠️  请编辑 .env 文件，填入你的凭证")
        else:
            print("❌ .env.example 文件不存在")
            return False
    else:
        print("✅ .env 文件已存在")

    return True

def run_install():
    """运行安装流程"""
    print("\n🦞 开始安装流程...")

    try:
        from services.webhook_service import WebhookService
        from services.feishu_service import FeishuService
        from services.coze_service import CozeService

        ws = WebhookService(FeishuService(), CozeService())
        result = ws.install_bot()

        print("\n🎉 安装完成！")
        print(f"配置文件已保存: config.json")

        return True
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("🦞 飞书智能客服Bot集成助手 - 一键安装")
    print("=" * 50)

    # 1. 安装依赖
    install_dependencies()

    # 2. 配置环境变量
    if not configure_environment():
        print("\n❌ 环境变量配置失败")
        return 1

    # 3. 询问是否继续
    print("\n" + "=" * 50)
    answer = input("是否继续安装? (y/n): ")

    if answer.lower() != 'y':
        print("❌ 安装已取消")
        return 0

    # 4. 运行安装
    if run_install():
        print("\n" + "=" * 50)
        print("下一步:")
        print("1. 编辑 .env 文件，填入你的凭证")
        print("2. 运行: python app.py")
        print("3. 访问: http://localhost:8080")
        print("4. 配置飞书Webhook: https://your-server.com/webhook")
        print("=" * 50)
        return 0
    else:
        return 1

if __name__ == '__main__':
    sys.exit(main())
