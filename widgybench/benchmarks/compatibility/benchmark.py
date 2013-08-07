from django.contrib.auth.models import AnonymousUser
from django.test.client import RequestFactory

from widgybench.utils import run_benchmark
from widgybench.site import site

from widgy.contrib.page_builder.models import DefaultLayout, Html, Accordion

from widgy.views.api import ShelfView

layout = None
r = None


def setup():
    global layout, r

    layout = DefaultLayout.add_root(site)
    main = layout.children['main']
    for i in range(100):
        main.add_child(site, Html, content=str(i))

    for i in range(100):
        main.add_child(site, Accordion)

    r = RequestFactory().get('/')
    r.user = AnonymousUser()


def benchmark():
    global layout
    ShelfView.get_compatibility_data(site, r, layout.node)

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'ShelfView.get_compatibility_data',
    },
)
