# read from .env
# set -a
# source .env
# set +a

# create connections
orchestrate env activate agentic-inc-3-v2
# orchestrate connections add --app-id playground_app
# orchestrate connections configure -a playground_app --env draft --kind key_value --type team

# orchestrate connections set-credentials -a playground_app --env draft -e LANGFLOW_API_KEY=$LANGFLOW_API_KEY -e LANGFLOW_FLOW_ID=$LANGFLOW_FLOW_ID -e LANGFLOW_BASE_URL=$LANGFLOW_BASE_URL

# create tools
orchestrate tools import -k python -f tools/StatsCalculator.py -r tools/requirements.txt

# create knowledge
orchestrate knowledge-bases import -f knowledge/report_extracted.yaml

# create agents
orchestrate agents import -f agents/StatsAgentADK.yaml
orchestrate agents import -f agents/SalesAgentADK.yaml