import time  # إضافة مكتبة الوقت في الأعلى

if aobsh == '1':
          try:

               h3={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}

               ttwid=requests.head('https://www.tiktok.com/',headers=h3).cookies.get_dict()['ttwid']
          except requests.exceptions.ConnectionError:
               print("يرجا التاكد من النت واعد المحاوله مره اخره");exit()
          except:print("يرجا المحاوله مره اخره");exit()
          

                    
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

import os, re, sys, time, math, random, threading, traceback
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from collections import deque

# ------------------ SETTINGS (tweak safely) ------------------
# Safety-first: don't set RPS_TOTAL extremely high.
RPS_TOTAL = 10.0              # إجمالي الطلبات/ثانية (جميع الخيوط مجتمعة)
MAX_RETRY_PER_ID = 2          # محاولات لكل ID
BACKOFF_BASE = 0.25           # ثواني (exponential backoff base)
BACKOFF_MAX = 6.0             # أقصى انتظار بين المحاولات
REQUEST_TIMEOUT = 10.0        # timeout لكل طلب (ثواني)
SESSION_POOL_SIZE = 6         # pool_maxsize per Session adapter
FORCE_COLOR = True            # ألوان في أندرويد، اجعل False لإيقافها

# HUD / bar
BAR_WIDTH = 30
BLOCKS_PER_GAP = 5
BAR_GRADIENT = []  # set below after colors

# Files (same folder)
try: BASE = os.path.dirname(os.path.abspath(__file__))
except: BASE = os.getcwd()
PRIMARY_FILE = os.path.join(BASE, "3.txr")
FALLBACK_FILE = os.path.join(BASE, "3.txt")
SESSIONS_FILE = os.path.join(BASE, "1.txt")
PROXIES_FILE  = os.path.join(BASE, "nasr1.txt")

# Thread caps (conservative safe defaults)
ANDROID_THREADS_CAP = 4
DESKTOP_THREADS_CAP = 24
MAX_WORKERS = None  # None => auto

# ------------------ ENV / COLORS ------------------
def _is_android_env():
    try:
        if "ANDROID_ROOT" in os.environ: return True
        exe = (sys.executable or "").lower()
        if "pydroid" in exe or "android" in exe: return True
        for k in os.environ.keys():
            if "PYDROID" in k or "TERMUX" in k: return True
    except: pass
    return False

IS_ANDROID = _is_android_env()

def _supports_ansi():
    if IS_ANDROID: return False
    return sys.stdout.isatty()

ANSI_OK = FORCE_COLOR or _supports_ansi()

RESET = "\033[0m" if ANSI_OK else ""
BOLD  = "\033[1m" if ANSI_OK else ""
DIM   = "\033[2m" if ANSI_OK else ""
RED   = "\033[91m" if ANSI_OK else ""
GRN   = "\033[92m" if ANSI_OK else ""
YLW   = "\033[93m" if ANSI_OK else ""
BLU   = "\033[94m" if ANSI_OK else ""
MAG   = "\033[95m" if ANSI_OK else ""
CYN   = "\033[96m" if ANSI_OK else ""
WHT   = "\033[97m" if ANSI_OK else ""
BAR_GRADIENT = [GRN, CYN, MAG]

CLR_OK = GRN; CLR_BAD = RED; CLR_NUM = CYN
EMO_OK = "OK"; EMO_BAD = "BAD"

HUD_MIN_INTERVAL = 0.2 if IS_ANDROID else 0.08

# ------------------ Utilities: file loading ------------------
def pick_id_file():
    path = PRIMARY_FILE if os.path.isfile(PRIMARY_FILE) else FALLBACK_FILE
    return path if os.path.isfile(path) else None

def _extract_ids_from_text_file(path):
    ids, seen = [], set()
    with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
        for line in f:
            s = line.strip()
            if not s: continue
            m = re.search(r'(\d{8,})', s)
            v = m.group(1) if m else s
            if v not in seen:
                seen.add(v); ids.append(v)
    return ids

def load_ids_once():
    p = pick_id_file()
    if not p: return []
    try: return _extract_ids_from_text_file(p)
    except: return []

def load_sessions():
    if not os.path.isfile(SESSIONS_FILE): return []
    with open(SESSIONS_FILE, "r", encoding="utf-8-sig", errors="ignore") as f:
        return [s.strip() for s in f if s.strip()]

def load_proxies():
    if not os.path.isfile(PROXIES_FILE): return []
    with open(PROXIES_FILE, "r", encoding="utf-8-sig", errors="ignore") as f:
        items, seen = [], set()
        for line in f:
            s = line.strip()
            if not s or s.startswith("#") or s in seen: continue
            seen.add(s); items.append(s if s.startswith(("http://","https://")) else "http://"+s)
    return items

