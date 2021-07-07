import time
from typing import Union, Dict

from config import Config


cache_max_age = Config().cache_max_age


class _CachedResult:
    def __init__(self, cached_result: dict):
        self.cached_at = time.time()
        self.cached_result = cached_result


_cached_results: Dict[str, _CachedResult] = {}


def add_cached_result(search_query: str, result: dict):
    _cached_results[search_query] = _CachedResult(result)


def get_cached_result(search_query: str) -> Union[dict, None]:
    if search_query in _cached_results:
        result = _cached_results[search_query]
        if time.time() - result.cached_at <= cache_max_age:
            return result.cached_result
        _cached_results.pop(search_query)
