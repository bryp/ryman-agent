# Ryman Agent
|Feature|Description|
|---|---|
|ExecutionContext|Central storage that manages all information during execution|
|Tool abstraction|Unifies tools under a consistent interface that can receive context|
|LLM communication layer|LlmRequest selects information for the LLM; LlmClient handles API calls; LlmResponse standardizes responses|
|Agent|Orchestrator that creates context, coordinates information flow, and implements the think–act loop|