import json
from pathlib import Path
from django.utils import timezone

VERSION_PATH = Path(__file__).resolve().parent.parent / "version.json"

def inject_data(request):
    version_data = {}
    if VERSION_PATH.exists():
        with open(VERSION_PATH) as f:
            version_data = json.load(f)
    return {
        "now": timezone.now(),
        "version_info": version_data,
    }