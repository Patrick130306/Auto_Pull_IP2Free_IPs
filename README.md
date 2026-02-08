# IP2FREE Agent

## 🌐 Language / 语言选择
- [English](#english)
- [简体中文](#简体中文)
- [繁体中文](#繁體中文)

---

## English
### IP2FREE Agent
Small Python helper that logs into IP2FREE, pulls the free proxy list, and writes a Clash-style YAML(`proxies.yaml`) to a folder named "proxy" on your desktop. It will auto-create the folder if it does not exist. A few saved HTML pages (`login.html`, `tmp_login_after.html`, `dashboard.html`) and JS chunks are included as snapshots of the IP2FREE UI.

### Prerequisites
- Python 3.9+
- Install dependencies: `pip install -r requirements.txt`

### Configuration
Set your IP2FREE account credentials via environment variables before running:
```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

## Usage
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

## Notes
- To fetch more or fewer pages, tweak the defaults in `_fetch_free_ips` inside `ip2free_agent.py`.

- ##简体中文
  ###IP2FREE Agent
一个轻量的 Python 工具，可登录 IP2FREE 平台、拉取免费代理列表，并将 Clash 格式的 YAML 文件（proxies.yaml）写入桌面名为 "proxy" 的文件夹（若该文件夹不存在则自动创建）。工具中包含了几个保存的 HTML 页面（login.html、tmp_login_after.html、dashboard.html）和 JS 片段，作为 IP2FREE 界面的快照。
    ##前置条件
 - Python 3.9 及以上版本
 - 安装依赖：pip install -r requirements.txt
   ##配置
运行前，请通过环境变量设置你的 IP2FREE 账号凭证：
```powershell
$env:IP2FREE_EMAIL="你的邮箱@示例.com"
$env:IP2FREE_PASSWORD="你的密码"
```
  ##使用方法
运行该工具，控制台会打印 YAML 文件的写入路径：
```powershell
python ip2free_agent.py
```
文件会被放置在 "proxy" 文件夹中，包含所有可用的免费代理（作为可选择的分组）。YAML 文件中包含 IP2FREE 返回的用户名和密码 —— 请将其视为敏感信息。
示例片段：
yaml
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
注意事项
如需拉取更多 / 更少页面的代理，可修改 ip2free_agent.py 文件中 _fetch_free_ips 函数的默认参数。
