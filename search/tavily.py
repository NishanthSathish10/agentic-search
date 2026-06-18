"""
Tavily Search API client.
Returns a list of search results with title, URL, and snippet.
"""

import logging

from tavily import AsyncTavilyClient

import config

logger = logging.getLogger(__name__)


async def search(query: str, num_results: int | None = None) -> list[dict]:
    """
    Search using Tavily Search API.

    Returns list of dicts: [{"title": ..., "url": ..., "snippet": ...}, ...]
    """
    num_results = num_results or config.SEARCH_NUM_RESULTS

    client = AsyncTavilyClient(api_key=config.TAVILY_API_KEY)
    try:
        response = await client.search(
            query=query,
            max_results=num_results,
            search_depth="basic",
        )
    except Exception as e:
        logger.error(f"Tavily search failed: {e}")
        return []

    results = []
    for item in response.get("results", [])[:num_results]:
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "snippet": item.get("content", ""),
        })

    logger.info(f"Tavily search for '{query}' returned {len(results)} results")
    return results
