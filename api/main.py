from fastapi import FastAPI from core.agent_orchestrator import Orchestrator

app = FastAPI(title="Cognitive Brain API") orchestrator = Orchestrator().compile()

@app.post("/chat") async def process_intent(user_input: str): # Initiate the multi-agent reasoning chain response = await orchestrator.ainvoke({ "plan": [], "memory_context": "Initial context", "result": "" }) return {"response": response["result"]}

if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)