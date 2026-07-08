from agents import Agent, Runner

agent = Agent(name = "Assistant", instructions = "You are a helpful assistant within the service department")

result = Runner.run_sync(agent, "Which technician should I send on a service call involving a dead battery in Longueuil.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
