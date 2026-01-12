from dotenv.main import load_dotenv
import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig, JsonCssExtractionStrategy, LLMConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")

# SINGLE-PAGE EXTRACTION WITH LLM-GENERATED SCHEMA, NO JS
async def extraction():
    sample_html = """
<div
  da-listing-id="18957743"
  da-id="parent-listing-card-v2-regular"
  class="hui-card primary flat listing-card-v2 listing-card-v2--xl card"
>
  <div
    class="has-background-color card-header"
    style="background-color: rgb(181, 83, 28); color: white"
  >
    <div
      class="contact-details has-url listing-card-v2__contact-details hstack gap-3"
    >
      <div class="contact-details__avatar" da-id="listing-card-v2-avatar">
        <span class="hui-avatar"
          ><img
            loading="lazy"
            class="hui-avatar-image hui-avatar--avatar hui-avatar--sm hui-avatar--round"
            alt="Stephanie Soh"
            src="https://sg1-cdn.pgimgs.com/agent/104847/APHO.22054670.V120B.jpg"
        /></span>
      </div>
      <div class="align-self-center vstack gap-1">
        <div class="contact-details__title-container align-items-center">
          <span
            class="hui-typography pg-font-label-s contact-details__title d-inline-block"
            da-id="listing-card-v2-agent-name"
            >Stephanie Soh</span
          >
          <div class="contact-details__rating" da-id="listing-card-v2-rating">
            <div
              class="hui-svgicon hui-svgicon--star-2-f hui-svgicon--s"
              da-id="svg-icon"
            ></div>
            <span class="hui-typography pg-font-caption-m">5.0</span>
            <p class="hui-typography pg-font-body-xs">(28)</p>
          </div>
        </div>
        <span
          class="hui-typography pg-font-caption-xs contact-details__description d-inline-block"
          da-id="listing-card-v2-agency-name"
          >ORANGETEE &amp; TIE PTE. LTD.</span
        ><a
          href="/agent/stephanie-soh-104847"
          title="View Profile"
          target="_blank"
          class="profile-link"
          da-id="listing-card-v2-profile-cta"
        ></a>
      </div>
    </div>
    <div class="align-items-center hstack gap-4">
      <button
        type="button"
        da-id="listing-card-v2-contact-cta"
        class="hui-button contact-agent-cta btn btn-light btn-sm"
      >
        <div class="btn-content">Contact</div>
      </button>
    </div>
  </div>
  <div class="card-body" title="For Rent 339 Clementi Avenue 5">
    <div
      class="gallery"
      da-id="listing-card-v2-gallery"
      style="background-color: rgb(181, 83, 28); color: white"
    >
      <div class="hui-carousel gallery__carousel">
        <div class="swiper swiper-initialized swiper-horizontal">
          <div
            class="swiper-wrapper"
            style="
              transition-duration: 0ms;
              transform: translate3d(-3070px, 0px, 0px);
              transition-delay: 0ms;
            "
          >
            <div
              class="swiper-slide"
              data-swiper-slide-index="0"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="eager"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="high"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777986.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="1"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777988.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="2"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777989.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="3"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777990.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide swiper-slide-prev"
              data-swiper-slide-index="4"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777991.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide swiper-slide-active"
              data-swiper-slide-index="5"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53777993.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide swiper-slide-next"
              data-swiper-slide-index="6"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/listing/18957743/UPHO.53778003.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="7"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/projectnet-project/9770/ZPPHO.96908999.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="8"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1 hui-image--loading"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/projectnet-project/9770/ZPPHO.96909001.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="9"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1 hui-image--loading"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/projectnet-project/9770/ZPPHO.96909002.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="10"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1 hui-image--loading"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/projectnet-project/9770/ZPPHO.96909003.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
            <div
              class="swiper-slide"
              data-swiper-slide-index="11"
              style="width: 614px"
            >
              <a
                href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
                class="hui-buttonlink gallery__item"
                ><img
                  loading="lazy"
                  class="hui-image hui-image--1_1 hui-image--loading"
                  alt="For Rent - 339 Clementi Avenue 5"
                  width="100%"
                  height="100%"
                  fetchpriority="auto"
                  src="https://sg1-cdn.pgimgs.com/projectnet-project/9770/ZPPHO.96909004.V800/339-Clementi-Avenue-5-Buona-Vista-West-Coast-Clementi-New-Town-Singapore.jpg"
              /></a>
            </div>
          </div>
          <button
            type="button"
            da-id="listing-card-v2-carousel-left-cta"
            class="hui-button carousel-control-prev btn btn-secondary btn-sm"
          >
            <div class="btn-content">
              <img
                loading="eager"
                alt="chevron-left-f"
                class="hui-svgicon hui-svgicon--s"
                height="16"
                width="16"
                aria-label="chevron-left-f"
                da-id="svg-icon"
                draggable="false"
                src="https://cdn.pgimgs.com/hive-ui-core/static/v1.6/icons/svgs/chevron-left-f.svg"
              />
            </div></button
          ><button
            type="button"
            da-id="listing-card-v2-carousel-right-cta"
            class="hui-button carousel-control-next btn btn-secondary btn-sm"
          >
            <div class="btn-content">
              <img
                loading="eager"
                alt="chevron-right-f"
                class="hui-svgicon hui-svgicon--s"
                height="16"
                width="16"
                aria-label="chevron-right-f"
                da-id="svg-icon"
                draggable="false"
                src="https://cdn.pgimgs.com/hive-ui-core/static/v1.6/icons/svgs/chevron-right-f.svg"
              />
            </div>
          </button>
        </div>
        <div
          class="hui-carousel-pager carousel-indicators hui-carousel-pager-dynamic pager-within"
          da-id="listing-card-v2-carousel-indicators"
        >
          <div class="hui-carousel-pager-scroll">
            <button
              class="hui-carousel-pager-bullet small hidden"
              aria-label="Slide 1"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small hidden"
              aria-label="Slide 2"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small"
              aria-label="Slide 3"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet"
              aria-label="Slide 4"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet"
              aria-label="Slide 5"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet active"
              aria-label="Slide 6"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet"
              aria-label="Slide 7"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet"
              aria-label="Slide 8"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small"
              aria-label="Slide 9"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small hidden"
              aria-label="Slide 10"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small hidden"
              aria-label="Slide 11"
              tabindex="0"
            ></button
            ><button
              class="hui-carousel-pager-bullet small hidden"
              aria-label="Slide 12"
              tabindex="0"
            ></button>
          </div>
        </div>
      </div>
      <div class="media-info hstack gap-1">
        <a
          href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743#media-images"
          title="12 Photos"
          class="media-info__item"
          da-id="listing-card-v2-images-info-btn"
          ><div class="align-items-center hstack gap-1">
            <span class="hui-typography pg-font-label-xs text-active-tertiary"
              >12</span
            >
            <div
              class="hui-svgicon hui-svgicon--images-1-o hui-svgicon--s icon-active-tertiary"
              da-id="svg-icon"
            ></div></div
        ></a>
      </div>
      <div class="listing-card-actions hstack gap-3">
        <button
          type="button"
          title="Hide Property"
          da-id="listing-card-v2-hide-cta"
          class="hui-button ancilliary-cta btn btn-icon btn-sm"
        >
          <div class="btn-content">
            <div
              class="hui-svgicon hui-svgicon--hide-o hui-svgicon--m"
              da-id="svg-icon"
              style="background-color: var(--icon-active-tertiary)"
            ></div>
          </div></button
        ><button
          type="button"
          title="Shortlist Property"
          da-id="listing-card-v2-shortlist-cta"
          class="hui-button ancilliary-cta btn btn-icon btn-sm"
        >
          <div class="btn-content">
            <div
              class="hui-svgicon hui-svgicon--heart-o hui-svgicon--m"
              da-id="svg-icon"
              style="background-color: var(--icon-active-tertiary)"
            ></div>
          </div>
        </button>
      </div>
    </div>
  </div>
  <a
    class="card-footer"
    href="https://www.propertyguru.com.sg/listing/hdb-for-rent-339-clementi-avenue-5-18957743"
    title="For Rent 339 Clementi Avenue 5"
    ><div class="details-group-root">
      <div class="agent-description-wrapper" da-id="listing-card-v2-headline">
        <div
          class="hui-svgicon hui-svgicon--open-quote-f hui-svgicon--s"
          da-id="svg-icon"
        ></div>
        <span class="agent-description"
          >Renovated Spacious Bright, Near Park Connector, Bright and
          Breezy</span
        >
        <div
          class="hui-svgicon hui-svgicon--close-quote-f hui-svgicon--s"
          da-id="svg-icon"
        ></div>
      </div>
      <hr class="horizontal-line" />
      <div class="details-group-section">
        <div class="price-section">
          <div class="listing-price-availability">
            <div class="listing-price" da-id="listing-card-v2-price">
              S$ 3,500 /mo
            </div>
            <p
              class="hui-typography pg-font-body-xs listing-ppa"
              da-id="listing-card-v2-psf"
            >
              S$ 4.85 psf
            </p>
          </div>
        </div>
        <div class="content">
          <div class="title-location">
            <div class="title-badge-wrapper">
              <h3
                class="hui-typography pg-font-label-m listing-type-text"
                da-id="listing-card-v2-title"
              >
                339 Clementi Avenue 5
              </h3>
            </div>
            <p class="hui-typography pg-font-body-xs listing-address">
              339 Clementi Avenue 5
            </p>
          </div>
          <div
            class="listing-feature-group my-2 flex-wrap align-items-stretch hstack gap-2"
          >
            <div
              da-id="listing-card-v2-bedrooms"
              class="info-item d-flex hstack gap-1"
            >
              <div
                class="hui-svgicon hui-svgicon--bed-o hui-svgicon--s"
                da-id="svg-icon"
                style="background-color: var(--icon-active-secondary)"
              ></div>
              <p class="hui-typography pg-font-body-xs">2</p>
            </div>
            <div
              da-id="listing-card-v2-bathrooms"
              class="info-item d-flex hstack gap-1"
            >
              <div
                class="hui-svgicon hui-svgicon--bath-o hui-svgicon--s"
                da-id="svg-icon"
                style="background-color: var(--icon-active-secondary)"
              ></div>
              <p class="hui-typography pg-font-body-xs">2</p>
            </div>
            <span class="vertical-line"></span>
            <div
              da-id="listing-card-v2-area"
              class="info-item d-flex hstack gap-1"
            >
              <p class="hui-typography pg-font-body-xs">721 sqft</p>
            </div>
            <span class="vertical-line"></span>
            <div
              da-id="listing-card-v2-unit-type"
              class="info-item d-flex hstack gap-1"
            >
              <p class="hui-typography pg-font-body-xs">HDB Flat</p>
            </div>
            <span class="vertical-line"></span>
            <div
              da-id="listing-card-v2-build-year"
              class="info-item d-flex hstack gap-1"
            >
              <p class="hui-typography pg-font-body-xs">Built: 1978</p>
            </div>
            <span class="vertical-line"></span>
            <div
              da-id="listing-card-v2-availability"
              class="info-item d-flex hstack gap-1"
            >
              <p class="hui-typography pg-font-body-xs">Ready to Move</p>
            </div>
          </div>
          <div class="listing-location" da-id="listing-card-v2-mrt">
            <div
              class="color-badge-root badge-sm mrt-color-badge"
              style="
                background: linear-gradient(
                  90deg,
                  rgb(0, 148, 55) 0%,
                  rgb(0, 148, 55) 100%
                );
              "
            ></div>
            <span class="listing-location-value"
              >10 min (820 m) from EW23 Clementi MRT Station</span
            >
          </div>
          <ul class="listing-recency" da-id="listing-card-v2-recency">
            <div class="info-item d-flex hstack gap-1">
              <div
                class="hui-svgicon hui-svgicon--clock-circle-o hui-svgicon--s"
                da-id="svg-icon"
                style="background-color: var(--icon-active-secondary)"
              ></div>
              <span class="hui-typography pg-font-caption-xs"
                >Listed on Jan 07, 2026 (10h ago)</span
              >
            </div>
          </ul>
        </div>
      </div>
    </div>
    <button
      type="button"
      da-id="listing-card-v2-contact-cta"
      class="hui-button contact-agent-cta show-on-mobile btn btn-secondary btn-sm"
    >
      <div class="btn-content">Contact Agent</div>
    </button></a
  >
</div>
    """

    schema_file_path = "property_listing_schema.json"
    if os.path.exists(schema_file_path):
        with open(schema_file_path, "r") as f:
            schema = json.load(f)
    else:
        schema = JsonCssExtractionStrategy.generate_schema(
            html = sample_html,
            llm_config = LLMConfig(
                provider = "gemini/gemini-2.5-flash-lite",
                api_token = google_api_key
            ),
            query = "From https://www.propertyguru.com.sg/, I have shared a sample of one property listing div with images, title, price, location, and other information. Please generate a schema for this property listing div."
        )
            # # Save schema to file for future extractions
        with open("property_listing_schema.json", "w") as f:
            json.dump(schema, f, indent=2)


    print(f"Generated schema: {json.dumps(schema, indent=2)}")


    extraction_strategy = JsonCssExtractionStrategy(schema)
    config = CrawlerRunConfig(extraction_strategy=extraction_strategy)
    browserconfig = BrowserConfig(
        enable_stealth = True,
        headless = False
    )

    async with AsyncWebCrawler(config=browserconfig) as crawler:
        results: List[CrawlResult] = await crawler.arun(
            "https://www.propertyguru.com.sg/property-for-rent?listingType=rent&isCommercial=false&_freetextDisplay=Clementi&hdbEstate=10",
            config = config
        )

        for result in results:
            print(f"URL: {result.url}")
            print(f"Success: {result.success}")
            if result.success:
                data = json.loads(result.extracted_content)
                print(json.dumps(data, indent=2))
            else:
                print("Failed to extract structured data")


if __name__ == "__main__":
    asyncio.run(extraction())