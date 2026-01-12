from dotenv.main import load_dotenv
import asyncio
import os
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig, CacheMode, JsonCssExtractionStrategy, DefaultMarkdownGenerator, PruningContentFilter
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
import jsonschema2md
import re
import base64
import uuid

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
MATHACADEMY_EMAIL = os.getenv("MATHACADEMY_EMAIL")
MATHACADEMY_PASSWORD = os.getenv("MATHACADEMY_PASSWORD")
profile_path = "C:/Users/bryan/.crawl4ai/profiles/bloobryan"

async def mathex(): 
    browser_config = BrowserConfig(
        headless=False,
        use_managed_browser=True,
        user_data_dir=profile_path,
        browser_type='chromium',
        verbose=True
    )

    MATH_EXTRACTOR = """
    (async () => {
        // 1. Find all SVG titles
        const titles = document.querySelectorAll('svg title');
        
        titles.forEach(title => {
            let fullLatexString = "";
            let finalString = "";
            if (title.querySelector('mjx-container')) {
                                
                // 2. Iterate through ALL child nodes (Text "A=", Element <mjx-container>, Text "?")
                title.childNodes.forEach(node => {
                    
                    // Case A: Text Node (The "A=" or "?")
                    if (node.nodeType === 3) { 
                        fullLatexString += node.textContent.trim();
                    } 
                    
                    // Case B: MathJax Container
                    else if (node.nodeType === 1 && node.tagName.toLowerCase() === 'mjx-container') {
                        const mathItems = MathJax.startup.document.getMathItemsWithin(node);
                        
                        if (mathItems.length > 0) {
                            // Append the raw LaTeX (without delimiters yet)
                            fullLatexString += mathItems[0].math;
                        } else {
                            // Fallback: if MathJax API fails, try hidden MathML or alt text
                            fullLatexString += node.textContent.trim();
                        }
                    }
                });
                finalString = `$$${fullLatexString.trim()}$$`;
            }
            else {
                fullLatexString += title.textContent.trim();
                if (fullLatexString.length > 0) {
                    finalString = `$${fullLatexString.trim()}$`
                }
            }
            
            // 4. Overwrite the title with the new pure text
            title.textContent = finalString;
        });

        // Extract Sidebar Info
        const topicName = document.querySelector('#sidebar #topicName')?.textContent?.trim() || "";
        const prereqs = Array.from(document.querySelectorAll('#sidebar .prerequisiteLink'))
                            .map(el => el.textContent.trim())
                            .join(',');

        const steps = document.querySelectorAll('div.step');

        // Pre-process images: Fetch and convert to Base64
        const images = document.querySelectorAll('div.step img');
        await Promise.all(Array.from(images).map(async (img) => {
            try {
                // Ensure we fetch from the src
                const response = await fetch(img.src);
                const blob = await response.blob();
                return new Promise((resolve) => {
                    const reader = new FileReader();
                    reader.onloadend = () => {
                        img.setAttribute('data-base64-src', reader.result);
                        resolve();
                    };
                    reader.readAsDataURL(blob);
                });
            } catch (err) {
                console.warn('Failed to fetch image:', img.src, err);
                // Fallback: leave as is, extraction will likely skip or get original src
            }
        }));

        steps.forEach(step => {
            // Attach sidebar info to step
            step.setAttribute('data-topic', topicName);
            step.setAttribute('data-prerequisites', prereqs);
            
            // Include IMG in the selector
            const contentNodes = Array.from(step.querySelectorAll('p, ol, ul, img'));

            const textParts = [];

            contentNodes.forEach(node => {
                // Safety: Skip paragraphs that are actually inside lists to avoid duplication
                if (node.tagName === 'P' && node.closest('li')) return; 
                
                if (node.tagName === 'P') {
                    const text = node.textContent.replace(/\s+/g, ' ').trim();
                    if (text) textParts.push(text);
                }

                else if (node.tagName === 'OL' || node.tagName === 'UL') {
                    const listItems = Array.from(node.querySelectorAll('li'));
                    
                    // Map each LI to a markdown bullet point
                    const listText = listItems.map(li => {
                        const cleanItemText = li.textContent.replace(/\s+/g, ' ').trim();
                        return node.tagName === 'OL' ? `1. ${cleanItemText}` : `* ${cleanItemText}`; 
                    }).join('\\n'); // Separate items with newlines            
                    
                    if (listText) textParts.push(listText);
                }

                else if (node.tagName === 'IMG') {
                    const src = node.getAttribute('data-base64-src') || node.src;
                    const alt = node.alt || 'image';
                    textParts.push(`![${alt}](${src})`);
                }
            });
            
            const fullSectionText = textParts.join('\\n');
            step.setAttribute('data-full-content', fullSectionText);
        });

        document.body.classList.add('math-processed');
    })();
    """

    schema_path = "mathacademy.json"
    if os.path.exists(schema_path):
        with open(schema_path, "r") as f:
            schema = json.load(f)
    else:
        raise Exception("Schema not found")

    c4a = [
        f"document.querySelector('#usernameOrEmail').value = '{MATHACADEMY_EMAIL}';",
        f"document.querySelector('#password').value = '{MATHACADEMY_PASSWORD}';",
        "document.querySelector('input#loginButton').click();"
    ]

    config = CrawlerRunConfig(
        js_code=c4a,
        wait_for="#content"
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:

        result = await crawler.arun(
            url="https://www.mathacademy.com/login",
            config=config
        )

        config2 = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(schema),
            js_code=MATH_EXTRACTOR,
            wait_for="css:body.math-processed",
            wait_for_images=True,   # tries to ensure images have finished loading before finalizing the HTML
            cache_mode=CacheMode.BYPASS,
        )

        results = await crawler.arun(
            url="https://www.mathacademy.com/topics/935",
            config=config2
        )

        for result in results:
            print(f"URL: {result.url}")
            print(f"Success: {result.success}")
            if result.success:
                data = json.loads(result.extracted_content)
                print(data)
                topic = data[0]['topic']
                with open(f"{topic}.md", "w", encoding="utf-8") as md_file:
                    prereqs = data[0]['prerequisites'].split(',')
                    md_file.write(f"---")
                    md_file.write("\nPrerequisites:\n")

                    for prereq in prereqs:
                        md_file.write(f"- [[{prereq}]]\n")
                        
                    md_file.write("---\n")

                    if not os.path.exists("ai-crawler/images"):
                        os.makedirs("ai-crawler/images")
                    for section in data:
                        title = section.get('header', '')
                        content = section.get('content', '')

                        if title:
                            title = title.replace(":", ": ")
                            md_file.write(f"## {title}\n")

                        if content:
                            # Process images
                            def replace_image(match):
                                alt_text = match.group(1)
                                data_url = match.group(2)
                                
                                if "base64," in data_url:
                                    try:
                                        _, b64_data = data_url.split("base64,", 1)
                                        image_data = base64.b64decode(b64_data)
                                        
                                        image_filename = f"img_{uuid.uuid4().hex[:8]}.png"
                                        image_path = os.path.join("ai-crawler", "images", image_filename)
                                        
                                        with open(image_path, "wb") as img_f:
                                            img_f.write(image_data)
                                            
                                        return f"![{alt_text}](images/{image_filename})"
                                    except Exception as e:
                                        print(f"Error saving image: {e}")
                                        return match.group(0) # Return original on error
                                return match.group(0)

                            # Regex to find ![alt](data:image/...) pattern
                            content = re.sub(r'!\[(.*?)\]\((data:image\/[^;]+;base64,[^\)]+)\)', replace_image, content)

                            content = content.replace("\n\n\n", "\n\n")
                            md_file.write(content)
                            md_file.write("\n\n---\n")
                # print(result.fit_html)
                # print(result.markdown.fit_markdown)
            else:
                print("Failed to extract structured data")


if __name__ == "__main__":
    asyncio.run(mathex())