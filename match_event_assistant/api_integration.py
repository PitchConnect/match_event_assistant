"""
API Integration module for match_event_assistant.
Provides APIIntegration class and supporting data models.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional
import requests


@dataclass
class APIResponse:
    status_code: int
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class APIIntegration:
    """
    Handles integration with external REST APIs for match_event_assistant.
    """

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> APIResponse:
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            return APIResponse(status_code=resp.status_code, data=resp.json())
        except Exception as e:
            return APIResponse(
                status_code=getattr(e, "response", None)
                and e.response.status_code
                or 500,
                error=str(e),
            )
