from .models import Taglines
from .views import SearchForm

import random

def layout_renderer(request):
    tagline = random.choice(Taglines.objects.all())
    return {
        'tagline': tagline,
        'searchform': SearchForm
    }
