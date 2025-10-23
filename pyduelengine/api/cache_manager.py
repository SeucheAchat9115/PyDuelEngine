import json
import os
from typing import Any, Dict


class YGOPROCache:
    """Simple file-backed JSON cache for the YGOPRO client.

    Responsibilities:
    - ensure cache file exists
    - read and write the cache dict
    """

    def __init__(
        self, 
        cache_dir: str = "cache", 
        filename: str = "ygopro_cache.json"
    ) -> None:
        """Initialize the cache manager.
        Args:
            cache_dir (str): Directory to store the cache file.
            filename (str): Name of the cache file.
        """
        self.cache_dir = cache_dir
        self.filename = filename
        os.makedirs(self.cache_dir, exist_ok=True)
        self.filepath = os.path.join(self.cache_dir, self.filename)
        if not os.path.exists(self.filepath):
            self.write({})

    def read(self) -> Dict[str, Any]:
        """Read the cache file and return the cached data.

        Returns:
            Dict[str, Any]: The cached data.
        """
        with open(self.filepath, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def write(self, data: Dict[str, Any]) -> None:
        """Write the given data to the cache file.

        Args:
            data (Dict[str, Any]): The data to cache.
        """
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
