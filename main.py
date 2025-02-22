from appwrite.client import Client
import os


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    # Why not try the Appwrite SDK?
    #
    # client = (
    #     Client()
    #         .set_endpoint("https://cloud.appwrite.io/v1")
    #         .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
    #         .set_key(os.environ["APPWRITE_API_KEY"])
    # )

    # You can log messages to the console
    context.log("Hello, Ramji!")

    # If something goes wrong, log an error
    context.error("Hello, John!")

    # The `context.req` object contains the request data
    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `context.res.send()` dispatches a string back to the client
        return context.res.send("Hello, CK Bro!")

    # `context.res.json()` is a handy helper for sending JSON
    return context.res.json({
        "motto": "Build like a team of hundreds_",
        "learn": "https://appwrite.io/docs",
        "connect": "https://appwrite.io/discord",
        "getInspired": "https://builtwith.appwrite.io",
    })
