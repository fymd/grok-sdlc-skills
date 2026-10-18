# 待办清单小程序（todo-miniprogram）

`grok-sdlc-skills` 端到端示例的**微信小程序版**，与 `examples/todo-cli`（Python CLI 版）对应同一需求。

## 功能
- 添加待办（输入框 + 添加按钮，支持回车提交）
- 点击条目切换完成 / 未完成
- 删除待办（条目右侧「删除」）
- 数据使用微信本地 `Storage` 持久化（key: `todos`），无需后端

## 目录结构
```
todo-miniprogram/
├── project.config.json      # 项目配置（appid 用 touristappid，无需账号即可本地编译）
├── sitemap.json
├── app.js / app.json / app.wxss
├── utils/store.js           # 待办读写封装（本地 Storage）
└── pages/index/             # 唯一页面：列表 + 添加 + 切换 + 删除
```

## 运行
1. 微信开发者工具 → 导入项目 → **目录必须精确到 `todo-miniprogram` 这一层**（即同时包含 `project.config.json` 和 `app.json` 的文件夹）。
   - ✅ 正确：`.../examples/todo-miniprogram`
   - ❌ 错误：`.../examples`（父目录，会报 `app.json: 在项目根目录未找到 app.json`）
2. 因为 appid 设为 `touristappid`，可直接以**测试号**模式本地预览，无需注册小程序账号。
3. 真机预览 / 上传发布需要替换为你自己的小程序 AppID，并登录开发者工具。

## 与 CLI 版的区别
| | todo-cli | todo-miniprogram |
|---|---|---|
| 形态 | 终端命令行 | 微信小程序（带 UI） |
| 运行环境 | Python + 标准库 | 微信开发者工具 / 微信 App |
| 持久化 | JSON 文件 | 微信本地 Storage |
| 用途 | 演示 SDLC 文本流程 | 演示 SDLC 在 UI 项目上的落地 |
