# RemNote Alfred 5 Workflow

<p align="center">
  <img src="icon.png" width="128" height="128" alt="RemNote Icon">
</p>

<p align="center">
  <b>Lightning-fast search, quick capture, and note navigation for RemNote Desktop in Alfred 5.</b><br>
  为 RemNote 桌面端打造的原生极速 Alfred 5 工作流，毫秒级本地直连。
</p>

---

## ✨ Features (功能特性)

- 🔍 **`rns <keyword>`**: Real-time script filter searching your active RemNote knowledge base. Press `Enter` to instantly open that note in RemNote. (即时搜索笔记，回车秒开对应文档)
- ⚡️ **`rn <content>` / `rnc <content>`**: Quick capture a thought or task directly appended to today's Daily Note with system notification confirmation. (闪念速记一键追加到今日 Daily Note)
- 🕒 **`rnr`**: Browse and filter recently edited documents from the past 14 days. (查看最近编辑过的笔记)

---

## 🔑 Where to Find Your RemNote Token (如何获取 Token)

This workflow connects directly to your **running RemNote Desktop Application** via its local embedded MCP server (`http://127.0.0.1:7788/mcp`).

1. Open **RemNote Desktop App** (打开 RemNote 桌面端).
2. Click **Settings ⚙️** in the bottom-left sidebar (or press `Cmd/Ctrl + ,`).
3. In the left settings navigation, scroll down and click **Developer** (or **Integrations** / **Model Context Protocol**).
4. Make sure **Local MCP Server** is enabled.
5. Copy the **Bearer Token** (it starts with `rn_mcp_...`).

---

## 🚀 Installation & Setup (安装与配置)

### Step 1: Download & Install
Download [`RemNote.alfredworkflow`](RemNote.alfredworkflow) and double-click to install it in Alfred 5.

### Step 2: Configure Environment Variables
Upon installing (or by clicking the `[x]` button in Alfred Preferences -> Workflows -> RemNote Companion):
1. **Local Server URL**: `http://127.0.0.1:7788/mcp` (Default)
2. **Bearer Token**: Paste your `rn_mcp_...` token.

---

## ⚡️ Keyboard Shortcuts (使用指令)

| Keyword | Description | Action |
| :--- | :--- | :--- |
| **`rns <query>`** | Search notes in RemNote | Opens note in RemNote on `Enter`, copies title on `Cmd+C` |
| **`rn <text>`** | Quick capture to Daily Note | Appends text to today's Daily Note |
| **`rnc <text>`** | Quick capture to Daily Note (alias) | Appends text to today's Daily Note |
| **`rnr`** | Recent notes | Shows recent edited notes |

---

## 📄 License

MIT License © 2026 [bianyeyu](https://github.com/bianyeyu)
