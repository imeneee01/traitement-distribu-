import json
import random
from datetime import datetime, timedelta
from tqdm import tqdm

# Nombre de lignes à générer
N = 100_000  # ~25 Mo (ajuste à 1_000_000 pour du "vrai" Big Data)

# Capteurs et équipements simulés
equipment_ids = [f"EQ-{i:03d}" for i in range(1, 51)]
sensor_ids = [f"S{i:05d}" for i in range(1, 501)]

# Fenêtre temporelle de simulation
start_time = datetime(2025, 10, 12, 8, 0, 0)

with open("sensors_stream.json", "w") as f:
    for i in tqdm(range(N), desc="Generating sensor data"):
        # Incrément temporel (1s)
        ts = start_time + timedelta(seconds=i)
        record = {
            "timestamp": ts.isoformat() + "Z",
            "sensor_id": random.choice(sensor_ids),
            "equipment_id": random.choice(equipment_ids),
            "temperature": round(random.gauss(65, 10), 2),
            "vibration": round(abs(random.gauss(0.5, 0.3)), 3),
            "pressure": round(random.gauss(101, 5), 2),
            "status": random.choices(
                ["OK", "WARN", "ALERT"], weights=[0.85, 0.1, 0.05], k=1
            )[0],
        }
        f.write(json.dumps(record) + "\n")

print(f"✅ Fichier sensors_stream.json généré ({N:,} lignes)")
