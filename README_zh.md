# RemNote Alfred 5 工作流

<p align="center">
  <img src="icon.png" width="128" height="128" alt="RemNote 图标">
</p>

<p align="center">
  <b>为 RemNote 桌面端打造的原生极速 Alfred 5 工作流，毫秒级本地直连。</b>
</p>

<p align="center">
  <a href="README.md">English</a> • <a href="README_zh.md">简体中文</a>
</p>

---

## 功能特性

- 🔍 **`rns <关键词>`**：即时全局搜索当前知识库中的所有笔记。按 `Enter` 键秒级呼出 RemNote 桌面客户端并跳转到该笔记。
- ⚡️ **`rn <内容>` / `rnc <内容>`**：闪念速记一键追加到今日 Daily Note 底部，并弹出 macOS 系统通知确认。
- 🕒 **`rnr`**：浏览与二次过滤最近 14 天内编辑过的文档列表。

---

## 如何获取 RemNote Token

本工作流通过 RemNote 桌面端内置的本地 MCP 服务（`http://127.0.0.1:7788/mcp`）进行通信。

1. 打开 **RemNote 桌面客户端**（必须为桌面端 App）。
2. 点击左下角的 **设置 ⚙️**（或按快捷键 `Cmd + ,`）。
3. 在左侧设置列表向下滚动，点击 **Developer**（或 **Integrations / Model Context Protocol**）。
4. 确保 **Local MCP Server** 处于开启状态。
5. 复制展示的 **Bearer Token**（以 `rn_mcp_...` 开头）。

---

## 安装与配置

### 第一步：下载并安装
直接下载仓库中的 [`RemNote.alfredworkflow`](RemNote.alfredworkflow) 并双击导入 Alfred 5。

### 第二步：配置环境变量
在导入时（或在 Alfred Preferences ➡️ Workflows ➡️ 选中 RemNote Companion ➡️ 点击右上角 `[x]` 按钮）：
1. **Local Server URL**：`http://127.0.0.1:7788/mcp`（默认保持不变）
2. **Bearer Token**：粘贴你的 `rn_mcp_...` 密钥。

---

## 快捷指令一览

| 触发词 | 功能说明 | 动作响应 |
| :--- | :--- | :--- |
| **`rns <关键词>`** | 搜索 RemNote 笔记 | 回车直接在客户端打开，`Cmd+C` 复制标题 |
| **`rn <内容>`** | 闪念速记到 Daily Note | 自动追加到今日 Daily Note 底部 |
| **`rnc <内容>`** | 闪念速记（同上） | 自动追加到今日 Daily Note 底部 |
| **`rnr`** | 最近编辑的笔记 | 列出最近 14 天的文档列表 |

---

## 开源协议

MIT License © 2026 [bianyeyu](https://github.com/bianyeyu)
