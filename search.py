#!/usr/bin/env python3
import sys
import os
import json
import urllib.request

DEFAULT_URL = os.environ.get("REMNOTE_SERVER_URL", "http://127.0.0.1:7788/mcp").strip()
TOKEN = os.environ.get("REMNOTE_TOKEN", "").strip()

def search(query):
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

    if not query.strip():
        print(json.dumps({
            "items": [{
                "title": "Type to search RemNote notes...",
                "subtitle": "Real-time search across your active knowledge base",
                "valid": False,
                "icon": {"path": "icon.png"}
            }]
        }, ensure_ascii=False))
        return

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "search_docs",
            "arguments": {"queries": [query.strip()]}
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
            
        matches = data.get("result", {}).get("structuredContent", {}).get("matches", [])
        items = []
        for m in matches:
            title = m.get("document", "Untitled")
            doc_id = m.get("doc_id", "")
            snippets = " | ".join(m.get("matches", []))
            count = m.get("descendant_count")
            extra = f" ({count} blocks)" if count is not None else ""
            items.append({
                "title": title + extra,
                "subtitle": snippets or f"Open in RemNote • ID: {doc_id}",
                "arg": doc_id,
                "valid": True,
                "text": {
                    "copy": title,
                    "largetype": f"{title}\n\n{snippets}"
                },
                "icon": {
                    "path": "icon.png"
                }
            })

        if not items:
            items.append({
                "title": f"No notes found matching '{query}'",
                "subtitle": "Try a different keyword",
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
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    search(query)
