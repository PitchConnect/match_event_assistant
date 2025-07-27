"""
Data models for match events, players, teams, and matches.
"""

from pydantic import BaseModel
from typing import Optional, List


class Player(BaseModel):
    id: str
    name: str
    number: Optional[int]
    team_id: str


class Team(BaseModel):
    id: str
    name: str
    players: Optional[List[Player]] = None


class MatchEvent(BaseModel):
    event_type: str  # e.g., 'goal', 'warning', 'substitution'
    minute: int
    second: Optional[int] = None
    player: Optional[Player] = None
    team: Optional[Team] = None
    description: Optional[str] = None


class Match(BaseModel):
    id: str
    date: str  # ISO format
    teams: List[Team]
    events: Optional[List[MatchEvent]] = None
    venue: Optional[str] = None
    referees: Optional[List[str]] = None
