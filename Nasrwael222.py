import threading
import time
import os
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

ls = []
file = 'nasr1.txt'

def read_file():
    """قراءة البروكسيات من الملف مع تنظيف الأسطر الفارغة والتعليقات وإزالة التكرار."""
    try:
        if not os.path.isfile(file):
            return []
        lines = []
        seen = set()
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            for raw in f.read().splitlines():
                line = raw.strip()
                if not line or line.startswith(("#", ";", "//")):
                    continue
                if line in seen:
                    continue
                seen.add(line)
                lines.append(line)
        return lines
    except FileNotFoundError:
        return []

def _normalize_proxy(line: str, default_scheme: str = "http") -> str:
   
    s = line.strip()

    if s.startswith(("http://", "https://", "socks5://", "socks4://")):
        return s

    s = s.replace(" ", "")

    if "@" in s and s.count(":") >= 2:
        return f"{default_scheme}://{s}"

    parts = s.split(":")
    if len(parts) == 2 and parts[1].isdigit():
        host, port = parts
        return f"{default_scheme}://{host}:{port}"

    if len(parts) == 4 and parts[3].isdigit():
        user, pwd, host, port = parts
        return f"{default_scheme}://{user}:{pwd}@{host}:{port}"

    if len(parts) == 4 and parts[1].isdigit():
        host, port, user, pwd = parts
        return f"{default_scheme}://{user}:{pwd}@{host}:{port}"

    return f"{default_scheme}://{s}"

def _to_requests_proxies(proxy_url: str) -> dict:
    """تهيئة dict مناسب لـ requests سواء http أو https أو socks."""
    return {"http": proxy_url, "https": proxy_url}

def _build_headers_minimal() -> dict:
    """
    هِدرز خفيفة بدون User-Agent حسب طلبك.
    تُبقي على accept-encoding واللغة والاتصال فقط.
    """
    return {
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "Accept-Language": "en-US,en;q=0.8,ar;q=0.7",
    }

def process_line(line: str):
    """
    تُرجع (proxies, headers) للاستخدام لاحقًا بدون أي طباعة.
    """
    proxy_url = _normalize_proxy(line, default_scheme="http")
    proxies = _to_requests_proxies(proxy_url)
    headers = _build_headers_minimal()  
    return proxies, headers

def process_lines(lines):
    results = []
    if not lines:
        return results
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_line, line) for line in lines]
        for future in as_completed(futures):
            results.append(future.result())
    return results

def update_file_loop():
    """
    حلقة تحديث مستمرة: تقرأ الملف كل 120 ثانية وتُجهّز النتائج للاستخدام لاحقًا.
    لا يوجد أي طباعة.
    """
    global ls
    while True:
        new_lines = read_file()
        ls = new_lines
        _ = process_lines(new_lines)
        time.sleep(120)

ls = read_file()
_ = process_lines(ls)

