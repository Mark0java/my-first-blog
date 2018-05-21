import json
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import Indicators
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def view_store(request):
    indicators = dict(request.POST)
    result = {'status': 'ok', 'indicators': indicators}
    
    Indicators(
        A=float(indicators['A'][0]),
        V=float(indicators['V'][0]),
        W=float(indicators['W'][0]),
        socket_id=int(indicators['socket_id'][0]),
    ).save()
    return HttpResponse(json.dumps(result))


def view_info(request):
    result = []
    indicators = Indicators.objects.all()
    for ind in indicators:
        result.append({'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id, "timestamp": str(ind.timestamp)})
        
    return HttpResponse(json.dumps(result, indent=4))
    

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
