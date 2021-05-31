from officer.models import Tag

def menu(request):
    nav_tags = Tag.objects.all()[:10]
    return { 'nav_tags' : nav_tags,
    }