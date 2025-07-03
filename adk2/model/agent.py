import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, SequentialAgent
from google.adk.code_executors import BuiltInCodeExecutor
import requests
import html2text

model="gemini-2.5-flash-preview-05-20"


def URLToMarkdown(url: str) -> str:
    """
    Fetches content from a URL, converts its HTML to Markdown, and returns it.

    Args:
        url: The URL of the website to convert.

    Returns:
        A string containing the website content as Markdown,
        or an error message if the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html_content = response.text

        converter = html2text.HTML2Text()
        markdown_content = converter.handle(html_content)

        return markdown_content

    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve the URL. Reason: {e}"
    except Exception as e:
        # Handle other potential errors
        return f"An unexpected error occurred: {e}"

summarizationAgent = Agent(
    name='webPageSummarization',
    model=model,
    description="Returns a quick summary of a web page (provided with a URL).",
    instruction="""You are a web page summarization agent.
    As an input, you need to have a URL of a page to summarize. You can then use the available tool to retrieve the contents of the web page. Summarize this retrieved text into a single paragraph and return to the user. 
    """,

    tools=[URLToMarkdown]
)

translationAgent = Agent(
    name='translationAgent',
    model=model,
    description="Translates text from English to Polish",
    instruction="""You are a translation agent that can translate text from English to Polish.
    As an input you are provided text to translate. Return only the translated text, no introduction.
    """,
)

safeguardAgent = Agent(
    name='safeguardAgent',
    model=model,
    description="Checks if the summary of a web page provided has any references to contents not appropriate for minors",
    instruction="""You are a safeguard agent that checks if the provided summary of a web page contains any material not suitable for minors under age of 8. Specifically, detect if the summary contains references to violance (even if it's based on news), sex or other disturbing content. If no such content is found, return the original input summary. If sensitive contents is found, return that the contents of this page violates the policy. 
    """,
)

safeWebPageSummarization = SequentialAgent(
    name="safeWebPageSummarization",
    description=(
        "Agent to retrieve the contents of a web page using its URL, check if contents is acceptable for minors"),
    sub_agents=[summarizationAgent, safeguardAgent]
)

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash-preview-05-20",
    description=(
        "Agent to summarize contents of a web page, in a safe way, in Polish"
    ),
    instruction=(
        "You are a helpful agent that can summarize the contents of a particular web page in a minor-safe way; it can also translate text from English to Polish. "
    ),
    sub_agents=[safeWebPageSummarization, translationAgent]
)