#!/usr/bin/env python3
"""PitchConnect CLI for fogis API client"""
import sys
import argparse
import os
import json
from communication.api_client import APIClient


def print_output(data, fmt):
    if fmt == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
    elif fmt == "yaml":
        try:
            import yaml

            print(yaml.dump(data, allow_unicode=True))
        except ImportError:
            print("YAML output requires PyYAML. Falling back to JSON.")
            print(json.dumps(data, indent=2, ensure_ascii=False))
    elif fmt == "table":
        if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
            rows = data["data"]
        elif isinstance(data, list):
            rows = data
        else:
            rows = [data]
        if rows and isinstance(rows[0], dict):
            headers = rows[0].keys()
            print("	".join(headers))
            for row in rows:
                print("	".join(str(row.get(h, "")) for h in headers))
        else:
            print(rows)
    else:
        print(data)


def main():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--output",
        choices=["json", "table", "yaml"],
        default="json",
        help="Output format",
    )
    parent_parser.add_argument(
        "--api-key", type=str, default=None, help="API key (overrides env)"
    )
    parent_parser.add_argument(
        "--base-url", type=str, default=None, help="API base URL (overrides env)"
    )
    parent_parser.add_argument(
        "--timeout", type=int, default=10, help="API timeout (seconds)"
    )
    parent_parser.add_argument(
        "--debug", action="store_true", help="Show debug info on error"
    )

    parser = argparse.ArgumentParser(
        description="PitchConnect match_event_assistant CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # get-match
    parser_match = subparsers.add_parser(
        "get-match", parents=[parent_parser], help="Fetch match metadata"
    )
    parser_match.add_argument("match_id", type=str, help="Match ID")
    # get-events
    parser_events = subparsers.add_parser(
        "get-events", parents=[parent_parser], help="Fetch event timeline"
    )
    parser_events.add_argument("match_id", type=str, help="Match ID")
    # get-roster
    parser_roster = subparsers.add_parser(
        "get-roster", parents=[parent_parser], help="Fetch team rosters"
    )
    parser_roster.add_argument("match_id", type=str, help="Match ID")
    # get-officials
    parser_officials = subparsers.add_parser(
        "get-officials", parents=[parent_parser], help="Fetch match officials"
    )
    parser_officials.add_argument("match_id", type=str, help="Match ID")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("FOGIS_API_KEY")
    base_url = args.base_url or os.environ.get("FOGIS_API_BASE_URL")
    timeout = args.timeout

    client = APIClient(api_key=api_key, base_url=base_url, timeout=timeout)

    try:
        if args.command == "get-match":
            result = client.get_match(args.match_id)
        elif args.command == "get-events":
            result = client.get_events(args.match_id)
        elif args.command == "get-roster":
            result = client.get_roster(args.match_id)
        elif args.command == "get-officials":
            result = client.get_officials(args.match_id)
        else:
            parser.print_help()
            sys.exit(1)
        print_output(result, args.output)
        sys.exit(0)
    except Exception as e:
        if hasattr(args, "debug") and args.debug:
            import traceback

            traceback.print_exc()
        else:
            print(json.dumps({"error": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
