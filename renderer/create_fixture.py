"""Fixture local del renderer. No representa una playlist real de Spotify."""
from __future__ import annotations
import base64
import json
from datetime import datetime, timezone
from pathlib import Path

# PNG 1x1 de prueba en data URI: el workflow comprueba el pipeline y los artefactos,
# no la disponibilidad de portadas reales de Spotify.
PNG_1X1 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/"
    "l1sAAAAASUVORK5CYII="
)
cover = "data:image/png;base64," + PNG_1X1
tracks = []
for index in range(1, 26):
    tracks.append({
        "name": f"Canción de prueba {index:02d}",
        "artists": f"Artista de prueba {((index - 1) % 6) + 1}",
        "durationMs": 175000 + index * 1000,
        "imageUrl": cover,
    })
payload = {
    "type": "real_render_test",
    "generationMode": "integration_test",
    "recordId": "FIXTURE_SPOTIFY_V2",
    "reportId": "FIXTURE_SPOTIFY_V2_REPORT",
    "playlistName": "Fixture local Spotify V2.0",
    "referenceTime": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    "playlistXTracks": tracks,
}
Path("fixture_payload.json").write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("Fixture creado: 25 canciones sintéticas; no usa datos reales.")
