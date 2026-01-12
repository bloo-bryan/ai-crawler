import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig, JsonCssExtractionStrategy, LLMConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

# SINGLE-PAGE EXTRACTION WITH JSON SCHEMA USING .arun_many WITH AUTO SCROLLING AND LAZY-LOADING IMAGE EXTRACTION
async def multipage():
    schema_file_path = "property_listing_schema.json"
    with open(schema_file_path, "r") as f:
        schema = json.load(f)

    browser_config = BrowserConfig(
        enable_stealth = True,
        headless = False
    )
    base_wait = """
        const listings = document.querySelectorAll("div.listing-card-v2")
        return listings.length > 0
    }"""

    config = CrawlerRunConfig(
        extraction_strategy=JsonCssExtractionStrategy(schema),
        wait_for_images=True,# tries to ensure images have finished loading before finalizing the HTML
        scan_full_page=True, # tells the crawler to try scrolling the entire page
        scroll_delay=0.5,    # delay (seconds) between scroll steps
        wait_for=base_wait,
        cache_mode=CacheMode.BYPASS,
    )

    url = "https://www.propertyguru.com.sg/property-for-rent?listingType=rent&isCommercial=false&_freetextDisplay=Clementi&hdbEstate=10"
    urls = [f"{url}&page={i}" for i in range(2)]

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=config
        )
        for i, result in enumerate(results):
            if result.success:
                data = json.loads(result.extracted_content)
                print(json.dumps(data, indent=2))
                print(f"Loaded page {i}, count: {len(data)} listings")

            else:
                print(f"❌ Page {i+1} Failed: {result.error_message}")

async def main():
    await multipage()

if __name__ == "__main__":
    asyncio.run(main())