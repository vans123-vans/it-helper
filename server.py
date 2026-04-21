

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import webbrowser
import os

PORT = 6225

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

def get_local_ip():
    import socket
    try:
        # 创建一个UDP套接字，连接到一个公共DNS服务器
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return '127.0.0.1'

def main():
    local_ip = get_local_ip()
    print(f"启动服务器，端口: {PORT}")
    print(f"本地访问地址: http://localhost:{PORT}")
    print(f"内网访问地址: http://{local_ip}:{PORT}")
    
    # 自动打开浏览器
    webbrowser.open(f'http://localhost:{PORT}')
    
    # 监听所有网络接口
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print("服务器运行中...")
        print("按 Ctrl+C 停止服务器")
        httpd.serve_forever()

if __name__ == "__main__":
    main()