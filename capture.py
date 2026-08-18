#!/usr/bin/env python3
import sys
import os
import json
import urllib.request
from datetime import datetime

DEFAULT_URL = os.environ.get("REMNOTE_SERVER_URL", "http://127.0.0.1:7788/mcp").strip()
TOKEN = os.environ.get("REMNOTE_TOKEN", "").strip() or "rn_mcp_kG0Stj6GgsLmk5iZ0L8WexNQU6osk1DWtkxa_FqxhuE"

def call_tool(name, args):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": name,
            "arguments": args
        }
    }
    req = urllib.request.Request(
        DEFAULT_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
    )
    with urllib.request.urlopen(req, timeout=3) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data.get("result", {}).get("structuredContent", {})

def capture(text):
    if not TOKEN:
        sys.stdout.write("Error: RemNote Token not configured")
        return

    if not text.strip():
        sys.stdout.write("Note is empty")
        return

    try:
        today = datetime.now().strftime("%Y-%m-%d")
        daily_res = call_tool("get_daily_doc", {"date": today})
        doc_id = daily_res.get("document_id")
        if not doc_id:
            sys.stdout.write("Failed to resolve Daily Document")
            return

        res = call_tool("append_doc", {"id": doc_id, "text": text.strip(), "pos": "bottom"})
        if res.get("ok") or res.get("appended"):
            sys.stdout.write(f"Added to Daily Note: {text.strip()}")
        else:
            sys.stdout.write("Failed to append note")
    except Exception as e:
        sys.stdout.write(f"Error: {e}")

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else ""
    capture(text)
