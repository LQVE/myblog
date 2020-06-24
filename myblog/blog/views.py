from django.shortcuts import render
from django.conf import settings
import logging

# logger = logging.getLogger("blog.views")

def global_setting(request):
    return {"SITE_NAME":settings.SITE_NAME,
            "SITE_DESC":settings.SITE_DESC,}

# Create your views here.
def index_views(request):
    # try:
    #     f = open("notexit.txt")
    # except Exception as e;
    #     logger.error(e)
    return render(request, "index.html",locals())
