import gradio as gr
from model import model, get_predicted_query, train_from_db
from db import DB_CONTEXT

dbContext = DB_CONTEXT()
gpt = model(dbContext)

def execute_first_query(prompt_text):
    sql_query = get_predicted_query(gpt, prompt_text)
    queries = sql_query.split("\n")
    first_query = None
    for query in queries:
        if query.startswith("A:"):
            first_query = query[3:].strip()
            break

    if first_query:
        try:
            result = dbContext.cursor(first_query)
            return {"result": result}
        except Exception as e:
            dbContext.connection.rollback()
            return {"error": str(e)}
    else:
        return {"error": "No query found in the response"}

iface = gr.Interface(
    fn=execute_first_query,
    inputs="text",
    outputs="json",
    title="AI based query assistent",
    description="Ask any questions in the context of your database"
)

iface.launch()