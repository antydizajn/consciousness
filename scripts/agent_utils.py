#!/usr/bin/env python3
"""
Shared helpers for agent naming and signature policy.
"""

import json
import os
from pathlib import Path


def load_agent_name(arg_name=None):
    if arg_name:
        return str(arg_name).strip()
    env_name = os.environ.get("AGENT_NAME")
    if env_name:
        return env_name.strip()
    profile_path = Path(__file__).resolve().parents[1] / "agent_profile.json"
    if profile_path.exists():
        data = json.loads(profile_path.read_text())
        name = data.get("agent_name") or data.get("name")
        if name:
            return str(name).strip()
    return None


def require_agent_name(arg_name=None):
    name = load_agent_name(arg_name)
    if not name:
        raise ValueError(
            "Agent name required. Provide --agent-name, set AGENT_NAME, "
            "or create agent_profile.json with agent_name."
        )
    return name
