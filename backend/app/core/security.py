import ipaddress
from urllib.parse import urlparse
from fastapi import HTTPException, status


def validate_public_url(value: str) -> str:
    """Reject non-web URLs, credentials, and literal private IP addresses."""
    parsed = urlparse(value.strip())
    hostname = (parsed.hostname or "").lower().rstrip(".")
    if parsed.scheme not in {"http", "https"} or not hostname or parsed.username or parsed.password:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Enter a valid public http(s) URL.")
    if hostname == "localhost" or hostname.endswith(".localhost") or hostname.endswith(".local"):
        raise HTTPException(status_code=422, detail="Private and local URLs are not allowed.")
    try:
        address = ipaddress.ip_address(hostname)
        if not address.is_global:
            raise ValueError
    except ValueError:
        # Hostnames are resolved and rechecked by the production fetch worker.
        if hostname.replace(".", "").isdigit():
            raise HTTPException(status_code=422, detail="Private and local URLs are not allowed.")
    return value.strip()
