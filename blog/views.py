import json
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import Indicators
from django.views.decorators.csrf import csrf_exempt
from .models import On_Off
from dialogflow_lite.dialogflow import Dialogflow
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Bright


@csrf_exempt
@require_http_methods(['POST'])
@csrf_exempt
def view_store(request):
    client_access_token = 'a4074b8968b642569227649d49ea41eb'
    dialogflow = Dialogflow(client_access_token=client_access_token)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['queryResult']['parameters']
    responses = dialogflow.text_request(str(input_text))
    print(input_text)
    Indicators(
        A=float(input_text['A']),
        V=float(input_text['V']),
        W=float(input_text['W']),
        socket_id=float(input_text['socket_id']),
    ).save()

    if request.method == "POST":
        data = {'': 'ok'}
        return JsonResponse(data, status=200)




def brightnees(request):
    values = dict(request.POST)
    result = {'status': 'ok', 'value': values}

    Bright(value=values).save()
    return HttpResponse(json.dumps(result))







# @csrf_exempt
# def view_store(request):
#     indicators = dict(request.POST)
#     result = {'status': 'ok', 'indicators': indicators}
#
#     Indicators(
#         A=float(indicators['A'][0]),
#         V=float(indicators['V'][0]),
#         W=float(indicators['W'][0]),
#         socket_id=int(indicators['socket_id'][0]),
#     ).save()
#     return HttpResponse(json.dumps(result))
    

@csrf_exempt
def view_set_on_off(request):
    if request.method == "POST":
        value = dict(request.POST).get('on_off')
        # print("Server retrieved data from mobile: '%s'. Save to database: %s" % (on_off, value))
        # DO NOT PRINT ANYTHING !!!!!!  use .format instead %
        if value and isinstance(value, list):
            value = value[0]
            o, is_new = On_Off.objects.get_or_create(user=request.user.id, on_off=value)
            o.save()
            return HttpResponse(json.dumps({'status': 'ok', 'on_off': value}))
    return HttpResponse(json.dumps({'status': 'invalid'}))


# def view_get_on_off(request):
#     ind_on = On_Off.objects.latest('timestamp')
#     response = json.dumps({'on_off': ind_on.on_off}, indent=4)
#     return HttpResponse(response)
#
def view_get_on_off(request):
    ind_on = get_object_or_404(On_Off, user=request.user.id) #On_Off.objects.get(user=request.user.id)
    response = json.dumps ({'on_off': ind_on.on_off}, indent=4)
    return HttpResponse(response)


def view_info(request):
    result = []
    try:
        ind = Indicators.objects.latest('timestamp')
        result.append({'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id})
    except Indicators.DoesNotExist:
        pass
    return HttpResponse(json.dumps(result, indent=4))
    
    
def view_history(request):
    result = []
    try:
        result = [{'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id, "timestamp": str(ind.timestamp)} for ind in Indicators.objects.all()]
    except Indicators.DoesNotExist:
        pass
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
