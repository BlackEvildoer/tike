import random
import requests
from colorama import *
import webbrowser
import time
import sys

def kata(s):
 for c in s + "\n":
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(10./1000)
  
kata("""
\033[1;31m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


\033[1;31m BY : BLACK
""")


chart = '.qwertyuio.pa.sd_fghj_klzx.cv_bnm1234567890_'
rq = requests.session()
f = Fore.MAGENTA
r = Fore.GREEN
w = Fore.RED

print(""
      )
print(""
      )
print(""
      )
tknb = input(f + "ENTER YOUR TOKEN : ")
id = input(f + "ENTER YOUR ID : ")
print("==========================================")
btn = input(r + "ENTER BKA : ")
if btn == "" \
          :
    while True:
        lst = str("".join(random.choice(chart) for _ in range(5)))
        trl = f"https://www.tiktok.com/@{lst}?"
        hdr = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        rqs = rq.get(trl, headers=hdr).status_code
        if rqs == 404:
            print(f'{f}[{r}Y{f}]{f} Available: {f}[{w}{lst}{f}]')

            bot = f'https://api.telegram.org/bot{tknb}/sendMessage?chat_id={id}&text= USER DONE : {lst}\nBY : - 《@B_1_2_4》'
            rq.get(bot)
            with open("  ALKING ", "a") as gre:
                gre.write(lst + "\n")
        else:
            print(f'{f}[{r}N{f}]{r} UnAvailable: {f}[{w}{lst}{f}]')
