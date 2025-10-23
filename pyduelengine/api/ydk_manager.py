from typing import Dict
from .ygopro_api import YGOPROAPIClient


class YDKDeckManager:
    """Manager for loading .ydk deck files and enriching them via YGOPRO API client.

    Responsibilities:
    - load a YDK file from disk
    - delegate enrichment to a YGOPROAPIClient instance
    """

    def __init__(self, cache_dir: str = "cache") -> None:
        self.client = YGOPROAPIClient(cache_dir=cache_dir)

    def load_and_enrich(self, file_path: str) -> Dict[str, list]:
        """Load a .ydk file and return an enriched deck dict.

        Args:
            file_path: path to the .ydk file

        Returns:
            A dict with keys 'main', 'extra', 'side' containing enriched card dicts.
        """
        print("Loading and enriching YDK deck from:", file_path)
        raw_deck = self._load_ydk_deck_file(file_path)
        enriched = self.enrich_deck(raw_deck)
        return enriched
    
    def load(self, file_path: str) -> Dict[str, list]:
        """Load a .ydk file and return the raw deck dict.

        Args:
            file_path: path to the .ydk file
        Returns:
            A dict with keys 'main', 'extra', 'side' containing card IDs as strings.
        """
        print("Loading YDK deck from:", file_path)
        return self._load_ydk_deck_file(file_path)

    def _load_ydk_deck_file(self, file_path: str) -> Dict[str, list]:
        """Internal: read a .ydk file and parse into sections.

        This mirrors the previous standalone `load_ydk_deck_file` behaviour.
        """
        ydk_data_dict = {"main": [], "extra": [], "side": []}
        current_section = None
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for line in content.splitlines():
            line = line.strip()
            if line == "#main":
                current_section = "main"
            elif line == "#extra":
                current_section = "extra"
            elif line == "!side":
                current_section = "side"
            elif line.startswith("#") or line.startswith("!"):
                continue
            elif line.isdigit() and current_section is not None:
                line = line.zfill(8)
                ydk_data_dict[current_section].append(line)

        return ydk_data_dict

    def enrich_deck(self, deck_data: Dict[str, list]) -> Dict[str, list]:
        """Enrich a parsed deck dict by delegating to the YGOPRO client.

        Returns the same structure but with card info dicts instead of IDs.
        """
        return self.client.enrich_deck_with_card_info(deck_data)
