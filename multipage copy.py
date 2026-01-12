import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, BrowserConfig, JsonCssExtractionStrategy, LLMConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def multipage():
    schema_file_path = "property_listing_schema.json"
    with open(schema_file_path, "r") as f:
        schema = json.load(f)

    browser_config = BrowserConfig(
        enable_stealth = True,
        headless = False
    )
    session_id = "pg_listings"

    base_wait = """
        const listings = document.querySelectorAll("div.listing-card-v2")
        return listings.length > 0
    }"""

    config1 = CrawlerRunConfig(
        extraction_strategy=JsonCssExtractionStrategy(schema),
        wait_for=base_wait,
        session_id=session_id,
        cache_mode=CacheMode.BYPASS
        # not using js_only yet since this is our first load
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(
            url="https://www.propertyguru.com.sg/property-for-rent?listingType=rent&isCommercial=false&_freetextDisplay=Clementi&hdbEstate=10",
            config=config1
        )
        for result in results:
            if result.success:
                    data = json.loads(result.extracted_content)
                    print(json.dumps(data, indent=2))

        print(f"Initial listings load. Count: {len(results)}")

        # For subsequent pages, we run JS to click next page if exists
        js_next_page = """
        const selector = document.querySelector("li.arrow-page a[da-id=hui-pagination-btn-next].page-link");

        if (element) {
            element.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' // Options: 'start', 'center', 'end', 'nearest'
            });
            element.click();
        }
        """
        for i, page in enumerate(range(2)):
            config_next = CrawlerRunConfig(
                session_id=session_id,
                js_code=js_next_page,
                wait_for=base_wait,
                js_only=True,
                extraction_strategy=JsonCssExtractionStrategy(schema),
                cache_mode=CacheMode.BYPASS
            )
            results2 = await crawler.arun(
                url="https://www.propertyguru.com.sg/property-for-rent?listingType=rent&isCommercial=false&_freetextDisplay=Clementi&hdbEstate=10",
                config=config_next
            )
            for result in results2:
                if result.success:
                    data = json.loads(result.extracted_content)
                    print(json.dumps(data, indent=2))

            print(f"Page {i} listings count: {len(results2)}")

async def main():
    await multipage()

if __name__ == "__main__":
    asyncio.run(main())