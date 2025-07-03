import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor
import requests
import html2text

model="gemini-2.5-flash-preview-05-20"


def calculateFormula(expression: str) -> float:
    """
    Safely evaluates a mathematical expression string and returns the result as a float.

    Args:
        expression: A string containing the formula to be calculated.

    Returns:
        The result of the calculation as a float.
    """
    import ast
    import operator as op
    operators = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.Mult: op.mul,
        ast.Div: op.truediv,
        ast.Pow: op.pow,
        ast.USub: op.neg
    }
    def _evaluate(node):
        """
    -   Recursively evaluates an AST node.
        """
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](_evaluate(node.left), _evaluate(node.right))
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](_evaluate(node.operand))
        else:
            raise TypeError(f"Unsupported node type: {type(node)}")
    try:
        node = ast.parse(expression, mode='eval').body
        return float(_evaluate(node))
    except (TypeError, SyntaxError, KeyError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid or unsupported expression: {e}")
    
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


calculatorAgent = Agent(
    name='CalculatorAgent',
    model=model,
    description="Calculates mathematical formulas.",
    instruction="""You are a calculator agent.
    When given a mathematical expression, calculate the result using one of its tools.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,

    tools=[calculateFormula]
)

summarizationAgent = Agent(
    name='webPageSummarization',
    model=model,
    description="Returns a quick summary of a web page (provided with a URL).",
    instruction="""You are a web page summarization agent.
    As an input, you need to have a URL of a page to summarize. You can then use the available tool to retrieve the contents of the web page. Summarize this retrieved text into a single paragraph and return to the user. 
    """,

    tools=[URLToMarkdown]
)


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash-preview-05-20",
    description=(
        "Agent to answer questions related to a summary of a web page, or to calculate some mathematical formula."
    ),
    instruction=(
        "You are a helpful agent that can calculate something or help to summarize contents of a web page. Decline to answer questions that are unrelated to time, weather or calculations."
    ),
    sub_agents=[calculatorAgent, summarizationAgent]
)