from widgybench.utils import run_benchmark
from widgybench.site import site

from widgy.contrib.page_builder.models import DefaultLayout, Html
from widgy.contrib.form_builder.models import Form



def setup():
    global layout
    layout = DefaultLayout.add_root(site)
    main = layout.children['main']
    for i in range(10):
        main.add_child(site, Html, content=str(i))

    main.add_child(site, Form)

def benchmark():
    layout.children['main'].render({})


run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'Simple tree creation',
    },
)
