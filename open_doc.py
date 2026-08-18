#!/usr/bin/env python3
import sys
import os
import json
import urllib.request

DEFAULT_URL = os.environ.get("REMNOTE_SERVER_URL", "http://127.0.0.1:7788/mcp").strip()
TOKEN = os.environ.get("REMNOTE_TOKEN", "").strip()

def open_doc(doc_id):
    if not doc_id:
        return
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "open_doc",
            "arguments": {"id": doc_id.strip()}
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
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sys.stdout.write(f"Opened doc {doc_id}")
    except Exception as e:
        sys.stderr.write(f"Error: {e}")

if __name__ == "__main__":
    doc_id = sys.argv[1] if len(sys.argv) > 1 else ""
    open_doc(doc_id)
