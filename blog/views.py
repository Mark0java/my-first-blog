import json
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import Indicators
from django.views.decorators.csrf import csrf_exempt
from .models import On_Off


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
    

@csrf_exempt

def view_info(request):
    result = []
    ind = Indicators.objects.latest('timestamp') 
    result.append({'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id})
  
    return HttpResponse(json.dumps(result, indent=4))
    
    
def view_history(request):
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

    
def view_set_on_off(request):
    on_off = dict(request.POST)
    value = float(on_off['on_off'][0])
    print("Server retrieved data from mobile: '%s'. Save to database: %s" % (on_off, value))

    o, is_new = On_Off.objects.get_or_create(id=1, defaults={'on_off': 0})
    o.on_off = value
    o.save()
    return HttpResponse(json.dumps({'status': 'ok', 'on_off': on_off}))


def view_get_on_off(request):
    ind_on = On_Off.objects.get(id=1)
    response = json.dumps({'on_off': ind_on.on_off}, indent=4)
    print(response)
    return HttpResponse(response)
