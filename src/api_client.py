"""
API client interface for fetching match, team, and event data from external sources.
"""
from typing import List, Optional
from .models import Match, Team, Player, MatchEvent

def fetch_match(match_id: str) -> Optional[Match]:
    """Fetch match metadata and events from external API."""
    pass

def fetch_team(team_id: str) -> Optional[Team]:
    """Fetch team and player data from external API."""
    pass

def fetch_events(match_id: str) -> List[MatchEvent]:
    """Fetch event timeline for a match from external API."""
    pass
