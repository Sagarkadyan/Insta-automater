# force_sessionid_extract.py
import instaloader

USERNAME = "trianga_tapes"

L = instaloader.Instaloader()

try:
    L.load_session_from_file(USERNAME)
    cookies = L.context._session.cookies.get_dict()
    print(f"[INFO] Cookies found in session file:")
    for key, val in cookies.items():
        print(f"  {key} = {val}")
    
    sessionid = cookies.get("sessionid")
    if sessionid:
        print(f"\n✅ Extracted sessionid: {sessionid}")
    else:
        print("❌ sessionid not found in cookies.")
except Exception as e:
    print(f"[ERROR] Failed to load session or extract cookies: {e}")
