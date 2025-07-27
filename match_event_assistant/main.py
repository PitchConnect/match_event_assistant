"""
Main entry point for match_event_assistant.
Wires together EventLogger, MatchStateManager, APIIntegration, and Analytics.
Provides a CLI for basic operations.
"""

import os
from dotenv import load_dotenv
from match_event_assistant.event_logging import EventLogger, MatchEvent
from match_event_assistant.match_state import MatchStateManager
from match_event_assistant.api_integration import APIIntegration
from match_event_assistant.analytics import Analytics
from datetime import datetime
import argparse

load_dotenv()

logger = EventLogger()
state_manager = MatchStateManager()
api = APIIntegration(base_url=os.getenv("API_BASE_URL", "http://localhost"))
analytics = Analytics()


def main():
    parser = argparse.ArgumentParser(description="Match Event Assistant CLI")
    parser.add_argument(
        "--log-event", nargs=2, metavar=("TYPE", "DESC"), help="Log a match event"
    )
    parser.add_argument(
        "--update-score", nargs=2, metavar=("TEAM_ID", "INC"), help="Update team score"
    )
    parser.add_argument(
        "--fetch-api", metavar="ENDPOINT", help="Fetch from API endpoint"
    )
    parser.add_argument(
        "--analytics", action="store_true", help="Run analytics on logged events"
    )
    args = parser.parse_args()

    if args.log_event:
        event = MatchEvent(
            timestamp=datetime.now(),
            event_type=args.log_event[0],
            description=args.log_event[1],
        )
        logger.log_event(event)
        print(f"Event logged: {event}")
    if args.update_score:
        team_id = int(args.update_score[0])
        inc = int(args.update_score[1])
        state_manager.update_score(team_id, inc)
        print(f"Score updated: {state_manager.get_state().teams[team_id].score}")
    if args.fetch_api:
        resp = api.get(args.fetch_api)
        print(f"API response: {resp}")
    if args.analytics:
        events = logger.get_events()
        result = analytics.summarize_events(events)
        print(f"Analytics: {result}")


if __name__ == "__main__":
    main()
