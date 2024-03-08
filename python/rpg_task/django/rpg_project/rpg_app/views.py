from django.shortcuts import render


def game(request):
    context = {"players": range(1, 7)}
    return render(request, "rpg_app/index.html", context)
