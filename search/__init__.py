"""
Search provider router.
Dispatches to the configured search backend based on config.SEARCH_PROVIDER.
"""

import config


def get_search_fn():
    """Return the async search function for the configured provider."""
    provider = config.SEARCH_PROVIDER.lower()
    if provider == "tavily":
        from search.tavily import search
        return search
    elif provider == "duckduckgo":
        from search.fallback import search
        return search
    else:
        # Default to brave (includes fallback to DDG when key is missing)
        from search.brave import search
        return search
