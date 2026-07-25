"""Find nearby hospitals using OpenStreetMap's free Nominatim + Overpass APIs.

No API key or account is required. Needs outbound internet access at
runtime (blocked in some sandboxed dev environments, but available on a
normal machine or typical hosting platform).
"""

import math

import requests

USER_AGENT = "mental-health-hackathon-2026-symptom-checker/1.0 (educational hackathon project)"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OVERPASS_URL = "https://overpass-api.de/api/interpreter"
REQUEST_TIMEOUT = 12


def geocode_location(query: str):
    """Return (lat, lon, display_name) for a free-text location, or None if not found."""
    params = {"format": "json", "q": query, "limit": 1}
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    results = response.json()
    if not results:
        return None
    top = results[0]
    return float(top["lat"]), float(top["lon"]), top.get("display_name", query)


def _haversine_km(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * earth_radius_km * math.asin(math.sqrt(a))


def find_nearby_hospitals(lat: float, lon: float, radius_km: float = 10.0, limit: int = 15) -> list:
    """Return hospitals near (lat, lon), sorted by distance, closest first."""
    radius_m = int(radius_km * 1000)
    query = f"""
    [out:json][timeout:25];
    (
      node["amenity"="hospital"](around:{radius_m},{lat},{lon});
      way["amenity"="hospital"](around:{radius_m},{lat},{lon});
      relation["amenity"="hospital"](around:{radius_m},{lat},{lon});
    );
    out center tags;
    """
    headers = {"User-Agent": USER_AGENT}
    response = requests.post(OVERPASS_URL, data={"data": query}, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    elements = response.json().get("elements", [])

    hospitals = []
    for element in elements:
        tags = element.get("tags", {})
        name = tags.get("name")
        if not name:
            continue

        if element["type"] == "node":
            h_lat, h_lon = element["lat"], element["lon"]
        else:
            center = element.get("center")
            if not center:
                continue
            h_lat, h_lon = center["lat"], center["lon"]

        address = ", ".join(
            part
            for part in (tags.get("addr:housenumber"), tags.get("addr:street"), tags.get("addr:city"))
            if part
        )

        hospitals.append(
            {
                "name": name,
                "lat": h_lat,
                "lon": h_lon,
                "distance_km": _haversine_km(lat, lon, h_lat, h_lon),
                "address": address,
                "phone": tags.get("phone") or tags.get("contact:phone"),
                "emergency": tags.get("emergency") == "yes",
                "directions_url": (
                    f"https://www.google.com/maps/dir/?api=1&origin={lat},{lon}"
                    f"&destination={h_lat},{h_lon}"
                ),
            }
        )

    hospitals.sort(key=lambda h: h["distance_km"])
    return hospitals[:limit]