# ------------------ Rate Limiter (Token Bucket) ------------------
class TokenBucket:
    def __init__(self, rate_per_sec):
        self.rate = float(rate_per_sec)
        self.tokens = float(rate_per_sec)
        self.capacity = float(max(1.0, rate_per_sec))
        self.last = time.time()
        self.lock = threading.Lock()

    def consume(self, amount=1.0, block=True, timeout=5.0):
        """حاول استهلاك توكن، اعد True لو نجحت"""
        deadline = time.time() + timeout if block else None
        while True:
            with self.lock:
                now = time.time()
                elapsed = now - self.last
                if elapsed > 0:
                    self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
                    self.last = now
                if self.tokens >= amount:
                    self.tokens -= amount
                    return True
            if not block:
                return False
            if time.time() >= (deadline or 0):
                return False
            time.sleep(0.01)

# ------------------ Global status & HUD ------------------
class GlobalStatus:
    def __init__(self, total_ids, total_sessions):
        self.lock = threading.Lock()
        self.total_ids = total_ids
        self.total_sessions = total_sessions
        self.done_unique_ids = set()
        self.ok_total = 0
        self.fail_total = 0
        self.sessions_used = set()
        # RTT samples for histogram (deque to bound memory)
        self.rtts = deque(maxlen=2000)

    def update(self, sessionid, aweme_id, success, rtt_ms=None):
        with self.lock:
            self.sessions_used.add(sessionid)
            if aweme_id not in self.done_unique_ids:
                self.done_unique_ids.add(aweme_id)
                if success: self.ok_total += 1
                else:       self.fail_total += 1
            if rtt_ms is not None:
                self.rtts.append(rtt_ms)

    def snapshot(self):
        with self.lock:
            return {
                "done_count": len(self.done_unique_ids),
                "total_ids": self.total_ids if self.total_ids>0 else 1,
                "ok_total": self.ok_total,
                "fail_total": self.fail_total,
                "used_sessions": len(self.sessions_used),
                "total_sessions": self.total_sessions if self.total_sessions>0 else 1,
                "rtts": list(self.rtts)
            }

GLOBAL_STATUS = None
_PREV_HUD_TS = 0.0
_HUD_LOCK = threading.Lock()

def _strip_ansi(s): return re.sub(r'\033\[[0-9;]*m','',s)

def _truncate_visible(text, length):
    vis_len = len(_strip_ansi(text))
    if vis_len <= length: return text
    raw = list(text); vis=0; out=[]; i=0
    while i<len(raw):
        ch = raw[i]; out.append(ch)
        if ch == "\033":
            i+=1
            while i < len(raw):
                out.append(raw[i])
                if raw[i] == "m":
                    i+=1; break
                i+=1
            continue
        else:
            vis += 1
            if vis >= length: break
            i+=1
    return "".join(out)

def _color_for_pct(p):
    if p < 40: return RED
    elif p < 80: return YLW
    else: return GRN

