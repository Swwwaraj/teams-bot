from botbuilder.core import BotFrameworkAdapter, TurnContext
from botbuilder.schema import Activity, ActivityTypes
import asyncio
from aiohttp import web

async def on_message_activity(turn_context: TurnContext):
    await turn_context.send_activity("You said: " + turn_context.activity.text)

async def handle(request):
    body = await request.json()
    activity = Activity().deserialize(body)

    turn_context = TurnContext(BotFrameworkAdapter(), activity)

    if activity.type == ActivityTypes.message:
        await on_message_activity(turn_context)

    return web.Response()

app = web.Application()
app.router.add_post("/api/messages", handle)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)
