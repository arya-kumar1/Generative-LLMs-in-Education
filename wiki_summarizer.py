import requests

def summarize_wikipedia_article(title: str) -> str:
    """
    Fetches a summary of a Wikipedia article using the REST API.
    Example: summarize_wikipedia_article("Artificial intelligence")
    """
    base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    encoded_title = requests.utils.quote(title)
    url = f"{base_url}{encoded_title}"

    response = requests.get(url, headers={"User-Agent": "WikiSummarizer/1.0"})
    if response.status_code != 200:
        return f"Error {response.status_code}: Could not retrieve the article."

    data = response.json()

    # Extract summary info
    title = data.get("title", "Unknown Title")
    description = data.get("description", "")
    extract = data.get("extract", "")
    article_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")

    summary = f"**{title}**\n{description}\n\n{extract}\n\nRead more: {article_url}"
    return summary


if __name__ == "__main__":
    topic = input("Enter a Wikipedia topic: ")
    print("\n" + summarize_wikipedia_article(topic))