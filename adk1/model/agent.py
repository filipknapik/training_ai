import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor


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


calculatorAgent = Agent(
    name='CalculatorAgent',
    model=model,
    instruction="""You are a calculator agent.
    When given a mathematical expression, calculate the result using one of its tools.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,
    description="Calculates mathematical formulas.",
    tools=[calculateFormula]
)

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash-preview-05-20",
    description=(
        "Agent to answer questions about the time and weather in a city, or to calculate some mathematical formula."
    ),
    instruction=(
        "You are a helpful agent who can calculate something or respond to questions on particular time and weather in a city provided by a user. Decline to answer questions that are unrelated to time, weather or calculations."
    ),
    tools=[get_weather, get_current_time],
    sub_agents=[calculatorAgent]
)