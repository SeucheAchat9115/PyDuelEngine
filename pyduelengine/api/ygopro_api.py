import requests
import os
import json
from .cache_manager import YGOPROCache


class YGOPROAPIClient():
    BASE_URL = "https://db.ygoprodeck.com/api/v7/"

    def __init__(self, cache_dir: str = "cache") -> None:
        """Initialize the YGOPRO API client.
        Args:
            cache_dir (str): Directory to cache API responses.
        """
        self.cache_dir = cache_dir
        self.session = requests.Session()
        self.cache = YGOPROCache(cache_dir=self.cache_dir)

    def get_cards_by_ids(self, card_ids: list[str]) -> dict:
        """Fetch multiple card information by a list of card IDs from the YGOPRO API.
        Args:
            card_ids (list[str]): The list of card IDs to fetch.
        Returns:
            dict: A dictionary mapping card IDs to their information.
        """

        data_in_cache = self.cache.read()

        cards_data = []
        for card_id in card_ids:
            if card_id in data_in_cache:
                # Cache hit, return cached data
                cards_data.append(data_in_cache[card_id])
                continue

            # Not cached or cache invalid, fetch from API
            url = f"{self.BASE_URL}cardinfo.php?id={card_id}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            card_data = response.json()["data"]

            if len(card_data) > 1:
                raise ValueError(f"Multiple cards found for ID {card_id}")
            card_data = card_data[0]

            keys_to_remove = ["card_images", "card_prices", "card_sets"]
            for key in keys_to_remove:
                card_data.pop(key, None)

            data_in_cache[card_id] = card_data
            cards_data.append(card_data)

        self.cache.write(data_in_cache)

        return cards_data

    def enrich_deck_with_card_info(self, deck_data: dict) -> dict:
        """Enrich the deck data with card information from the YGOPRO API.
        Args:
            deck_data (dict): The YGOPRO deck data.
        Returns:
            dict: The enriched deck data with all card information.
        """
        enriched_deck = {"main": [], "extra": [], "side": []}

        for section in ["main", "extra", "side"]:
            card_ids = deck_data.get(section, [])
            enriched_deck[section] = self.get_cards_by_ids(card_ids)

            if len(enriched_deck[section]) != len(card_ids):
                raise ValueError(f"Mismatch in number of cards for section {section}")

        return enriched_deck