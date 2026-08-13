import os
import xml.etree.ElementTree as ET

import requests
from dotenv import load_dotenv

load_dotenv()


class get_news(list):
    NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
    RSS_FALLBACK_URL = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"

    def __init__(self, country="us", limit=5, timeout=10, api_key=None):
        self.country = country
        self.limit = limit
        self.timeout = timeout
        self.api_key = api_key or os.getenv("NEWS_API_KEY")

        super().__init__(self._load_headlines())

    def refresh(self):
        """Reload the latest headlines and update the list in place."""
        self[:] = self._load_headlines()
        return self

    def _load_headlines(self):
        headlines = self._fetch_from_news_api()

        if headlines:
            return headlines

        headlines = self._fetch_from_rss()

        if headlines:
            return headlines

        return ["No news sources were available right now."]

    def _fetch_from_news_api(self):
        if not self.api_key:
            return []

        try:
            response = requests.get(
                self.NEWS_API_URL,
                params={
                    "country": self.country,
                    "pageSize": self.limit,
                    "apiKey": self.api_key,
                },
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, ValueError):
            return []

        articles = data.get("articles", [])
        headlines = []

        for article in articles:
            title = (article.get("title") or "").strip()

            if not title:
                continue

            source = (article.get("source") or {}).get("name")

            if source:
                headlines.append(f"{title} - {source}")
            else:
                headlines.append(title)

            if len(headlines) >= self.limit:
                break

        return headlines

    def _fetch_from_rss(self):
        try:
            response = requests.get(self.RSS_FALLBACK_URL, timeout=self.timeout)
            response.raise_for_status()
            root = ET.fromstring(response.text)
        except (requests.RequestException, ET.ParseError):
            return []

        headlines = []

        for item in root.findall("./channel/item"):
            title = (item.findtext("title") or "").strip()

            if not title:
                continue

            headlines.append(title)

            if len(headlines) >= self.limit:
                break

        return headlines