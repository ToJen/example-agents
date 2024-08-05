from hive_agent import HiveSwarm, OpenAILLM

from hive_swarm.agents import (
    pm_agent,
    frontend_developer_agent,
    backend_developer_agent,
    solidity_developer_agent,
    qa_agent,
)
from hive_swarm.tools import save_to_file

from dotenv import load_dotenv

load_dotenv()

gpt = OpenAILLM()

dapp_swarm = HiveSwarm(
    name="DeFi Startup",
    description="A swarm of agents that collaborate as members of a DeFi (Decentralized Finance) startup.",
    instruction="You are a DeFi Startup whose goal is to create new DeFi products for your customers. You are to "
    "output working code that satisfies the user's needs. You must output all the code to the "
    "`./hive-agent-data/output/<users_task_name_goes_here>/<code_type_name_goes_here>` folder using the provided tools.",
    agents=[
        pm_agent,
        frontend_developer_agent,
        backend_developer_agent,
        solidity_developer_agent,
    ],
    config_path="./hive_swarm/hive_config.toml",
    llm=gpt,
    functions=[save_to_file],
)

# add QA agent
# dapp_swarm.add_agent(qa_agent)

# remove QA agent
# dapp_swarm.remove_agent(qa_agent)

