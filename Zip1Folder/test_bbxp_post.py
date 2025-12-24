import requests
import json
import time
import uuid

# Configuration
USE_MOCK_MODE = True  # Set to False to send to actual running server
RETRY_COUNT = 3
RETRY_DELAY = 2  # seconds
TEST_BUNDLE_FILE = "simulated_bbxp_test_payload.json"

# Load the test payload
with open(TEST_BUNDLE_FILE, "r") as f:
    payload = json.load(f)

# Ensure test bundle is clearly marked
payload["meta"]["export_permission"] = "restricted"
payload["meta"]["anti_capture"] = True
payload["meta"]["interpretation_hint"] += " (TEST - DO NOT INGEST)"
payload["bundle_id"] = str(uuid.uuid4())
payload["source_framework"] = "bronze_accord (TEST_ONLY)"

# Determine endpoint
if USE_MOCK_MODE:
    print("🧪 MOCK MODE ENABLED — No data will be sent to live endpoint.")
    print("Simulated payload:")
    print(json.dumps(payload, indent=2))
else:
    url = "http://localhost:8000/submit_bbxp_bundle"
    print(f"🔁 Attempting POST to {url}")

    for attempt in range(1, RETRY_COUNT + 1):
        try:
            response = requests.post(url, json=payload, timeout=5)
            response.raise_for_status()
            print("✅ Success:")
            print("Status Code:", response.status_code)
            print("Response:", response.json())
            break
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt < RETRY_COUNT:
                print(f"⏳ Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("❌ All attempts failed. Aborting.")