def _gradient_color(index, total_fill):
    if not BAR_GRADIENT or total_fill <= 0: return GRN
    seg_count = len(BAR_GRADIENT)
    seg_len = max(1, total_fill // seg_count)
    idx = min(seg_count-1, index // seg_len)
    return BAR_GRADIENT[idx]

def _make_bar(done, total, width=BAR_WIDTH):
    if total <= 0: total = 1
    ratio = done / float(total)
    pct = ratio * 100.0
    fill = int(width * ratio)
    left = width - fill
    if not ANSI_OK:
        blocks = []
        for i in range(fill):
            blocks.append("#")
            if (i+1) % BLOCKS_PER_GAP == 0 and (i+1) < fill: blocks.append(" ")
        return "".join(blocks) + "-"*left, pct
    ch_full = "█"; ch_empty = "░"
    segs = []
    t = time.time()
    for i in range(fill):
        col = _gradient_color(i, fill)
        phase = ((t*2.0) + (i / float(max(1, fill)))) % 1.0
        bright = (phase < 0.22)
        segs.append(f"{(BOLD if bright else '')}{col}{ch_full}{RESET}")
        if (i+1) % BLOCKS_PER_GAP == 0 and (i+1) < fill: segs.append(" ")
    segs.append(f"{DIM}{ch_empty*left}{RESET}")
    return "".join(segs), pct

def _pct_badge(pct):
    if not ANSI_OK: return f"{int(round(pct))}%"
    color = _color_for_pct(pct)
    return f"{BOLD}{color}{int(round(pct))}%{RESET}"

def _summary_rtt(rtts):
    if not rtts: return "P50 N/A"
    arr = sorted(rtts)
    n = len(arr)
    p50 = arr[int(0.5*(n-1))]
    p90 = arr[int(0.9*(n-1))]
    return f"P50 {p50:.0f}ms P90 {p90:.0f}ms"

def print_status_compact(bucket: TokenBucket):
    global _PREV_HUD_TS
    snap = GLOBAL_STATUS.snapshot()
    done_ids = snap["done_count"]; total_ids = snap["total_ids"]
    ok_total = snap["ok_total"]; fail_total = snap["fail_total"]
    used = snap["used_sessions"]; total_sess = snap["total_sessions"]
    rtt_summary = _summary_rtt(snap["rtts"])
    bar_txt, pct = _make_bar(done_ids, total_ids)
    badge = _pct_badge(pct)
    stats = (f"{BOLD}{CLR_NUM}IDs{RESET} {done_ids}/{total_ids}  "
             f"{EMO_OK} {CLR_OK}{ok_total}{RESET}  "
             f"{EMO_BAD} {CLR_BAD}{fail_total}{RESET}  "
             f"SESS {CLR_NUM}{used}{RESET}/{CLR_NUM}{total_sess}{RESET}  "
             f"{DIM}{rtt_summary}{RESET}")
    line_prog = f"{BOLD}{MAG}PROGRESS{RESET} [{bar_txt}] {badge}  {DIM}RPScap={bucket.rate:.1f}{RESET}"
    now = time.time()
    if now - _PREV_HUD_TS < HUD_MIN_INTERVAL: return
    _PREV_HUD_TS = now
    with _HUD_LOCK:
        print(_truncate_visible(stats, 140))
        print(_truncate_visible(line_prog, 140))

# ------------------ HTTP Session factory (per worker) ------------------
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def make_worker_session(proxy_url=None):
    s = requests.Session()
    # Retry on connection-level errors (not for logic-level failures)
    retry = Retry(total=0, connect=0, read=0, status=0)
    adapter = HTTPAdapter(pool_connections=SESSION_POOL_SIZE, pool_maxsize=SESSION_POOL_SIZE, max_retries=retry)
    s.mount('http://', adapter)
    s.mount('https://', adapter)
    # apply proxy if provided (string)
    if proxy_url:
        s.proxies.update({"http": proxy_url, "https": proxy_url})
    # small default headers to keep sessions consistent
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; NASR/1.0)",
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
    })
    return s

# ------------------ AFR wrapper (user must provide afr_impl) ------------------
# afr_impl should accept (aweme_id, sessionid, session=requests.Session()) and return True/False (or None)
# We'll call afr_impl with worker session to reuse connections.
def afr_call_via_session(afr_impl, aweme_id, sessionid, sess: requests.Session):
    """
    Must return (ok_bool, rtt_ms)
    afr_impl may either:
      - return True/False (sync), or
      - raise exception on network error
    """
    start = time.time()
    try:
        # If afr_impl supports session param, pass it
        try:
            res = afr_impl(aweme_id, sessionid, session=sess, timeout=REQUEST_TIMEOUT)
        except TypeError:
            # fallback: call without session
            res = afr_impl(aweme_id, sessionid)
        ok = (res is True) or (res is None)
    except Exception:
        traceback.print_exc(limit=1, file=sys.stderr)
        ok = False
    rtt = (time.time() - start) * 1000.0
    return ok, rtt

# ------------------ Worker logic ------------------
def worker_session_fn(sessionid, aweme_ids, proxy_rotator, token_bucket: TokenBucket, afr_impl):
    """
    Each worker uses a dedicated requests.Session for keep-alive + pooling.
    TokenBucket controls RPS globally.
    """
    if not aweme_ids: return (0,0,0)
    # create session for this worker (with optional proxy)
    proxy = proxy_rotator.next() if proxy_rotator else None
    sess = make_worker_session(proxy)
    ok_cnt = 0; fail_cnt = 0; calls = 0

    for aweme_id in aweme_ids:
        # Acquire token (blocks short time if needed)
        got = token_bucket.consume(1.0, block=True, timeout=5.0)
        if not got:
            # couldn't get slot, wait small then continue
            time.sleep(0.1)
        # Try up to MAX_RETRY_PER_ID with exponential backoff
        success = False
        backoff = BACKOFF_BASE
        for attempt in range(1, MAX_RETRY_PER_ID+1):
            calls += 1
            ok, rtt = afr_call_via_session(afr_impl, aweme_id, sessionid, sess)
            GLOBAL_STATUS.update(sessionid, aweme_id, ok, rtt_ms=rtt)
            if ok:
                success = True
                break
            else:
                # backoff before retry (jittered)
                to_sleep = min(BACKOFF_MAX, backoff * (1 + random.uniform(0,0.25)))
                time.sleep(to_sleep)
                backoff *= 2.0
        if success: ok_cnt += 1
        else: fail_cnt += 1
        print_status_compact(token_bucket)
    try: sess.close()
    except: pass
    return (ok_cnt, fail_cnt, calls)

