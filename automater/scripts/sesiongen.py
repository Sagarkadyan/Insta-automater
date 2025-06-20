import instaloader

username = input("Instagram username: ").strip()
password = input("Instagram password (not hidden): ").strip()

L = instaloader.Instaloader()
L.login(username, password)
L.save_session_to_file(f"/storage/emulated/0/automater/sessions/{username}.session")

print(f"[✅] Session saved for {username}")
