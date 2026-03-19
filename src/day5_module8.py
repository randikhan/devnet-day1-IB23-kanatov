import requests, json, hashlib, os

TOKEN = os.environ.get("WEBEX_TOKEN", "N2Q2ODMwMTEtMjU5Ny00NmQ4LWE4MTMtNGQwZWIwODM1ZmMwM2NlZTgzNTMtZjc5_P0A1_381a95f5-7349-4f5b-bc0d-1e1f574b419a")
hash8 = hashlib.sha256(TOKEN.encode()).hexdigest()[:8]
H = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
BASE = "https://webexapis.com/v1"

def save(path, data):
    import pathlib; pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    open(path, "w").write(json.dumps(data, indent=2))

# me
me = requests.get(f"{BASE}/people/me", headers=H).json()
save("artifacts/day5/webex/me.json", me)

# rooms list
rooms = requests.get(f"{BASE}/rooms", headers=H, params={"max":100}).json()
save("artifacts/day5/webex/rooms_list.json", rooms)

# create room
room = requests.post(f"{BASE}/rooms", headers=H, json={"title": f"DevNet-{hash8}"}).json()
save("artifacts/day5/webex/room_create.json", room)
room_id = room["id"]

# post message
msg = requests.post(f"{BASE}/messages", headers=H, json={"roomId": room_id, "text": f"Test {hash8}"}).json()
save("artifacts/day5/webex/message_post.json", msg)

# list messages
msgs = requests.get(f"{BASE}/messages", headers=H, params={"roomId": room_id}).json()
save("artifacts/day5/webex/messages_list.json", msgs)

print("Done!", hash8)