import asyncio
from crawl4ai import AsyncWebCrawler, DefaultMarkdownGenerator, PruningContentFilter, CacheMode
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig(verbose=True)  # Leave blank or verbose=True to enable verbose logging
    run_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.6),
            options={"ignore_links": True}  # include links as text in markdown, discard link
        ),
        word_count_threshold=10,        # Minimum words per content block
        # exclude_external_links=True,    # Remove external links
        excluded_tags=['form', 'header'],
        exclude_external_links=True,

        # Content processing
        process_iframes=True,           # Process iframes content
        remove_overlay_elements=True,   # Remove popups/modals

        # Cache control
        cache_mode=CacheMode.ENABLED  # Use cache if available

    )


    async with AsyncWebCrawler(config=browser_config) as crawler:
        # The arun() method returns a CrawlResult object with several useful properties. Here's a quick overview (see CrawlResult for complete details):
        result = await crawler.arun(
            url="https://brightdata.com/blog/web-data/crawl4ai-and-deepseek-web-scraping",
            config=run_config
        )

        if result.success:
            print("Content:", result.markdown[:500])  # First 500 chars

            # Process images
            for image in result.media["images"]:
                print(f"Found image: {image['src']}")

            # Process links
            for link in result.links["internal"]:
                print(f"Internal link: {link['href']}")

            # print(result.markdown)  # Print clean markdown content

            # Different content formats
            # print(result.html)         # Raw HTML
            # print(result.cleaned_html) # Cleaned HTML
            # print(result.markdown.raw_markdown) # Raw markdown from cleaned html
            # print(result.markdown.fit_markdown) # Most relevant content in markdown

            # Check success status
            # print(result.success)      # True if crawl succeeded
            # print(result.status_code)  # HTTP status code (e.g., 200, 404)

            # # Access extracted media and links
            # print(result.media)        # Dictionary of found media (images, videos, audio)
            # print(result.links)        # Dictionary of internal and external links

        else:  # check if crawl was successful, or handle the errors
            print(f"Crawl failed: {result.error_message}")
            print(f"Status code: {result.status_code}")

if __name__ == "__main__":
    asyncio.run(main())