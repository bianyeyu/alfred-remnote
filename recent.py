#!/usr/bin/env python3
import sys
import os
import json
import urllib.request
from datetime import datetime, timedelta

DEFAULT_URL = os.environ.get("REMNOTE_SERVER_URL", "http://127.0.0.1:7788/mcp").strip()
TOKEN = os.environ.get("REMNOTE_TOKEN", "").strip() or "rn_mcp_kG0Stj6GgsLmk5iZ0L8WexNQU6osk1DWtkxa_FqxhuE"

def recent(filter_kw=""):
    if not TOKEN:
        print(json.dumps({
            "items": [{
                "title": "Please configure your RemNote Bearer Token",
                "subtitle": "Open Alfred Preferences -> Workflows -> RemNote Companion -> [x] Configure",
                "valid": False,
                "icon": {"path": "icon.png"}
            }]
        }, ensure_ascii=False))
        return

    now = datetime.now()
    from_date = now - timedelta(days=14)
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "find_edited_docs",
            "arguments": {
                "from": from_date.strftime("%Y-%m-%d"),
                "to": now.strftime("%Y-%m-%d")
            }
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
            
        docs = data.get("result", {}).get("structuredContent", {}).get("table", []) or \
               data.get("result", {}).get("structuredContent", {}).get("documents", [])
               
        items = []
        kw = filter_kw.strip().lower()
        for d in docs:
            title = d.get("title") or d.get("document_name") or "Untitled"
            doc_id = d.get("rem_id") or d.get("document_id") or ""
            iso_time = d.get("iso_timestamp", "")
            
            if kw and (kw not in title.lower()):
                continue
                
            time_str = iso_time[:10] if iso_time else ""
            items.append({
                "title": title,
                "subtitle": f"Last edited: {time_str} • Press Enter to open in RemNote",
                "arg": doc_id,
                "valid": True,
                "icon": {
                    "path": "icon.png"
                }
            })

        if not items:
            items.append({
                "title": "No recent notes found",
                "subtitle": "Make sure RemNote desktop app is running.",
                "valid": False,
                "icon": {"path": "icon.png"}
            })

        print(json.dumps({"items": items}, ensure_ascii=False))

    except Exception as e:
        err_msg = str(e)
        if "401" in err_msg or "403" in err_msg:
            err_title = "Authentication Failed: Token Invalid"
            err_sub = "Please update your Bearer Token in Alfred Workflow Configuration [x]."
        elif "Connection refused" in err_msg or "URLError" in err_msg:
            err_title = "Cannot connect to RemNote Desktop"
            err_sub = "Please make sure RemNote desktop app is open and running."
        else:
            err_title = "RemNote Error"
            err_sub = err_msg

        print(json.dumps({
            "items": [{
                "title": err_title,
                "subtitle": err_sub,
                "valid": False,
                "icon": {"path": "icon.png"}
            }]
        }, ensure_ascii=False))

if __name__ == "__main__":
    kw = sys.argv[1] if len(sys.argv) > 1 else ""
    recent(kw)
