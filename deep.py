import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BestFirstCrawlingStrategy, BFSDeepCrawlStrategy, DFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import (
    FilterChain,
    DomainFilter,
    URLPatternFilter,
    ContentTypeFilter
)
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer


async def main():
    # Create a relevance scorer
    """
    # KeywordRelevanceScorer - Scorers assign priority values to discovered URLs, helping the crawler focus on the most relevant content first.

    # How scorers work: - Evaluate each discovered URL before crawling - Calculate relevance based on various signals within the webpage - Help the crawler make intelligent choices about traversal order
    """

    scorer = KeywordRelevanceScorer(
        keywords=["hdb"],
        weight=0.9
    )

    # url_filter = URLPatternFilter(patterns=["*blog*", "*docs*"])
    """
    # Combining multiple filters with FilterChain - Crawl4AI includes several specialized filters:
    # Types of filters:
        URLPatternFilter: Matches URL patterns using wildcard syntax
        DomainFilter: Controls which domains to include or exclude
        ContentTypeFilter: Filters based on HTTP Content-Type
        ContentRelevanceFilter: Uses similarity to a text query
        SEOFilter: Evaluates SEO elements (meta tags, headers, etc.)
    """

    # Create a filter chain
    filter_chain = FilterChain([
        # Only follow URLs with specific patterns
        URLPatternFilter(patterns=["*api*", "*ai*"]),

        # Only crawl specific domains
        DomainFilter(
            allowed_domains=["brightdata.com"],
            # blocked_domains=["old.docs.example.com"]
        ),

        # Only include specific content types
        ContentTypeFilter(allowed_types=["text/html"])
    ])

    """
    # Create an SEO filter that looks for specific keywords in page metadata - The SEOFilter helps youidentify pages with strong SEO characteristics:

        seo_filter = SEOFilter(
            threshold=0.5,  # Minimum score (0.0 to 1.0)
            keywords=["tutorial", "guide", "documentation"]
        ),

    # Create a content relevance filter - Measures semantic similarity between query and page content -It's a BM25-based relevance filter using head section content

        relevance_filter = ContentRelevanceFilter(
            query="Web crawling and data extraction with Python",
            threshold=0.7  # Minimum similarity score (0.0 to 1.0)
        )
    """


    # Configure a 2-level deep crawl
    """
        # BFS and DFS Crawling Strategies:
        BFS - The BFSDeepCrawlStrategy uses a breadth-first approach, exploring all links at one depth before moving deeper:
        DFS - The DFSDeepCrawlStrategy uses a depth-first approach, explores as far down a branch as possible before backtracking.

        Key parameters: - max_depth: Number of levels to crawl beyond the starting page - include_external: Whether to follow links to other domains - max_pages: Maximum number of pages to crawl (default: infinite) - score_threshold: Minimum score for URLs to be crawled (default: -inf) - filter_chain: FilterChain instance for URL filtering - url_scorer: Scorer instance for evaluating URLs
    """
    browser_config = BrowserConfig(
        enable_stealth=True,
        headless=False
    )


    config = CrawlerRunConfig(
        # Configure the deep crawl strategy
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,               # Crawl initial page (page 0) + 2 levels deep
            include_external=False,    # Stay within the same domain
            max_pages=25,              # Maximum number of pages to crawl (optional)
            # score_threshold=0.3,       # Minimum score for URLs to be crawled (optional)
        ),

        # deep_crawl_strategy=DFSDeepCrawlStrategy(
        #     max_depth=2,               # Crawl initial page + 2 levels deep
        #     include_external=False,    # Stay within the same domain
        #     max_pages=30,              # Maximum number of pages to crawl (optional)
        #     score_threshold=0.5,       # Minimum score for URLs to be crawled (optional)
        # ),

        # For more intelligent crawling, use BestFirstCrawlingStrategy with scorers to prioritize the most relevant pages. This crawling approach: - Evaluates each discovered URL based on scorer criteria - Visits higher-scoring pages first - Helps focus crawl resources on the most relevant content - Can limit total pages crawled with max_pages - Does not need score_threshold as it naturally prioritizes by score

        # deep_crawl_strategy = BestFirstCrawlingStrategy(
        #     max_depth=2,
        #     include_external=False,
        #     url_scorer=scorer,
        #     max_pages=25,              # Maximum number of pages to crawl (optional)
        #     # filter_chain = FilterChain([url_filter]),
        #     filter_chain=filter_chain
        # ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True,
        stream=True,
        magic=True
    )

    results = []

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun("https://www.propertyguru.com.sg/property-for-rent?listingType=rent&isCommercial=false&page=1&_freetextDisplay=Clementi&hdbEstate=10", config=config):
            results.append(result)
            score = result.metadata.get("score", 0)
            depth = result.metadata.get("depth", 0)
            print(f"Depth: {depth} | Score: {score:.2f} | {result.url}")

    print(f"Crawled {len(results)} high-value pages")
    print(f"Average score: {sum(r.metadata.get('score', 0) for r in results) / len(results):.2f}")

    # Group by depth
    depth_counts = {}
    for result in results:
        print(result.markdown)
        depth = result.metadata.get("depth", 0)
        depth_counts[depth] = depth_counts.get(depth, 0) + 1

    print("Pages crawled by depth:")
    for depth, count in sorted(depth_counts.items()):
        print(f"  Depth {depth}: {count} pages")


if __name__ == "__main__":
    asyncio.run(main())

"""
# Non-streaming mode - When you need the complete dataset before processing - You're performing batch operations on all results together - Crawl time isn't a critical factor


config = CrawlerRunConfig(
    deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1),
    stream=False  # Default behavior
)

async with AsyncWebCrawler() as crawler:
    # Wait for ALL results to be collected before returning
    results = await crawler.arun("https://example.com", config=config)

    for result in results:
        process_result(result)

# Streaming mode - Process results immediately as they're discovered - Start working with early results while crawling continues - Better for real-time applications or progressive display - Reduces memory pressure when handling many pages

config = CrawlerRunConfig(
    deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1),
    stream=True  # Enable streaming
)

async with AsyncWebCrawler() as crawler:
    # Returns an async iterator
    async for result in await crawler.arun("https://example.com", config=config):
        # Process each result as it becomes available
        process_result(result)

"""

"""
Common Pitfalls & Tips
1.Set realistic limits. Be cautious with max_depth values > 3, which can exponentially increase crawl size. Use max_pages to set hard limits.

2.Don't neglect the scoring component. BestFirstCrawling works best with well-tuned scorers. Experiment with keyword weights for optimal prioritization.

3.Be a good web citizen. Respect robots.txt. (disabled by default)

4.Handle page errors gracefully. Not all pages will be accessible. Check result.status when processing results.

5.Balance breadth vs. depth. Choose your strategy wisely - BFS for comprehensive coverage, DFS for deep exploration, BestFirst for focused relevance-based crawling.

6.Preserve HTTPS for security. If crawling HTTPS sites that redirect to HTTP, use preserve_https_for_internal_links=True to maintain secure connections:

config = CrawlerRunConfig(
    deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=2),
    preserve_https_for_internal_links=True  # Keep HTTPS even if server redirects to HTTP
)
Copy
This is especially useful for security-conscious crawling or when dealing with sites that support both protocols.
"""