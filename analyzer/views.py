from django.shortcuts import render

from .forms import TextForm


def index(request):
    data = {
        "text": "text one",
        "text_length": 0,
        "words": 0,
        "long_word": "",
        "short_word": "",
        "time_to_read": 0,
    }
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            data["text"] = text
            data["text_length"] = len(text)
            words = text.split()
            data["words"] = len(words)
            data["long_word"] = max(words, key=len)
            data["short_word"] = min(words, key=len)
            data["time_to_read"] = str(data["words"] / 3)[:str(data["words"] / 3).rfind(".")+2]
        else:
            print(form.errors)

    return render(request=request, template_name='index.html', context=data)
