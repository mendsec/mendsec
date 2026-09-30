#!/usr/bin/env python3
"""Render the "most used languages" card from owned and allowlisted org repos.

Replaces the metrics languages plugin, whose repository fetch times out
intermittently once org repos are included and then renders an empty card.
This one pages through a minimal GraphQL query and fails loudly instead, so
a bad run leaves the previous card in place.

Usage: languages.py OUT_DIR   (token in GH_TOKEN)
"""
import json
import os
import sys
import urllib.request
from html import escape

USER = "mendsec"
ORGS = ["catnet-io", "barahn", "fabrintek", "MadeiraHackerSpace", "portosoft", "AuraOneStudios"]
# Repos that would misrepresent the card, e.g. vendored third-party code.
SKIPPED = {"AuraOneStudios/unity-open-projects"}
IGNORED = {"HTML", "CSS"}
LIMIT = 10

THEMES = {
    "light": {"text": "#24292f", "muted": "#57606a", "track": "#eaeef2"},
    "dark": {"text": "#c9d1d9", "muted": "#8b949e", "track": "#21262d"},
}

QUERY = """
query($login: String!, $after: String, $user: Boolean!) {
  user(login: $login) @include(if: $user) {
    repositories(first: 50, after: $after, ownerAffiliations: OWNER, isFork: false) { ...page }
  }
  organization(login: $login) @skip(if: $user) {
    repositories(first: 50, after: $after, isFork: false) { ...page }
  }
}
fragment page on RepositoryConnection {
  pageInfo { hasNextPage endCursor }
  nodes { nameWithOwner languages(first: 20) { edges { size node { name color } } } }
}
"""


def graphql(variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {os.environ['GH_TOKEN']}"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = json.load(resp)
    if body.get("errors"):
        sys.exit(f"GraphQL errors: {body['errors']}")
    return body["data"]


def collect():
    sizes, colors = {}, {}
    for login, is_user in [(USER, True)] + [(o, False) for o in ORGS]:
        after = None
        while True:
            data = graphql({"login": login, "after": after, "user": is_user})
            conn = data["user" if is_user else "organization"]["repositories"]
            for repo in conn["nodes"]:
                if repo["nameWithOwner"] in SKIPPED:
                    continue
                for edge in repo["languages"]["edges"]:
                    name = edge["node"]["name"]
                    sizes[name] = sizes.get(name, 0) + edge["size"]
                    colors[name] = edge["node"]["color"] or "#8b949e"
            if not conn["pageInfo"]["hasNextPage"]:
                break
            after = conn["pageInfo"]["endCursor"]
    return sizes, colors


def render(top, colors, count, theme):
    t = THEMES[theme]
    width, rows = 480, (len(top) + 1) // 2
    height = 64 + rows * 22
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="Most used languages">',
        "<style>text{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,"
        "Helvetica,Arial,sans-serif}</style>",
        f'<text x="0" y="16" font-size="14" font-weight="600" fill="{t["text"]}">'
        "Most used languages</text>",
        f'<text x="{width}" y="16" font-size="12" text-anchor="end" fill="{t["muted"]}">'
        f"{count} languages</text>",
        '<clipPath id="bar"><rect x="0" y="28" width="480" height="8" rx="4"/></clipPath>',
        f'<rect x="0" y="28" width="{width}" height="8" rx="4" fill="{t["track"]}"/>',
        '<g clip-path="url(#bar)">',
    ]
    x = 0.0
    for name, share in top:
        w = share * width
        out.append(f'<rect x="{x:.2f}" y="28" width="{w:.2f}" height="8" fill="{colors[name]}"/>')
        x += w
    out.append("</g>")
    for i, (name, share) in enumerate(top):
        cx, cy = (0 if i % 2 == 0 else width // 2), 60 + (i // 2) * 22
        out += [
            f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{colors[name]}"/>',
            f'<text x="{cx + 16}" y="{cy}" font-size="13" fill="{t["text"]}">{escape(name)}</text>',
            f'<text x="{cx + 230}" y="{cy}" font-size="12" text-anchor="end" '
            f'fill="{t["muted"]}">{share * 100:.1f}%</text>',
        ]
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main():
    out_dir = sys.argv[1]
    sizes, colors = collect()
    counted = {k: v for k, v in sizes.items() if k not in IGNORED}
    if not counted:
        sys.exit("No language data collected; refusing to write an empty card")
    ranked = sorted(counted.items(), key=lambda kv: kv[1], reverse=True)[:LIMIT]
    total = sum(v for _, v in ranked)
    top = [(name, size / total) for name, size in ranked]
    for theme in THEMES:
        with open(os.path.join(out_dir, f"languages-{theme}.svg"), "w") as f:
            f.write(render(top, colors, len(sizes), theme))
    for name, share in top:
        print(f"{name:<12} {share * 100:5.1f}%")


if __name__ == "__main__":
    main()
