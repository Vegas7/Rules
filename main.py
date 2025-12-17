import os
import requests

# ================= 配置区域 =================
# 在这里定义你要下载的规则和保存的文件名
# 格式： "保存的文件名.list": "下载源的URL"
# 注意：你需要把下面的 URL 换成你真正想引用的上游规则地址
SOURCES = {
    "AI_Services.list": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
    "Emby.list": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Emby/Emby.list",
    "Telegram.list": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list"
}

# 输出文件夹（保存到当前目录下的 Surge 文件夹）
OUTPUT_DIR = "./Surge"
# ===========================================

def download_and_save(filename, url):
    try:
        print(f"正在下载: {filename} ...")
        response = requests.get(url, timeout=10)
        response.raise_for_status() # 检查请求是否成功
        
        content = response.text
        
        # 可以在这里添加一些内容过滤或处理逻辑
        # 比如：只保留包含 DOMAIN 或 IP-CIDR 的行
        # filtered_lines = [line for line in content.split('\n') if not line.startswith('#')]
        
        # 拼接保存路径
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # 加上头部注释
            f.write(f"# Auto-generated from {url}\n")
            f.write("# Updated by Github Actions\n\n")
            f.write(content)
            
        print(f"✅ 成功保存: {filepath}")
        
    except Exception as e:
        print(f"❌ 下载失败 {filename}: {e}")

def main():
    # 1. 确保输出目录存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"创建目录: {OUTPUT_DIR}")

    # 2. 遍历下载
    for filename, url in SOURCES.items():
        download_and_save(filename, url)

if __name__ == "__main__":
    main()
