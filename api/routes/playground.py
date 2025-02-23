from os import getenv
from phi.playground import Playground

from agents.finance import get_finance_agent
from agents.research import get_research_agent
from agents.web_search import get_web_search_agent
from agents.youtube import get_youtube_agent

######################################################
## Router for the agent playground
######################################################

finance_agent = get_finance_agent(debug_mode=True)
research_agent = get_research_agent(debug_mode=True)
web_search_agent = get_web_search_agent(debug_mode=True)
youtube_agent = get_youtube_agent(debug_mode=True)

# Create a playground instance
playground = Playground(agents=[web_search_agent, research_agent, finance_agent, youtube_agent])
# Log the playground endpoint with phidata.app
if getenv("RUNTIME_ENV") == "dev":
    playground.create_endpoint("http://localhost:8000")

playground_router = playground.get_router()
