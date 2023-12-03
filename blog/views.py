from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

blogs = [
    {"title": "First Blog", "content": "This is the content of the first blog."},
    {"title": "Second Blog", "content": "Another blog entry with some content."},
    {"title": "Third Blog", "content": "Content for the third blog entry."},
    {"title": "Fourth Blog", "content": "Content for the fourth blog entry."},
    {"title": "Fifth Blog", "content": "Content for the fifth blog entry."},
    {"title": "Sixth Blog", "content": "Content for the sixth blog entry."},
    {"title": "Seventh Blog", "content": "Content for the seventh blog entry."},
    {"title": "Eighth Blog", "content": "Content for the eighth blog entry."},
    {"title": "Ninth Blog", "content": "Content for the ninth blog entry."},
    {"title": "Tenth Blog", "content": "Content for the tenth blog entry."},
]


def home(req: HttpRequest):
    return render(req, "index.html", {"blogs": blogs[:2]})
