# todo-miniprogram 上线指南（Launch Guide）

本目录是一个微信小程序。从「本地跑通」到「正式上线」需经过：
**本地验证 → 换真实 AppID → 开发者工具上传 → 公众平台提交审核 → 审核通过后发布**。

> ⚠️ 「上传 / 提交审核 / 发布」涉及你自己的微信小程序账号与微信官方审核，
> 必须在「微信开发者工具 + mp.weixin.qq.com」由你本人完成；代码侧准备本仓库已就绪。

## 1. 本地验证（现在就能跑）
- 逻辑单测：`node tests/store.test.js`（10 个用例，零依赖，应全绿）
- 编译预览：开发者工具导入本目录，`appid=touristappid` 可用**测试号**模式本地预览

## 2. 换真实 AppID（上线必做）
`touristappid` 只能本地预览，**不能上传/发布**。上线前：
1. 到 https://mp.weixin.qq.com 注册小程序，拿到 AppID（形如 `wxXXXXXXXXXXXXXXXX`）。
2. 编辑 `project.config.json`，把 `"appid": "touristappid"` 改成你的 AppID。
3. 在开发者工具登录该账号（扫码）。

## 3. 上传代码
方式 A — 命令行（需先开启服务端口）：
1. 开发者工具 →「设置 → 安全设置」→ 打开「服务端口（Service Port）」，可顺手复制 CLI 访问令牌。
2. 设了令牌就带 `--token <令牌>`，或设环境变量 `WECHAT_DEVTOOLS_CLI_TOKEN`；也可用 `--port <端口>` 指定 IDE HTTP 端口。
3. 上传（需已在开发者工具里扫码登录微信）：
   ```bash
   cli.bat upload --project <todo-miniprogram 绝对路径> -v 1.0.0 -d "待办清单首个版本"
   ```
   `cli.bat` 在开发者工具安装目录，例如
   `C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat`；
   参数以 `cli.bat upload --help` 为准（`-v` 版本号、`-d` 备注均必填）。

> 说明：不开服务端口直接跑 upload 会报
> `IDE service port disabled ... set Service Port On`，这是 IDE 安全门，需 GUI 手动开一次。

方式 B — 图形界面：开发者工具右上角「上传」→ 填版本号 + 备注 → 确认。

## 4. 提交审核（mp.weixin.qq.com）
公众平台 → 版本管理 → 开发版本 → 选刚上传的版本 → 设为体验版/提交审核 →
填服务类目、标签。本示例数据仅存**本地 Storage、不采集用户信息**，隐私声明从简。

## 5. 发布
审核通过后 → 版本管理 → 审核版本 → 发布。发布后即可被搜索/扫码访问。

## 6. 版本管理建议
- 每次上传递增版本号（`-v 1.0.0 / 1.1.0 ...`），与仓库 `CHANGELOG.md` 对齐。
- 上传前先跑 `node tests/store.test.js` 确认全绿。

## 已知限制
- `touristappid`（测试号）仅供本地预览，**不能上传**：实测上传被微信后端驳回
  （`code 10: 不存在此 AppID 请检查后重新输入`）。上传 / 发布必须用真实注册的 AppID。
- 真机预览、云开发、微信登录等需真实 AppID 并在公众平台配置。
