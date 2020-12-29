from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

#emfanizo ola ta antikeimena enow pinaka vasis
def all_blogs(request):
    #posts = Post.objects.all() #fernei oles tis eggrafes toy pinaka post
    #posts = Post.objects.order_by('-date') #fernei sortarismenes me tin pio prosfath hmerominia
    posts = Post.objects.order_by('-date')#[:5] #fernei mono 5
    return render(request, 'blog/all_blogs.html', {'posts': posts})

#yha emfaniso 1 antikeimeno toy pinaka analoga me to post poy epilegei o xristis (link)
def detail(request, post_id):
    #return render(request, 'blog/detail.html', {'id': post_id}) #epistrefei sto detail.html to id san arithmo

    #epistefei to sigekrimeno object vasi tou id allios 404
    post = get_object_or_404(Post, pk=post_id) #vazei to object sti metavliti post
    return render(request, 'blog/detail.html', {'post': post})