def distribute_ids_round_robin(all_ids, sessions):
    buckets = {sid: [] for sid in sessions}
    if not sessions: return buckets
    idx = 0
    for aw in all_ids:
        sid = sessions[idx % len(sessions)]
        buckets[sid].append(aw)
        idx += 1
    return buckets

def _compute_workers(n_sessions):
    if n_sessions <= 0: return 1
    cap = ANDROID_THREADS_CAP if IS_ANDROID else DESKTOP_THREADS_CAP
    if MAX_WORKERS and MAX_WORKERS>0: cap = min(cap, MAX_WORKERS)
    return min(n_sessions, cap)

def run_cycle(sessions, ids, proxies, afr_impl):
    global GLOBAL_STATUS
    GLOBAL_STATUS = GlobalStatus(total_ids=len(ids), total_sessions=len(sessions))
    # token bucket rate is RPS_TOTAL
    bucket = TokenBucket(rate_per_sec=RPS_TOTAL)
    rotator = ProxyRotator(proxies, shuffle=True) if proxies else None
    # distribute IDs to sessions round-robin
    dist = distribute_ids_round_robin(ids, sessions)
    workers = _compute_workers(len(sessions))
    # we'll activate up to 'workers' sessions (safety)
    active_sessions = sessions[:workers]

    results = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futmap = {ex.submit(worker_session_fn, sid, dist[sid], rotator, bucket, afr_impl): sid for sid in active_sessions}
        for fut in as_completed(futmap):
            sid = futmap[fut]
            try:
                results[sid] = fut.result()
            except Exception as e:
                results[sid] = (0,0,0)
                sys.stderr.write(f"{RED}[ERROR]{RESET} session {sid} crashed: {e}\n")
    # final stats
    snap = GLOBAL_STATUS.snapshot()
    print(f"\n{BOLD}{BLU}FINISH{RESET} IDs {snap['done_count']}/{snap['total_ids']}  {EMO_OK} {GRN}{snap['ok_total']}{RESET}  {EMO_BAD} {RED}{snap['fail_total']}{RESET}  SESS {CYN}{snap['used_sessions']}{RESET}/{CYN}{snap['total_sessions']}{RESET}\n")
    return results

# ------------------ ProxyRotator ------------------
class ProxyRotator:
    def __init__(self, proxies, shuffle=True):
        self._list = list(proxies) if proxies else []
        if shuffle and self._list: random.shuffle(self._list)
        self._cycle = cycle(self._list) if self._list else None
        self._lock = threading.Lock()
    def next(self):
        if not self._cycle: return None
        with self._lock:
            return next(self._cycle)

# ------------------ Entrypoint / AFR dummy ------------------
def main(afr_impl):
    sessions = load_sessions()
    if not sessions:
        print(f"{RED}لا يوجد سيشنات في {SESSIONS_FILE}.{RESET}")
        return
    proxies = load_proxies()
    print(f"{BOLD}{MAG}NASR High-Performance (Safe){RESET}  {DIM}RPS={RPS_TOTAL} ThreadsCap(android)={ANDROID_THREADS_CAP}{RESET}\n")

    while True:
        ids = load_ids_once()
        while not ids:
            print(f"{YLW}⚠ لا يوجد IDs حالياً… نعيد المحاولة.{RESET}")
            time.sleep(1.0)
            ids = load_ids_once()
        try:
            run_cycle(sessions, ids, proxies, afr_impl)
        except KeyboardInterrupt:
            print(f"\n{YLW}تم الإيقاف بواسطة المستخدم.{RESET}")
            return
        except Exception as e:
            print(f"{RED}[FATAL]{RESET} تشغيل فشل: {e}")
            traceback.print_exc()
        print(f"{DIM}إعادة تشغيل الدورة...{RESET}")

# ------------------ If run as script (provide dummy afr) ------------------
if __name__ == "__main__":
    # dummy afr implementation for testing — replace with your real afr()
    def afr_dummy(aweme_id, sessionid, session=None, timeout=None):
        # simulate network + processing: RTT randomized
        t = random.uniform(0.05, 0.35)
        time.sleep(t)
        return random.choice([True, True, True, False])  # ~75% success

    try:
        afr_impl = afr  # if user has afr in their environment
    except NameError:
        afr_impl = afr_dummy

    # run
    main(afr_impl)
