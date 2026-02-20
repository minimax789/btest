from decouple import config

try:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN", default="8027723166:AAEPAxi6y_CLkTayU46KgltLRUtVg7pvxWw")
    DEV = config("DEV", default="1772989999")
    OWNER = config("OWNER", default="1772989999 7035550935")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
