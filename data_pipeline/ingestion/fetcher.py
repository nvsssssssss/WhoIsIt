import json
from urllib.request import Request, urlopen


def fetch_json(url: str) -> dict:
    """Fetch JSON data from an external source."""

    request = Request(
        url,
        headers={
            "User-Agent": "WhoIsIt/0.1",
            "Accept": "application/json",
        },
    )

    with urlopen(request, timeout=10) as response:
        data = response.read()

    return json.loads(data)
