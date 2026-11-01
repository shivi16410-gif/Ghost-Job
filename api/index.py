import os
import sys

# Vercel executes this file from the repository root. Keep the existing
# backend package intact while exposing its FastAPI ASGI app as /api/*.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.main import app

