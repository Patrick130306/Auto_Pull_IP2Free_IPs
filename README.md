
# IP2FREE Agent

**选择语言 / Language / 語言**  
[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

---

<a id="english"></a>
## English

Python script that logs into IP2FREE, retrieves the free proxy list, and generates a Clash-compatible YAML configuration file (`proxies.yaml`). The script supports custom save paths via environment variables.

### Features
- Automatically logs into IP2FREE using your credentials
- Fetches all available free proxies (supports pagination)
- Generates a ready-to-use Clash configuration
- Supports custom save locations
- Handles errors gracefully with clear messages

### Prerequisites
- Python 3.9 or higher
- Required packages: `requests`

### Installation
```bash
pip install requests
```

Or create a `requirements.txt` file with:
```
requests>=2.28.0
```

Then install:
```bash
pip install -r requirements.txt
```

### Configuration

#### 1. Set Account Credentials
Set your IP2FREE account credentials as environment variables:

**Windows (PowerShell):**
```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

**Windows (Command Prompt):**
```cmd
set IP2FREE_EMAIL=your-email@example.com
set IP2FREE_PASSWORD=your-password
```

**Linux/Mac:**
```bash
export IP2FREE_EMAIL="your-email@example.com"
export IP2FREE_PASSWORD="your-password"
```

#### 2. Custom Save Path (Optional)
You can specify where to save the configuration file using the `IP2FREE_CONFIG_PATH` environment variable:

**Examples:**
```powershell
# Save to custom folder (absolute path)
$env:IP2FREE_CONFIG_PATH="C:\ProxyConfigs"

# Save to desktop subfolder (default if not set)
$env:IP2FREE_CONFIG_PATH="$HOME\Desktop\proxy"

# Save to current directory
$env:IP2FREE_CONFIG_PATH="."

# Save to relative path
$env:IP2FREE_CONFIG_PATH="./configs"

# Save to home directory
$env:IP2FREE_CONFIG_PATH="~/proxy-configs"
```

If `IP2FREE_CONFIG_PATH` is not set, the file will be saved to a folder named `proxy` on your desktop.

### Usage

Run the script:
```bash
python ip2free_agent.py
```

Output example:
```
开始获取IP2Free免费代理...
登录成功
获取到 150 个免费代理
使用默认保存路径: C:\Users\YourName\Desktop\proxy
配置文件已保存到: C:\Users\YourName\Desktop\proxy\proxies.yaml
操作完成！
```

### File Structure

The generated `proxies.yaml` file includes:
- All available free proxies as individual proxy entries
- A proxy group named "自动选择" (Auto Select) containing all proxies
- Basic Clash configuration with DNS settings
- Proxy authentication (username/password) as provided by IP2FREE

### Important Notes
1. **Security**: The generated YAML file contains proxy credentials. Keep it secure and don't share publicly.
2. **Proxy Limits**: Free proxies may have limitations on bandwidth or concurrent connections.
3. **API Changes**: If IP2FREE changes their API, the script may need updates.
4. **Customization**: To fetch more or fewer proxies, modify the `get_free_proxies()` method in the code.

### Troubleshooting

#### Login Failed
- Ensure your credentials are correct
- Check if your IP2FREE account is active
- Verify environment variables are properly set

#### No Proxies Retrieved
- IP2FREE may have no free proxies available at the moment
- Try running the script again later
- Check your internet connection

#### File Permission Issues
- Ensure you have write permissions to the target directory
- Try running as administrator/root if needed
- Specify a different directory using `IP2FREE_CONFIG_PATH`

---

<a id="简体中文"></a>
## 简体中文

Python脚本，用于登录IP2FREE、获取免费代理列表，并生成Clash兼容的YAML配置文件（`proxies.yaml`）。脚本支持通过环境变量自定义保存路径。

### 功能特点
- 使用您的凭据自动登录IP2FREE
- 获取所有可用的免费代理（支持分页）
- 生成即用型Clash配置文件
- 支持自定义保存位置
- 清晰的错误提示信息

### 环境要求
- Python 3.9 或更高版本
- 必需包：`requests`

### 安装
```bash
pip install requests
```

或创建包含以下内容的 `requirements.txt` 文件：
```
requests>=2.28.0
```

然后安装：
```bash
pip install -r requirements.txt
```

### 配置

#### 1. 设置账户凭据
将您的IP2FREE账户凭据设置为环境变量：

**Windows (PowerShell):**
```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

**Windows (命令提示符):**
```cmd
set IP2FREE_EMAIL=your-email@example.com
set IP2FREE_PASSWORD=your-password
```

**Linux/Mac:**
```bash
export IP2FREE_EMAIL="your-email@example.com"
export IP2FREE_PASSWORD="your-password"
```

#### 2. 自定义保存路径（可选）
您可以使用 `IP2FREE_CONFIG_PATH` 环境变量指定配置文件的保存位置：

**示例：**
```powershell
# 保存到自定义文件夹（绝对路径）
$env:IP2FREE_CONFIG_PATH="C:\ProxyConfigs"

# 保存到桌面子文件夹（默认设置，如果不设置此变量）
$env:IP2FREE_CONFIG_PATH="$HOME\Desktop\proxy"

# 保存到当前目录
$env:IP2FREE_CONFIG_PATH="."

# 保存到相对路径
$env:IP2FREE_CONFIG_PATH="./configs"

# 保存到用户主目录
$env:IP2FREE_CONFIG_PATH="~/proxy-configs"
```

如果未设置 `IP2FREE_CONFIG_PATH`，文件将默认保存到桌面上的 `proxy` 文件夹中。

### 使用方法

运行脚本：
```bash
python ip2free_agent.py
```

输出示例：
```
开始获取IP2Free免费代理...
登录成功
获取到 150 个免费代理
使用自定义保存路径: C:\ProxyConfigs
配置文件已保存到: C:\ProxyConfigs\proxies.yaml
操作完成！
```

### 文件结构

生成的 `proxies.yaml` 文件包含：
- 所有可用的免费代理作为单独的代理条目
- 名为"自动选择"的代理组，包含所有代理
- 基本的Clash配置和DNS设置
- IP2FREE提供的代理认证信息（用户名/密码）

### 重要提示
1. **安全性**：生成的YAML文件包含代理凭据。请妥善保管，不要公开分享。
2. **代理限制**：免费代理可能有带宽或并发连接限制。
3. **API变更**：如果IP2FREE更改其API，脚本可能需要更新。
4. **自定义**：要获取更多或更少的代理，请修改代码中的 `get_free_proxies()` 方法。

### 故障排除

#### 登录失败
- 确保凭据正确
- 检查您的IP2FREE账户是否有效
- 验证环境变量是否正确设置

#### 未获取到代理
- IP2FREE当前可能没有可用的免费代理
- 稍后再次尝试运行脚本
- 检查网络连接

#### 文件权限问题
- 确保对目标目录有写入权限
- 必要时以管理员/root权限运行
- 使用 `IP2FREE_CONFIG_PATH` 指定其他目录

---

<a id="繁體中文"></a>
## 繁體中文

Python腳本，用於登入IP2FREE、取得免費代理列表，並產生Clash相容的YAML配置文件（`proxies.yaml`）。腳本支援透過環境變數自定義保存路徑。

### 功能特點
- 使用您的憑證自動登入IP2FREE
- 取得所有可用的免費代理（支援分頁）
- 產生即用型Clash配置文件
- 支援自定義保存位置
- 清晰的錯誤提示訊息

### 環境要求
- Python 3.9 或更高版本
- 必要套件：`requests`

### 安裝
```bash
pip install requests
```

或建立包含以下內容的 `requirements.txt` 檔案：
```
requests>=2.28.0
```

然後安裝：
```bash
pip install -r requirements.txt
```

### 配置

#### 1. 設定帳戶憑證
將您的IP2FREE帳戶憑證設定為環境變數：

**Windows (PowerShell):**
```powershell
$env:IP2FREE_EMAIL="your-email@example.com"
$env:IP2FREE_PASSWORD="your-password"
```

**Windows (命令提示字元):**
```cmd
set IP2FREE_EMAIL=your-email@example.com
set IP2FREE_PASSWORD=your-password
```

**Linux/Mac:**
```bash
export IP2FREE_EMAIL="your-email@example.com"
export IP2FREE_PASSWORD="your-password"
```

#### 2. 自定義保存路徑（可選）
您可以使用 `IP2FREE_CONFIG_PATH` 環境變數指定配置檔案的保存位置：

**範例：**
```powershell
# 保存到自定義資料夾（絕對路徑）
$env:IP2FREE_CONFIG_PATH="C:\ProxyConfigs"

# 保存到桌面子資料夾（預設設定，如果不設定此變數）
$env:IP2FREE_CONFIG_PATH="$HOME\Desktop\proxy"

# 保存到目前目錄
$env:IP2FREE_CONFIG_PATH="."

# 保存到相對路徑
$env:IP2FREE_CONFIG_PATH="./configs"

# 保存到使用者主目錄
$env:IP2FREE_CONFIG_PATH="~/proxy-configs"
```

如果未設定 `IP2FREE_CONFIG_PATH`，檔案將預設保存到桌面上的 `proxy` 資料夾中。

### 使用方法

執行腳本：
```bash
python ip2free_agent.py
```

輸出範例：
```
開始獲取IP2Free免費代理...
登入成功
獲取到 150 個免費代理
使用自定義保存路徑: C:\ProxyConfigs
配置文件已保存到: C:\ProxyConfigs\proxies.yaml
操作完成！
```

### 檔案結構

產生的 `proxies.yaml` 檔案包含：
- 所有可用的免費代理作為獨立的代理條目
- 名為"自動選擇"的代理組，包含所有代理
- 基本的Clash配置和DNS設定
- IP2FREE提供的代理認證資訊（使用者名稱/密碼）

### 重要提示
1. **安全性**：產生的YAML檔案包含代理憑證。請妥善保管，不要公開分享。
2. **代理限制**：免費代理可能有頻寬或並行連線限制。
3. **API變更**：如果IP2FREE更改其API，腳本可能需要更新。
4. **自定義**：要取得更多或更少的代理，請修改程式碼中的 `get_free_proxies()` 方法。

### 故障排除

#### 登入失敗
- 確保憑證正確
- 檢查您的IP2FREE帳戶是否有效
- 驗證環境變數是否正確設定

#### 未取得代理
- IP2FREE當前可能沒有可用的免費代理
- 稍後再次嘗試執行腳本
- 檢查網路連線

#### 檔案權限問題
- 確保對目標目錄有寫入權限
- 必要時以管理員/root權限執行
- 使用 `IP2FREE_CONFIG_PATH` 指定其他目錄

---
### 版本更新
- **v1.0** - 初始版本
- **v1.1** - 新增自定義保存路徑功能
- **v1.2** - 改進錯誤處理和使用者提示

### 許可證
本項目僅供個人學習和研究使用，請遵守IP2FREE的服務條款。

### 免責聲明
本工具僅為技術展示用途。使用免費代理服務時請遵守當地法律法規。作者不對任何使用行為負責。
```
