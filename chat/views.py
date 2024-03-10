from django.http import HttpResponse
from django.shortcuts import render
from requests import Request


def index(request: Request) -> HttpResponse:
    return render(request, "index.html")


def room(request: Request, room_name: str) -> HttpResponse:
    return render(request, "room.html", {"room_name": room_name})
