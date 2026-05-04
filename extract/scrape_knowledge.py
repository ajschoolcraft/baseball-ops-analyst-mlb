"""Scrape knowledge base sources and save as markdown files.

Reads URLs from a config list, scrapes each with requests + beautifulsoup4,
converts to markdown, and saves to knowledge/raw/. Used by GitHub Actions
for scheduled re-scraping.
"""

import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

SOURCES = [
    ("01-statcast-metrics-context.md", "https://baseballsavant.mlb.com/statcast-metrics-context"),
    ("02-fangraphs-wrc-plus.md", "https://library.fangraphs.com/offense/wrc/"),
    ("03-driveline-stuff-plus-pitch-models.md", "https://www.drivelinebaseball.com/2021/12/what-is-stuff-quantifying-pitches-with-pitch-models/"),
    ("04-fangraphs-woba.md", "https://library.fangraphs.com/offense/woba/"),
    ("05-fangraphs-fip.md", "https://library.fangraphs.com/pitching/fip/"),
    ("06-fangraphs-babip.md", "https://library.fangraphs.com/pitching/babip/"),
    ("07-fangraphs-war.md", "https://library.fangraphs.com/misc/war/"),
    ("08-savant-expected-stats.md", "https://baseballsavant.mlb.com/leaderboard/expected_statistics"),
    ("09-savant-barrel-definition.md", "https://www.mlb.com/glossary/statcast/barrel"),
    ("10-savant-exit-velo-launch-angle.md", "https://www.mlb.com/glossary/statcast/exit-velocity"),
    ("11-savant-pitch-tracking.md", "https://www.mlb.com/glossary/statcast"),
    ("12-fangraphs-ops-plus.md", "https://library.fangraphs.com/offense/ops/"),
    ("13-bp-intro-sabermetrics.md", "https://www.baseballprospectus.com/glossary/"),
    ("14-bp-drc-plus.md", "https://www.baseballprospectus.com/glossary/index.php?search=DRC"),
    ("15-tangotiger-linear-weights.md", "https://library.fangraphs.com/principles/linear-weights/"),
    ("16-savant-statcast-glossary.md", "https://baseballsavant.mlb.com/statcast-metrics-context"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BaseballAnalyticsBot/1.0; +https://github.com/ajschoolcraft/baseball-ops-analyst-mlb)"
}

RAW_DIR = Path(__file__).resolve().parent.parent / "knowledge" / "raw"


def scrape_source(filename: str, url: str) -> bool:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"SKIP {filename}: {e}")
        return False

    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    main = soup.find("main") or soup.find("article") or soup.find("body")
    content = md(str(main), heading_style="ATX", strip=["img"])

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out = RAW_DIR / filename
    out.write_text(f"Source: {url}\n\n{content.strip()}\n")
    print(f"OK   {filename} ({len(content)} chars)")
    return True


def main():
    ok, skip = 0, 0
    for filename, url in SOURCES:
        if scrape_source(filename, url):
            ok += 1
        else:
            skip += 1
    print(f"\nDone: {ok} scraped, {skip} skipped")
    if skip > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