thread = threading.Thread(target=update_file_loop, daemon=True)
thread.start()
def afr(aweme_id,sessionid):
                    global tr,fa,er
                    proxies1=str(random.choice(ls))
                    _rticket = int(time.time() * 1000)
                    ts=str(int(time.time() * 1000))[:10]
                    from uuid import uuid4
                    uid=str(uuid4())
                    install_id = random.randrange(7334285683765348101, 7334285999999999999)
                    device_id=random.randrange(7283928371561793029, 7283929999999999999)
                    openudid = str(binascii.hexlify(os.urandom(8)).decode())
                    tz_name = random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', 'Asia/Kolkata', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Dubai', 'America/Sao_Paulo', 'Asia/Shanghai'])
                    webcast_language = random.choice(['en', 'es', 'fr', 'de', 'ja', 'pt', 'it', 'ru', 'ar', 'hi'])
                    current_region = random.choice(['US', 'UK', 'CA', 'AU', 'IN', 'BR', 'FR', 'DE', 'IT', 'ES','AB'])
                    region = random.choice(['US', 'UK', 'CA', 'AU', 'IN', 'BR', 'FR', 'DE', 'IT', 'ES'])
                    screen_height = random.randint(600,1080)
                    screen_width = random.randint(800,1920)
                    samsung = ["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"]
                    oppo =['CPH2359','CPH2457','CPH2349','CPH2145','CPH2293','CPH2343','CPH2127','CPH2197','CPH2173','CPH2371','CPH2269','CPH2005','CPH2185']
                    realme=['RMX3501','RMX3085','RMX1921','RMX3771','RMX3461','RMX3092','RMX3393','RMX3392','RMX1821','RMX1825','RMX3310',]
                    phone=random.choice([samsung,oppo,realme])
                    type1=random.choice(phone)
                    if 'SM' in type1 :
                         brand='samsung'
                         dev=type1.split('-')[1]
                    if 'RMX' in type1:
                         brand='realme'
                         dev=type1.split('X')[1]
                    if 'CPH' in type1:
                         brand='OPPO'
                         dev=type1.split('H')[1]

                    off=int(round((datetime.datetime.now() - datetime.datetime.utcnow()).total_seconds()))
                  
                    if aobsh == '1':
                         time1 = int(datetime.datetime.now().timestamp())
                         
                         reason=str(random.choice(sdsd))
                         pro1=urlencode({'WebIdLastTime': time1,
'aid': '1988', 
'legal_jurisdiction': 'de',
'relevant_law': 'Betrug, Täuschung oder Manipulation mit Kryptowährungen sind verboten.Jeder Versuch von Scam oder Fake-Investments wird nach §263 StGB (Betrug) und EU-Recht strafrechtlich verfolgt.', 
'report_desc':'Betrug, Täuschung oder Manipulation mit Kryptowährungen sind verboten.Jeder Versuch von Scam oder Fake-Investments wird nach §263 StGB (Betrug) und EU-Recht strafrechtlich verfolgt.',  
'report_signature': 'semo', 
'logout_reporter_email': 'Semo@gmail.com',
'nickname':  nickname,
'object_id': aweme_id,
'object_owner_id':id, 
'odinId': 'odinId', 
'owner_id':  id, 
'reason': reason,
'report_type': 'video',
'reporter_id': 'didd',
'target': aweme_id,
'video_id': aweme_id, 
'language':webcast_language,
'openudid':openudid,
'current_region':current_region,
'screen_height': screen_height,
'screen_width': screen_width,
'_rticket':_rticket,
'device_type':type1,
'device_brand':brand,
'screen_width': screen_width,
'lang': webcast_language,
'video_owner': '[object Object]', 
'msToken': 'bBnmc3bGnJnwRNRl8ub8FpnMoe_FBOO5iSegKwmcoS7t8ccpDBGMGhBv56gcZ03OJ0hiRloHWlZ9GMsmQn6jS4GfZ7qqjwz_M50f42ZBBuGtR20Pr4CesyFZATf1h-hZ8X1H2xkJENqK-8c=',

'X-Bogus': 'DFSzswVLHzGANe5ECPlOvQVRr3Nx', 
'X-Gnarly':' MwZNYM9kQNZZ9OBmZLTeU94uJuKkFoO-R9DP2xCfOYTjJGUmeqpSjxvH5dDrGI76fbwLNuZKXZHDZTtmDilleAjwA-yuU0yA77zprIgR1XZdXCRN2-VntJbDtFk6VVtQpm9p9rO-rEi4r23ncc5CBBRAfIoQzX3q3gSKM/hrszZggM7AjpljA3rnm535T3K7V/t/xXt/VzGoL9eIifyJW5zhfXYvXOueaHqeR/31CVcFOQ7dhhHkJGc1tqWU5aWZK-THEml0dLVuwmY33Hyb-0dnViiMFF22GTzY8fVYqslN',

                              '_signature': '_02B4Z6wo00001qvYUFwAAIDArHJl-y89yw6r2FTAAMyOac',})



                         url='https://www.tiktok.com/aweme/v2/aweme/feedback/?%s'%(pro1)

                         h={

                              'Cookie': f'ttwid=; sid_tt='+sessionid+'; sessionid='+sessionid+'; sessionid_ss='+sessionid+';',

                              'Referer': 'https://www.tiktok.com/@'+g+'/video/'+aweme_id,

                              'Sec-Fetch-Site': 'same-origin',

                              'User-Agent': 'com.zhiliaoapp.musically/2024306030 (Linux; U; Android 13; en_US; SM-G998U Build/TP1A.220624.014;tt-ok/3.12.13.4-tiktok)',}

                         
                    #Other
                    if aobsh == '2':
                         if xxx == '14': # type: ignore
                              pro=urlencode({
                              
                              'cdid':uid})
                              
                         #Harassment and bullying
                         else:
                              pro=urlencode({
                             
                              'cdid':uid})
                         u='https://api22-normal-c-useast1a.tiktokv.com/aweme/v2/aweme/feedback/?'
                         url = u+pro
                         payload = f''
                         signed = ttsign(url.split('?')[1], payload, None).get_value()
                         x_gorgon=signed['x-gorgon']
                         x_khronos=signed['x-khronos']
                         xss=signed['x-ss-req-ticket']
                         
                         h={
                         'Cookie':
                         f'sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid};',
                        
                         'User-Agent' :f'com.zhiliaoapp.musically/2024306030 (Linux; U; Android 13; en_US; SM-G998U Build/TP1A.220624.014;tt-ok/3.12.13.4-tiktok)',#SM-G955N
     
                         'X-Gorgon':x_gorgon,
                         'X-Khronos':x_khronos,
                         'X-SS-REQ-TICKET':xss,
                    }
                    try:
                         r=requests.get(url,headers=h,proxies={'https': f'socks5://{str(random.choice(ls))}','https': f'socks4://{str(random.choice(ls))}','https': f'http://{str(random.choice(ls))}'}).text
                         tr+=1
                         if aweme_id in soso:
                              pass
                         else:
                              soso.append(aweme_id)
                         if sessionid in loop:
                              pass
                         else:
                              loop.append(sessionid)
                         bi = random.choice([F,J,Z,C,B,L,J1,J2,J21,J22,F1,C1,P1])
                    except:
                         fa +=1
                         #bi = random.choice([F,J,Z,C,B,L,J1,J2,J21,J22,F1,C1,P1])
          

# -*- coding: utf-8 -*-
"""
TikTok AFR Tool (silent global HUD)
- توزيع الـ IDs على كل السيشنات بالتساوي (round-robin).
- تشغيل متوازي لكل السيشنات.
- عداد HUD واحد فقط عالمي (IDs / OK / FAIL / PROGRESS / SESS count).
- بدون LIVE STATUS
- بدون إظهار أسماء السيشنات
- بدون بانر
"""

# -*- coding: utf-8 -*-
"""
NASR • High-Performance (Safe) HUD + Rate-Limited Workers
- Single-file (no external config)
- Reuse requests.Session per worker (keep-alive, connection pool)
- Global token-bucket RPS limiter (safe cap)
- Exponential backoff on failures
- Measures RTT, reports P50/P90
- Pulse Gradient HUD (Green->Cyan->Magenta)
- OK/BAD counted once per ID
- Compatible with Pydroid3 (Android)
"""
