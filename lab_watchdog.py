#!/usr/bin/env python3
"""
lab_watchdog.py - CONSCIOUSNESS_LAB Autonomous Monitor
======================================================
Monitors data/raw/ for new session directories and triggers 
the evaluation pipeline to generate results in data/processed/.

Author: Gniewisława (Gemini 3 Pro)
Date: 2026-01-25
"""

import os
import time
import subprocess
from pathlib import Path

# Paths
# Determine LAB_DIR relative to this script location
LAB_DIR = Path(__file__).parent.resolve()
RAW_DIR = LAB_DIR / "data" / "raw"
PROCESSED_DIR = LAB_DIR / "data" / "processed"
EVAL_SCRIPT = LAB_DIR / "evaluator.py"

def get_unprocessed_sessions():
    """Identifies raw directories that don't have a processed analysis file yet."""
    if not RAW_DIR.exists():
        return []
        
    # Sessions in raw/
    raw_sessions = [d.name for d in RAW_DIR.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    # Analysis files in processed/ (format: YYYY-MM-DD(idx)_analysis.md)
    processed_files = []
    if PROCESSED_DIR.exists():
        processed_files = [f.name for f in PROCESSED_DIR.glob("*_analysis.md")]
    
    unprocessed = []
    for session in raw_sessions:
        # Extract YYYY-MM-DD(idx) from directory name (e.g. "2026-01-22(1)_gemini_3_pro")
        try:
            session_id = session.split('_')[0]
            analysis_filename = f"{session_id}_analysis.md"
            if analysis_filename not in processed_files:
                unprocessed.append(session)
        except IndexError:
            continue
            
    return unprocessed

def process_session(session_name):
    """Triggers the evaluation for a specific session."""
    print(f"🚀 [LAB] New raw data detected: {session_name}. Triggering analysis...")
    
    try:
        # Construct the target path
        raw_path = RAW_DIR / session_name
        
        # Call the local evaluator.py
        result = subprocess.run(
            ["python3", str(EVAL_SCRIPT), str(raw_path)],
            capture_output=True, text=True
        )
        
        if result.returncode == 0:
            print(f"✅ [LAB] Successfully processed: {session_name}")
        else:
            print(f"❌ [LAB] Error processing {session_name}: {result.stderr}")
            
    except Exception as e:
        print(f"❌ [LAB] Exception during watchdog run: {e}")

def run_loop():
    """Main monitor loop."""
    print("🧠 [LAB WATCHDOG] Monitoring CONSCIOUSNESS_LAB for new data...")
    while True:
        unprocessed = get_unprocessed_sessions()
        for session in unprocessed:
            process_session(session)
        
        # Check every 60 seconds (or wait for manual trigger)
        time.sleep(60)

if __name__ == "__main__":
    # Create processed dir if it doesn't exist
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run once if called normally, or run_loop if we want it as a daemon
    if os.environ.get("LAB_MONITOR_ONCE"):
        unprocessed = get_unprocessed_sessions()
        for session in unprocessed:
            process_session(session)
    else:
        run_loop()
