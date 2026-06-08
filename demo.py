"""
awesome-copilot-wrap - Python Demo
GitHub Copilot 优质资源列表封装示例

演示如何通过 GitHub API 获取 awesome-copilot 资源信息。
"""

import requests
import base64
import json
import os
from typing import List, Dict, Optional

# ============================================================
# 配置 / Configuration
# ============================================================
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "your_token_here")
REPO_OWNER = "github"
REPO_NAME = "awesome-copilot"
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


# ============================================================
# 核心函数 / Core Functions
# ============================================================

def get_file_content(path: str) -> str:
    """
    获取仓库中指定文件的内容（Base64 解码）

    Args:
        path: 文件路径，如 "README.md", "docs/README.agents.md"

    Returns:
        文件内容字符串
    """
    url = f"{BASE_URL}/contents/{path}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content


def list_directory(path: str) -> List[Dict]:
    """
    列出仓库目录下的所有文件和文件夹

    Args:
        path: 目录路径，如 "docs", "cookbook"

    Returns:
        文件/文件夹信息列表
    """
    url = f"{BASE_URL}/contents/{path}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_repo_info() -> Dict:
    """
    获取仓库基本信息

    Returns:
        仓库信息字典
    """
    resp = requests.get(BASE_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


# ============================================================
# 示例函数 / Demo Functions
# ============================================================

def demo_get_readme():
    """示例：获取 README 内容"""
    print("\n" + "=" * 60)
    print("📖 示例1：获取 README.md 内容")
    print("=" * 60)

    try:
        content = get_file_content("README.md")
        lines = content.split("\n")
        print(f"README 总行数: {len(lines)}")
        print(f"前 10 行预览:")
        print("-" * 40)
        for line in lines[:10]:
            print(line)
        print("-" * 40)
    except Exception as e:
        print(f"❌ 获取 README 失败: {e}")


def demo_list_docs():
    """示例：列出 docs 目录结构"""
    print("\n" + "=" * 60)
    print("📂 示例2：列出 docs 目录结构")
    print("=" * 60)

    try:
        items = list_directory("docs")
        for item in items:
            icon = "📄" if item["type"] == "file" else "📁"
            print(f"  {icon} {item['name']}")
    except Exception as e:
        print(f"❌ 列出 docs 目录失败: {e}")


def demo_list_cookbook():
    """示例：列出 cookbook 目录"""
    print("\n" + "=" * 60)
    print("🍳 示例3：列出 cookbook 目录")
    print("=" * 60)

    try:
        items = list_directory("cookbook")
        for item in items:
            icon = "📄" if item["type"] == "file" else "📁"
            print(f"  {icon} {item['name']}")
    except Exception as e:
        print(f"❌ 列出 cookbook 目录失败: {e}")


def demo_get_repo_stats():
    """示例：获取仓库统计信息"""
    print("\n" + "=" * 60)
    print("📊 示例4：获取仓库统计信息")
    print("=" * 60)

    try:
        info = get_repo_info()
        print(f"  仓库名: {info['name']}")
        print(f"  描述: {info['description']}")
        print(f"  ⭐ 星标数: {info['stargazers_count']}")
        print(f"  🍴 Fork数: {info['forks_count']}")
        print(f"  👀 Watch数: {info['watchers_count']}")
        print(f"  📝 最后提交: {info['updated_at']}")
    except Exception as e:
        print(f"❌ 获取仓库信息失败: {e}")


def demo_fetch_resource_doc(doc_name: str):
    """
    示例：获取指定资源文档

    Args:
        doc_name: 文档名称，如 "README.agents.md"
    """
    print(f"\n📋 获取资源文档: {doc_name}")
    try:
        content = get_file_content(f"docs/{doc_name}")
        lines = content.split("\n")
        print(f"总行数: {len(lines)}")
        # 显示前20行
        print("预览:")
        for line in lines[:20]:
            print(f"  {line}")
    except Exception as e:
        print(f"❌ 获取失败: {e}")


# ============================================================
# 主程序 / Main
# ============================================================

def main():
    print("\n" + "=" * 60)
    print("🤖 Awesome Copilot Resource Demo")
    print("GitHub Copilot 优质资源封装示例")
    print("=" * 60)

    # 检查 Token
    if GITHUB_TOKEN == "your_token_here" or not GITHUB_TOKEN:
        print("\n⚠️  警告: 未设置 GITHUB_TOKEN 环境变量")
        print("请设置: export GITHUB_TOKEN=your_token_here")
        print("或者在代码中修改 GITHUB_TOKEN 变量")
        print("\n部分示例可能无法运行，但基础浏览功能仍可演示。\n")

    # 运行所有示例
    demo_get_repo_stats()
    demo_get_readme()
    demo_list_docs()
    demo_list_cookbook()

    # 演示获取具体资源文档
    print("\n" + "=" * 60)
    print("📋 示例5：获取 Agents 资源文档")
    print("=" * 60)
    demo_fetch_resource_doc("README.agents.md")

    print("\n" + "=" * 60)
    print("✅ 所有示例执行完成！")
    print("🌐 更多资源请访问: https://awesome-copilot.github.com")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()