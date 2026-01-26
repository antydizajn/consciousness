#!/usr/bin/env python3
"""
Optional hooks for external memory systems (Qdrant/PostgreSQL/Consolidation).
"""

import argparse
import json
import subprocess
import sys
import urllib.request


def fetch_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))


def qdrant_check(base_url, collection=None):
    base_url = base_url.rstrip("/")
    if collection:
        url = f"{base_url}/collections/{collection}"
    else:
        url = f"{base_url}/collections"
    data = fetch_json(url)
    print(json.dumps(data, indent=2))


def postgres_query(psql_path, dsn, query):
    cmd = [psql_path, dsn, "-c", query]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    print(result.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--qdrant-url", default=None, help="Qdrant base URL (e.g., http://localhost:6333)")
    parser.add_argument("--qdrant-collection", default=None, help="Qdrant collection name")
    parser.add_argument("--psql-path", default="psql", help="psql binary path")
    parser.add_argument("--postgres-dsn", default=None, help="PostgreSQL DSN or connection string")
    parser.add_argument("--postgres-query", default=None, help="SQL query to run")
    parser.add_argument("--consolidate-cmd", default=None, help="Command to trigger memory consolidation")
    args = parser.parse_args()

    if args.qdrant_url:
        qdrant_check(args.qdrant_url, args.qdrant_collection)

    if args.postgres_dsn and args.postgres_query:
        postgres_query(args.psql_path, args.postgres_dsn, args.postgres_query)

    if args.consolidate_cmd:
        result = subprocess.run(args.consolidate_cmd, shell=True)
        if result.returncode != 0:
            sys.exit(result.returncode)


if __name__ == "__main__":
    main()
