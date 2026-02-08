
# IP2FREE Agent

**选择语言 / Language / 語言**  
[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

---

<a id="english"></a>
## English

Small Python helper that logs into IP2FREE, pulls the free proxy list, and writes a Clash-style YAML(`proxies.yaml`) to a folder named "proxy" on your desktop,it will auto-create a folde if there is not a folder named("proxy"). A few saved HTML pages (`login.html`, `tmp_login_after.html`, `dashboard.html`) and JS chunks are included as snapshots of the IP2FREE UI.

### Prerequisites
- Python 3.9+
- Install dependencies: `pip install -r requirements.txt`

### Configuration
Set your IP2FREE account credentials via environment variables before running:

```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

### Usage
Run the agent; it will print where the YAML was written:

```powershell
python ip2free_agent.py
```

The file is placed in folder("proxy") and includes all available free proxies as a selectable group. The YAML contains the usernames and passwords returned by IP2FREE—treat it as a secret.

Example snippet:

```yaml
proxies:
  - name: "ip2free-US-New_York-123"
    type: socks5
    server: 203.0.113.10
    port: 1080
    username: user
    password: pass

proxy-groups:
  - name: "PROXY"
    type: select
    proxies:
      - "ip2free-US-New_York-123"
      - DIRECT
```

### Notes
- To fetch more or fewer pages, tweak the defaults in `_fetch_free_ips` inside `ip2free_agent.py`.

---

<a id="简体中文"></a>
## 简体中文

这是一个小型 Python 助手，用于登录 IP2FREE、拉取免费代理列表，并将 Clash 风格的 YAML 配置文件（`proxies.yaml`）写入桌面上的“proxy”文件夹中。如果不存在名为“proxy”的文件夹，它将自动创建。项目中包含一些保存的 HTML 页面（`login.html`、`tmp_login_after.html`、`dashboard.html`）和 JS 片段，作为 IP2FREE 界面的快照。

### 环境要求
- Python 3.9+
- 安装依赖：`pip install -r requirements.txt`

### 配置
在运行前通过环境变量设置你的 IP2FREE 账户凭据：

```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

### 使用方法
运行脚本，它将输出 YAML 文件的写入位置：

```powershell
python ip2free_agent.py
```

文件将保存在名为“proxy”的文件夹中，并包含所有可用的免费代理作为一个可选组。YAML 中包含 IP2FREE 返回的用户名和密码，请将其视为机密信息。

示例片段：

```yaml
proxies:
  - name: "ip2free-US-New_York-123"
    type: socks5
    server: 203.0.113.10
    port: 1080
    username: user
    password: pass

proxy-groups:
  - name: "PROXY"
    type: select
    proxies:
      - "ip2free-US-New_York-123"
      - DIRECT
```

### 注意事项
- 若要获取更多或更少的页面，请在 `ip2free_agent.py` 中的 `_fetch_free_ips` 函数中调整默认值。

---

<a id="繁體中文"></a>
## 繁體中文

這是一個小型 Python 助手，用於登入 IP2FREE、拉取免費代理列表，並將 Clash 風格的 YAML 配置文件（`proxies.yaml`）寫入桌面上的“proxy”資料夾中。如果不存在名為“proxy”的資料夾，它會自動創建。專案中包含一些儲存的 HTML 頁面（`login.html`、`tmp_login_after.html`、`dashboard.html`）和 JS 片段，作為 IP2FREE 介面的快照。

### 環境要求
- Python 3.9+
- 安裝依賴：`pip install -r requirements.txt`

### 配置
在執行前透過環境變數設定你的 IP2FREE 帳戶憑證：

```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

### 使用方法
執行腳本，它將輸出 YAML 檔案的寫入位置：

```powershell
python ip2free_agent.py
```

檔案將儲存在名為“proxy”的資料夾中，並包含所有可用的免費代理作為一個可選組。YAML 中包含 IP2FREE 返回的使用者名稱和密碼，請將其視為機密資訊。

示例片段：

```yaml
proxies:
  - name: "ip2free-US-New_York-123"
    type: socks5
    server: 203.0.113.10
    port: 1080
    username: user
    password: pass

proxy-groups:
  - name: "PROXY"
    type: select
    proxies:
      - "ip2free-US-New_York-123"
      - DIRECT
```

### 注意事項
- 若要獲取更多或更少的頁面，請在 `ip2free_agent.py` 中的 `_fetch_free_ips` 函式中調整預設值。

```
