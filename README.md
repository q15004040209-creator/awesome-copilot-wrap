# awesome-copilot-wrap

> 🤖 GitHub Copilot 优质资源封装 / GitHub Copilot Curated Resources Wrapper

[![Stars](https://img.shields.io/github/stars/q15004040209-creator/awesome-copilot-wrap?style=flat-square)](https://github.com/q15004040209-creator/awesome-copilot-wrap/stargazers)
[![Fork](https://img.shields.io/github/forks/q15004040209-creator/awesome-copilot-wrap?style=flat-square)](https://github.com/q15004040209-creator/awesome-copilot-wrap/network/members)
[![License](https://img.shields.io/github/license/q15004040209-creator/awesome-copilot-wrap?style=flat-square)](LICENSE)

---

## 🌐 介绍 / Introduction

本项目是对 [github/awesome-copilot](https://github.com/github/awesome-copilot) 的资源封装，由 GitHub 官方维护，**星标总数 34,634**。收录了自定义 Agent、指令集、Skills、Hooks、工作流和插件，旨在全面提升你的 GitHub Copilot 使用体验。

This project wraps [github/awesome-copilot](https://github.com/github/awesome-copilot) — GitHub's official curated list of Copilot and AI developer tool resources, with **34,634 total stars**. It collects custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your GitHub Copilot experience.

---

## 📂 资源分类 / Resource Categories

| 类型 | 英文 | 说明 |
|------|------|------|
| 🤖 Agents | [Agents](docs/README.agents.md) | 集成 MCP 服务器的专业化 Copilot Agent |
| 📋 Instructions | [Instructions](docs/README.instructions.md) | 按文件模式自动应用的编码规范 |
| 🎯 Skills | [Skills](docs/README.skills.md) | 包含指令和捆绑资源的多功能文件夹 |
| 🔌 Plugins | [Plugins](docs/README.plugins.md) | 针对特定工作流打包的 Agent + Skill 集合 |
| 🪝 Hooks | [Hooks](docs/README.hooks.md) | Copilot Agent 会话期间触发的自动化操作 |
| ⚡ Workflows | [Workflows](docs/README.workflows.md) | 用 Markdown 编写的 AI 驱动 GitHub Actions |
| 🍳 Cookbook | [Cookbook](cookbook/README.md) | Copilot API 使用的复制粘贴式配方 |

---

## 🚀 快速开始 / Quick Start

### 安装插件 / Install a Plugin

```bash
# 直接安装 Awesome Copilot 插件
copilot plugin install <plugin-name>@awesome-copilot

# 如果市场未注册，先添加再安装
copilot plugin marketplace add github/awesome-copilot
copilot plugin install <plugin-name>@awesome-copilot
```

### 在 AI Agent 中使用 / Use in AI Agent

机器可读的 `llms.txt` 文件已可用，方便 AI 智能体解析所有资源结构：

```
https://awesome-copilot.github.com/llms.txt
```

---

## 🐍 Python 示例代码 / Python Demo

本目录包含 Python 示例代码，演示如何调用 GitHub Copilot 相关资源接口。

This directory contains Python demo code that shows how to interact with GitHub Copilot resources.

```python
# demo.py - 示例：获取 awesome-copilot 资源列表
# Demo: Fetch awesome-copilot resource list via GitHub API

import requests
import base64
import json

GITHUB_TOKEN = "your_github_token_here"
REPO_OWNER = "github"
REPO_NAME = "awesome-copilot"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_readme_content(owner, repo, path="README.md"):
    """获取仓库中指定文件的内容（Base64 解码）"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content

def list_docs(owner, repo):
    """列出 docs 目录下的所有资源文档"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/docs"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    items = resp.json()
    return [item["name"] for item in items if item["type"] == "file" and item["name"].endswith(".md")]

def main():
    print("=== Awesome Copilot Resource Demo ===\n")

    # 获取 README
    print("📖 获取 README.md...")
    readme = get_readme_content(REPO_OWNER, REPO_NAME)
    print(f"README 长度: {len(readme)} 字符")

    # 列出 docs 目录文件
    print("\n📂 列出文档文件...")
    docs = list_docs(REPO_OWNER, REPO_NAME)
    for doc in docs:
        print(f"  - {doc}")

    print("\n✅ 完成！更多资源请访问: https://awesome-copilot.github.com")

if __name__ == "__main__":
    main()
```

运行方式 / Run:

```bash
pip install requests
python demo.py
```

---

## 🌐 在线资源 / Online Resources

| 资源 | 链接 |
|------|------|
| 🌐官方网站 | [awesome-copilot.github.com](https://awesome-copilot.github.com) |
| 📋全部 Agent | [agents](https://awesome-copilot.github.com/agents) |
| 🎯全部 Skills | [skills](https://awesome-copilot.github.com/skills) |
| 🔌全部 Plugins | [plugins](https://awesome-copilot.github.com/plugins) |
| 🪝全部 Hooks | [hooks](https://awesome-copilot.github.com/hooks) |
| ⚡全部 Workflows | [workflows](https://awesome-copilot.github.com/workflows) |
| 📖学习中心 | [learning-hub](https://awesome-copilot.github.com/learning-hub) |
| 🤖 llms.txt | [llms.txt](https://awesome-copilot.github.com/llms.txt) |

---

## ⚠️ 注意事项 / Note

> 本项目封装的资源来自第三方开发者，请在安装前仔细查阅相关 Agent 及其文档。
>
> The customizations here are sourced from third-party developers. Please inspect any agent and its documentation before installing.

---

## 📄 License

本项目基于原仓库协议。详细请参阅 [LICENSE](LICENSE)。

Based on the original repository license. See [LICENSE](LICENSE) for details.

---

⭐ 如果对你有帮助，请给本仓库一个 Star！
⭐ If you find this useful, please give this repo a Star!