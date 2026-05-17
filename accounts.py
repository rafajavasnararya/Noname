import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNTS = [
    {"user": os.getenv("USER1"), "pass": os.getenv("PASS1"), "game": os.getenv("GAME1")},
    {"user": os.getenv("USER2"), "pass": os.getenv("PASS2"), "game": os.getenv("GAME2")},
    {"user": os.getenv("USER3"), "pass": os.getenv("PASS3"), "game": os.getenv("GAME3")},
    {"user": os.getenv("USER4"), "pass": os.getenv("PASS4"), "game": os.getenv("GAME4")},
    {"user": os.getenv("USER5"), "pass": os.getenv("PASS5"), "game": os.getenv("GAME5")},
]
