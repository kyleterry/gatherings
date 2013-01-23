from annoying.decorators import render_to


@render_to('news/view.html')
def view_post(request, post_id):
    pass
