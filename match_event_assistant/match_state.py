# flake8: max-line-length=88
"""
Match State Management module for match_event_assistant.
Provides MatchStateManager and supporting data models.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from datetime import datetime


@dataclass
class PlayerState:
    player_id: int
    name: "Optional[str]" = None
    on_field: bool = True


@dataclass
class TeamState:
    team_id: int
    name: "Optional[str]" = None
    score: int = 0
    players: "Dict[int, PlayerState]" = field(default_factory=dict)


@dataclass
class MatchState:
    period: int = 1
    clock: float = 0.0  # seconds elapsed
    is_running: bool = False
    teams: "Dict[int, TeamState]" = field(default_factory=dict)
    last_event_time: "Optional[datetime]" = None


class MatchStateManager:
    """
        Manages the current state of the match (score, time, period, teams, players)
    .
    """

    def __init__(self):
        self.state = MatchState()

    def start_match(self):
        """Start the match clock."""
        self.state.is_running = True
        self.state.last_event_time = datetime.now()

    def stop_match(self):
        """Stop the match clock."""
        self.state.is_running = False
        self.state.last_event_time = datetime.now()

    def update_score(self, team_id: int, increment: int = 1):
        """Update the score for a team."""
        if team_id in self.state.teams:
            self.state.teams[team_id].score += increment
        else:
            self.state.teams[team_id] = TeamState(team_id=team_id, score=increment)
        self.state.last_event_time = datetime.now()

    def get_state(self) -> MatchState:
        """Return the current match state."""
        return self.state
