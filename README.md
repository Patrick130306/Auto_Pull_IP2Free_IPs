# IP2FREE Agent

Small Python helper that logs into IP2FREE, pulls the free proxy list, and writes a Clash-style YAML(`proxies.yaml`) to a folder named "proxy" on your desktop,it will auto-create a folde if there is not a folder named("proxy"). A few saved HTML pages (`login.html`, `tmp_login_after.html`, `dashboard.html`) and JS chunks are included as snapshots of the IP2FREE UI.

## Prerequisites
- Python 3.9+
- Install dependencies: `pip install -r requirements.txt`

## Configuration
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
