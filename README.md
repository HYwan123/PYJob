# 招聘网站自动沟通脚本


![](image.png)
<p align="center">
  <a href="https://github.com/HYwan123/PYJob/stargazers"><img src="https://img.shields.io/github/stars/HYwan123/PYJob?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/HYwan123/PYJob/network/members"><img src="https://img.shields.io/github/forks/HYwan123/PYJob?style=social" alt="GitHub forks"></a>
  <br>
  <img src="https://img.shields.io/github/license/HYwan123/PYJob" alt="GitHub license">
  <img src="https://img.shields.io/github/repo-size/HYwan123/PYJob" alt="GitHub repo size">
  <img src="https://img.shields.io/github/last-commit/HYwan123/PYJob" alt="GitHub last commit">
  <img src="https://img.shields.io/github/issues/HYwan123/PYJob" alt="GitHub issues">
</p>

这是一个基于 Playwright 和 `rich` 构建的 Python 自动化脚本，旨在自动与招聘网站上的新职位进行"打招呼"，以提高求职效率。

## ✨ 功能特性

- **🤖 自动沟通**：脚本会自动浏览职位列表，并对每个职位发起沟通。
- **🍪 智能会话管理**：
    - 首次运行需要您手动扫码登录，脚本会自动保存您的登录状态（Cookies 等）到 `auth.json` 文件中。
    - 后续运行将自动加载 `auth.json`，跳过登录步骤，实现无缝自动化。
- **💅 精美的命令行界面**：
    - 使用 `rich` 库提供色彩丰富、信息清晰的控制台输出。
    - 通过美观的面板和状态提示，让您实时了解脚本的运行状况。
- **🔄 循环与健壮性**：
    - 脚本会无限循环执行，每轮操作后会暂停一段时间，以模拟正常用户行为。
    - 包含错误处理机制，即使页面结构发生细微变化（如弹窗未出现），脚本也能继续运行。
    - 支持优雅地中断（`Ctrl+C`），确保浏览器等资源被正确关闭。

## 📦 环境要求

- Python 3.7+

## ⚙️ 安装与设置

1.  **下载代码**
    将项目文件（`main.py`, `requirements.txt`）下载到您的本地文件夹。

2.  **安装依赖库**
    在您的终端或命令行工具中，进入项目所在的文件夹，然后运行以下命令来安装所有必需的 Python 库：
    ```bash
    pip install -r requirements.txt
    ```

3.  **安装 Playwright 浏览器驱动**
    Playwright 需要下载它专用的浏览器驱动才能工作。运行以下命令进行安装：
    ```bash
    playwright install
    ```

## 🚀 使用方法

1.  **运行脚本**
    在终端中执行以下命令：
    ```bash
    python main.py
    ```

2.  **首次登录**
    - 脚本第一次运行时，会检测到没有 `auth.json` 文件。
    - 它会自动打开一个浏览器窗口，并暂停执行。
    - 您需要在这个浏览器窗口中，通过**扫码**或**账号密码**的方式手动完成登录。
    - 登录成功后，在脚本暂停的终端或 Playwright Inspector 窗口中点击"Resume"（继续），脚本便会把您的登录信息保存到 `auth.json` 中，然后开始自动化流程。

3.  **后续运行**
    再次运行 `python main.py` 时，脚本会发现 `auth.json` 文件，自动加载您的登录状态，直接开始处理职位，无需您进行任何操作。

## 🔧 如何配置

如果您想更改求职的目标，例如修改城市、职位关键词或学历要求，可以直接修改 `main.py` 文件中第 27 行的 URL。

```python
# main.py - line 27
await page.goto("https://www.zhipin.com/web/geek/jobs?city=101020100&jobType=1902&degree=203&query=%E8%BF%90%E7%BB%B4")
```

URL 各参数的含义（以示例 URL 为例）：
- `city=101020100`: 城市代码（`101020100` 代表上海）。
- `jobType=1902`: 职位类型。
- `degree=203`: 学历要求（`203` 代表本科）。
- `query=%E8%BF%90%E7%BB%B4`: 职位关键词（`%E8%BF%90%E7%BB%B4` 是"运维"的 URL 编码）。

您可以直接在网站上筛选好您想要的条件，然后将浏览器地址栏中的整个 URL 复制过来替换即可。 