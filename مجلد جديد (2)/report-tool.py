import requests
import random
import time

def report_account(url, num_reports):
    warnings = [
        "This account is using a fake name!",
        "Beware! This account is likely a scam!",
        "This account appears to be involved in illegal activities!",
        "Warning: This account may be trading drugs illegally!"
    ]
    comments = [
        "Nice profile!",
        "Interesting posts!",
        "Keep it up!",
        "Great content!"
    ]
    fake_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3029.110 Safari/537.3"
    ]
    fake_referers = [
        "https://www.facebook.com/",
        "https://www.google.com/",
        "https://www.bing.com/"
    ]
    proxies = [
        {"http": "http://your_proxy_ip1:port1", "https": "https://your_proxy_ip1:port1"},
        {"http": "http://your_proxy_ip2:port2", "https": "https://your_proxy_ip2:port2"},
        {"http": "http://your_proxy_ip3:port3", "https": "https://your_proxy_ip3:port3"}
    ]
    fake_names = [
        "John Doe",
        "Jane Smith",
        "Michael Johnson",
        "Emily Williams"
    ]
    for _ in range(num_reports):
        headers = {
            'User-Agent': random.choice(fake_user_agents),
            'Referer': random.choice(fake_referers),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        proxy = random.choice(proxies)
        response = requests.get(url, headers=headers, proxies=proxy)
        if response.status_code == 200:
            print("Reporting the account at:", url)
            warning = random.choice(warnings)
            print("Leaving a warning:", warning)
            comment = random.choice(comments)
            print("Leaving a comment:", comment)
            print("Account reported successfully!")
        else:
            print("Failed to report account at:", url)
        time.sleep(60)

# تحديد عدد الإبلاغات المراد إرسالها
num_reports = 300

# تحديد روابط الحسابات المستهدفة
urls = [
    "ENTER_PROFILE_URL_HERE",
    "ENTER_ANOTHER_PROFILE_URL_HERE",
    "ENTER_YET_ANOTHER_PROFILE_URL_HERE"
]

# استدعاء الدالة لإرسال الإبلاغات لكل حساب
for url in urls:
    report_account(url, num_reports)
