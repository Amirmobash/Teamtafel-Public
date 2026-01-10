import os, re, time, zipfile, random, requests, cv2
import numpy as np

API_KEY = "2QMvcyNdQJyAKXrHk52YTK4C7Mjhdu8SMt3bIgDkwJGXNGyEGL9b4qsI"

OUTPUT_DIR = "personalfotos_200"
ZIP_NAME = "Personalfotos_200_DE.zip"

# =========================
# 200 نفر تولید می‌کنیم
# =========================
first_names = [
    "Max","Lena","Jonas","Marie","Paul","Sophie","Leon","Mila","Noah","Emma",
    "Ben","Mia","Luis","Hannah","Felix","Laura","Tim","Anna","Elias","Nina",
    "David","Lea","Moritz","Clara","Julian","Lisa","Philipp","Sarah","Tom","Johanna",
    "Kevin","Carolin","Daniel","Katharina","Matthias","Franziska","Sebastian","Theresa",
    "Niklas","Jana","Finn","Luca","Amelie","Charlotte","Marlon","Greta","Till","Zoe"
]
last_names = [
    "Müller","Schneider","Weber","Wagner","Becker","Hoffmann","Fischer","Klein","Neumann","Wolf",
    "Krause","Koch","Richter","Werner","Braun","Schmitt","Keller","Hartmann","Vogel","Frank",
    "Lange","Peters","Schäfer","Busch","Weiss","Krüger","Meyer","Lehmann","Bauer","Seidel",
    "Fuchs","Maier","Scholz","Brandt","Kuhn","Otto","Sommer","König","Zimmermann","Herrmann"
]

employees = [("Amir mobasher", 543)]  # این باید باشد

pid = 100
while len(employees) < 200:
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    pid += random.randint(1, 9)
    employees.append((f"{fn} {ln}", pid))

QUERIES = ["headshot face", "portrait face person", "business headshot", "corporate headshot"]

HEADERS = {"Authorization": API_KEY}

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Haar Cascade برای تشخیص چهره
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def has_face(img_bytes):
    img_np = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False
    faces = face_cascade.detectMultiScale(img, 1.1, 5)
    return len(faces) > 0

def safe_filename(s):
    return re.sub(r'[<>:"/\\\\|?*]', "", s)

def fetch_urls():
    query = random.choice(QUERIES)
    r = requests.get(
        "https://api.pexels.com/v1/search",
        headers=HEADERS,
        params={
            "query": query,
            "orientation": "portrait",
            "per_page": 80,
            "page": random.randint(1, 80)
        },
        timeout=20
    )
    r.raise_for_status()
    data = r.json()

    # ⚡ برای سرعت و جلوگیری از فایل‌های خیلی بزرگ، original را برندار:
    urls = []
    for p in data.get("photos", []):
        src = p.get("src") or {}
        urls.append(src.get("large2x") or src.get("large") or src.get("medium") or src.get("original"))
    return [u for u in urls if u]

saved = 0
urls = []

while saved < len(employees):
    if not urls:
        urls = fetch_urls()

    name, pid = employees[saved]
    filename = safe_filename(f"{name}_{pid}.jpg")
    path = os.path.join(OUTPUT_DIR, filename)

    url = urls.pop(0)

    try:
        img = requests.get(url, timeout=30).content
    except Exception:
        print("❌ Download Fehler – übersprungen:", filename)
        continue

    if has_face(img):
        with open(path, "wb") as f:
            f.write(img)
        print(f"✔ Gesicht erkannt: [{saved+1}/200] {filename}")
        saved += 1
    else:
        print("❌ Kein Gesicht – übersprungen")

# ZIP
with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as z:
    for f in os.listdir(OUTPUT_DIR):
        z.write(os.path.join(OUTPUT_DIR, f), f)

print("✅ Fertig. ZIP erstellt:", ZIP_NAME)
