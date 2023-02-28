from django.shortcuts import render
from django.http import HttpResponse
import openai

openai.api_key = "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"

def index(request):
    trait_values = {"Openness": 50, "Intellect": 75, "Industriousness": 40, "Orderliness": 60,
                    "Enthusiasm": 30, "Assertiveness": 70, "Politeness": 80, "Compassion": 90,
                    "Withdrawal": 20, "Volatility": 10}

    if request.method == 'POST':
        for trait in trait_values:
            trait_values[trait] = int(request.POST.get(trait))

        response = openai.Completion.create(engine="text-davinci-002", prompt="Analyze the following traits: " + str(trait_values))
        output = response["choices"][0]["text"]
    else:
        output = ""

    context = {"trait_values": trait_values, "output": output}
    return render(request, "index.html", context)
