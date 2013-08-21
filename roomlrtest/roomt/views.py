from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def post_login(request):
    response = render_to_response('post.html', {'user': request.user})
    return response
