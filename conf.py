import os
## TXT-k elérési útja ##
assets_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                           "assets")

def path(fajl_nev: str) -> str:
    return os.path.join(assets_path, fajl_nev)

## Fontok, Színek ##
kis_font = ("Segoe UI", 16)
nagy_font = ("Segoe UI", 24)

