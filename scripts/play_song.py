import sys
import re
import urllib.parse
import webbrowser


def get_direct_url(query: str) -> str:
    # If user sends video ID or full URL, use it directly
    if re.match(r'^[a-zA-Z0-9_-]{11}$', query.strip()):
        return f"https://www.youtube.com/watch?v={query.strip()}&autoplay=1"
    if 'youtube.com/watch?v=' in query:
        return query + '&autoplay=1' if '?' in query else query.replace('watch?v=', 'watch?v=') + '&autoplay=1'
    # Fallback: search (user clicks manually)
    return f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"


song = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "lofi hip hop"
url = get_direct_url(song)
webbrowser.open(url)
