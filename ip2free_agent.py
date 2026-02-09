import datetime
import json
import os
from pathlib import Path

import requests

# 配置信息
API_URL = "https://api.ip2free.com"
HEADERS = {
    "webname": "IP2FREE",
    "domain": "www.ip2free.com",
    "lang": "cn",
    "referer": "https://www.ip2free.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "content-type": "text/plain;charset=UTF-8",
}


class IP2FreeClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.token = None
        
    def check_credentials(self):
        """检查登录信息"""
        email = os.environ.get("IP2FREE_EMAIL")
        password = os.environ.get("IP2FREE_PASSWORD")
        if not email or not password:
            raise Exception("请先设置IP2FREE_EMAIL和IP2FREE_PASSWORD环境变量")
        return email, password
    
    def login(self):
        """登录获取token"""
        email, password = self.check_credentials()
        
        data = {
            "email": email,
            "password": password
        }
        
        response = self.session.post(
            f"{API_URL}/api/account/login",
            data=json.dumps(data),
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        self.token = result.get("data", {}).get("token") or self.session.cookies.get("Mall-Token")
        
        if not self.token:
            raise Exception("登录失败，未获取到token")
            
        self.session.headers["x-token"] = self.token
        self.session.cookies.set("Mall-Token", self.token, domain="www.ip2free.com", path="/")
        
        print("登录成功")
        return True
    
    def get_free_proxies(self):
        """获取免费代理列表"""
        if not self.token:
            self.login()
        
        all_proxies = []
        page = 1
        
        while True:
            data = {
                "keyword": "",
                "country": "",
                "city": "",
                "page": page,
                "page_size": 100
            }
            
            response = self.session.post(
                f"{API_URL}/api/ip/freeList",
                data=json.dumps(data),
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            proxy_list = result.get("data", {}).get("free_ip_list", [])
            
            if not proxy_list:
                break
                
            all_proxies.extend(proxy_list)
            
            # 如果获取的数量少于page_size，说明没有更多数据了
            if len(proxy_list) < 100:
                break
                
            page += 1
            
            # 最多获取10页，避免无限循环
            if page > 10:
                break
        
        if not all_proxies:
            raise Exception("没有获取到可用的免费代理")
            
        print(f"获取到 {len(all_proxies)} 个免费代理")
        return all_proxies
    
    def create_clash_config(self, proxies):
        """生成Clash配置文件"""
        
        # 代理节点部分
        proxy_configs = []
        proxy_names = []
        
        for proxy in proxies:
            country = proxy.get("country_code", "XX")
            city = proxy.get("city", "unknown").replace(" ", "_")
            proxy_id = proxy.get("id", "free")
            
            name = f"ip2free_{country}_{city}_{proxy_id}"
            
            proxy_config = f"""  - name: "{name}"
    type: {proxy.get("protocol", "socks5")}
    server: {proxy.get("ip", "")}
    port: {proxy.get("port", 0)}
    username: {proxy.get("username", "")}
    password: {proxy.get("password", "")}
"""
            proxy_configs.append(proxy_config)
            proxy_names.append(name)
        
        # 代理组配置
        proxy_group = f"""proxy-groups:
  - name: "自动选择"
    type: select
    proxies:
"""
        for name in proxy_names:
            proxy_group += f"      - \"{name}\"\n"
        proxy_group += "      - DIRECT\n"
        
        # 完整配置
        config = f"""port: 7890
socks-port: 7891
mode: rule
allow-lan: false
log-level: info

proxies:
{''.join(proxy_configs)}
{proxy_group}
rules:
  - MATCH,自动选择

dns:
  enabled: true
  listen: 0.0.0.0:1053
  default-nameserver:
    - 1.1.1.1
    - 8.8.8.8
  nameserver:
    - 1.1.1.1
    - 8.8.8.8
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  use-hosts: true
"""
        
        return config
    
    def save_config(self, config):
        """保存配置文件"""
        desktop = Path.home() / "Desktop"
        proxy_dir = desktop / "proxy"
        proxy_dir.mkdir(exist_ok=True)
        
        config_file = proxy_dir / "proxies.yaml"
        config_file.write_text(config, encoding="utf-8")
        
        print(f"配置文件已保存到: {config_file}")
        return config_file


def main():
    """主函数"""
    try:
        print("开始获取IP2Free免费代理...")
        
        # 创建客户端
        client = IP2FreeClient()
        
        # 登录
        client.login()
        
        # 获取代理列表
        proxies = client.get_free_proxies()
        
        # 生成配置文件
        config = client.create_clash_config(proxies)
        
        # 保存文件
        client.save_config(config)
        
        print("操作完成！")
        
    except Exception as e:
        print(f"出错了: {e}")
        return False
    
    return True


if __name__ == "__main__":
    main()
