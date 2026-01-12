from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, LLMConfig, DefaultMarkdownGenerator, CacheMode 
from crawl4ai.content_filter_strategy import LLMContentFilter
import os
import re
from dotenv import load_dotenv
import asyncio

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
profile_path = "C:/Users/bryan/.crawl4ai/profiles/bloobryan"


async def llmmathex():
    MATH_EXTRACTOR = """
        // 1. Find all SVG titles
        const titles = document.querySelectorAll('svg title');
        
        titles.forEach(title => {
            // Only process titles that actually contain a MathJax container
            if (title.querySelector('mjx-container')) {
                
                let fullLatexString = "";
                
                // 2. Iterate through ALL child nodes (Text "A=", Element <mjx-container>, Text "?")
                title.childNodes.forEach(node => {
                    
                    // Case A: Text Node (The "A=" or "?")
                    if (node.nodeType === 3) { 
                        fullLatexString += node.textContent;
                    } 
                    
                    // Case B: MathJax Container
                    else if (node.nodeType === 1 && node.tagName.toLowerCase() === 'mjx-container') {
                        // Ask MathJax for the specific math item attached to this container node
                        // We look within the node itself to be precise
                        const mathItems = MathJax.startup.document.getMathItemsWithin(node);
                        
                        if (mathItems.length > 0) {
                            // Append the raw LaTeX (without delimiters yet)
                            fullLatexString += mathItems[0].math;
                        } else {
                            // Fallback: if MathJax API fails, try hidden MathML or alt text
                            fullLatexString += node.textContent;
                        }
                    }
                });
                
                // 3. Wrap the combined result in delimiters
                // We strip existing whitespace to prevent " $$ A= ... $$ " gaps if preferred
                const finalString = ` $$${fullLatexString.trim()} $$ `;
                
                // 4. Overwrite the title with the new pure text
                title.textContent = finalString;
            }
        });
        document.body.classList.add('math-processed');
    """

    math_config = CrawlerRunConfig(
            js_code=MATH_EXTRACTOR,
            wait_for="css:body.math-processed",
            wait_for_images=True,   # tries to ensure images have finished loading before finalizing the HTML
            cache_mode=CacheMode.BYPASS
    )

    # Initialize LLM filter with specific instruction
    filter = LLMContentFilter(
        llm_config = LLMConfig(provider="gemini/gemini-2.5-flash-lite",api_token=google_api_key), #or use environment variable
        instruction="""
        Focus on extracting the core lesson content. Each lesson is a div with class ".step". 
        Include:
        - Key concepts and explanations
        - Example questions and explanations
        - LaTeX code, either inline or as a block. Remove escape backslash characters.
        Exclude:
        - Multiple choice questions and answers
        - Navigation elements
        - Sidebars
        - Footer content
            # LaTeX: Use single backslashes for commands and delimiters unless double backslash is strictly required for a newline.
            # Formatting: Ensure double newlines between headers and paragraphs.
            Format the output as clean markdown with proper markdown formatting and headers.
            """,
            chunk_token_threshold=4096,  # Adjust based on your needs
            verbose=True
        )
    md_generator = DefaultMarkdownGenerator(
        content_filter=filter,
        options={"ignore_links": True}
    )
    llm_config = CrawlerRunConfig(
        markdown_generator=md_generator,
        js_code=MATH_EXTRACTOR,
        wait_for="css:body.math-processed",
        wait_for_images=True,   # tries to ensure images have finished loading before finalizing the HTML
        cache_mode=CacheMode.BYPASS
    )

    browser_config = BrowserConfig(
        headless=False,
        use_managed_browser=True,
        user_data_dir=profile_path,
        browser_type='chromium',
        verbose=True
    )

    c4a = [
        "document.querySelector('#usernameOrEmail').value = 'email';",
        "document.querySelector('#password').value = 'password';",
        "document.querySelector('input#loginButton').click();"
    ]

    init_config = CrawlerRunConfig(
        js_code=c4a,
        wait_for="#content"
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        init = await crawler.arun(
            url="https://www.mathacademy.com/login",
            config=init_config
        )
        if init.success:
            print(init.markdown)

        results = await crawler.arun(
            url="https://mathacademy.com/topics/55",
            config=llm_config
        )
        output_content = results.markdown.fit_markdown
        
        # Post-processing to fix formatting issues
        if output_content:
            # 1. Ensure headers start on a new line (preceded by double newline)
            output_content = re.sub(r'(\s*)(#+ )', r'\n\n\2', output_content)
            
            # 2. Fix LaTeX backslashes (unescape double backslashes)
            # This turns \\{ into \{ and \\ into \ (which might turn \\\\ into \\ for latex newlines)
            output_content = output_content.replace("\\\\", "\\")
        
        print(output_content)  # Filtered markdown content
        
        with open("mathex_output.md", "w", encoding="utf-8") as f:
            f.write(output_content)
        print("Successfully saved output to mathex_output.md")

if __name__ == "__main__":
    asyncio.run(llmmathex())
