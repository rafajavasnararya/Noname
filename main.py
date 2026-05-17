
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import os
from flask import Flask
from threading import Thread

# Web server biar UptimeRobot bisa nge-ping
app = Flask('')

@app.route('/')
def home():
    return "Roblox 5 Account Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# ISI 5 AKUN DI SINI PAKAI SECRETS
ACCOUNTS = [
    {"user": os.getenv("USER1"), "pass": os.getenv("PASS1"), "game": os.getenv("GAME1")},
    {"user": os.getenv("USER2"), "pass": os.getenv("PASS2"), "game": os.getenv("GAME2")},
    {"user": os.getenv("USER3"), "pass": os.getenv("PASS3"), "game": os.getenv("GAME3")},
    {"user": os.getenv("USER4"), "pass": os.getenv("PASS4"), "game": os.getenv("GAME4")},
    {"user": os.getenv("USER5"), "pass": os.getenv("PASS5"), "game": os.getenv("GAME5")},
]

def run_account(account):
    if not account['user'] or not account['pass'] or not account['game']:
        print("Lewati akun kosong")
        return
    
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,720')
    
    driver = None
    try:
        print(f"[{account['user']}] Mulai login...")
        driver = uc.Chrome(options=options)
        driver.set_page_load_timeout(30)
        
        # Login
        driver.get("https://www.roblox.com/login")
        time.sleep(4)
        
        driver.find_element(By.ID, "login-username").send_keys(account['user'])
        driver.find_element(By.ID, "login-password").send_keys(account['pass'])
        driver.find_element(By.ID, "login-button").click()
        time.sleep(8)
        
        # Join game
        game_url = f"https://www.roblox.com/games/{account['game']}"
        driver.get(game_url)
        time.sleep(6)
        
        driver.find_element(By.CLASS_NAME, "btn-primary-md").click()
        print(f"[{account['user']}] Berhasil masuk game {account['game']}")
        
        # Anti AFK selama 12 menit per akun
        for i in range(12):
            time.sleep(60)
            try:
                webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
                print(f"[{account['user']}] Anti AFK {i+1}/12")
            except:
                print(f"[{account['user']}] Koneksi putus")
                break
                
    except Exception as e:
        print(f"[{account['user']}] Error: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"[{account['user']}] Selesai, ganti akun")

def main_loop():
    print("Bot dimulai. 5 akun akan jalan bergiliran")
    while True:
        for acc in ACCOUNTS:
            run_account(acc)
            time.sleep(15)  # jeda 15 detik sebelum ganti akun

if __name__ == "__main__":
    keep_alive()
    main_loop()
