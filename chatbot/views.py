import os
from django.shortcuts import render
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

_client = None


def get_openai_client():
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            _client = OpenAI(api_key=api_key)
    return _client


def chat(request):
    response_text = ""
    if request.method == "POST":
        user_input = request.POST.get("message", "").strip()
        if user_input:
            client = get_openai_client()
            if not client:
                response_text = "Error: OPENAI_API_KEY is not configured."
            else:
                try:
                    response = client.responses.create(
                        model="gpt-5-mini",
                        input=user_input,
                    )
                    response_text = response.output_text
                except OpenAIError as exc:
                    response_text = f"Error communicating with OpenAI: {exc}"
    return render(
        request,
        "chatbot/chat.html",
        {
            "response": response_text,
        },
    )
