from django.shortcuts import render, redirect

from post.models import Post


def post_list_view(request):

    if request.method == 'POST':
        likes = request.POST.get('likes', 0)
        likes = int(likes) + 1
    else:
        likes = 0
    context = {'posts': Post.objects.all(),
            'likes': likes}
    return render(request, 'post_list.html', context)


def post_detail_view(request, slug):
    if request.method == 'POST':
        likes = request.POST.get('likes', 0)
        likes = int(likes) + 1
    else:
        likes = 0

    context = {'post': Post.objects.get(slug=slug),
               'likes': likes}
    return render(request, 'post_detail.html', context)

def post_create_view(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        author = request.POST.get('author')
        title = request.POST.get('title')
        body = request.POST.get('body')
        likes = request.POST.get('likes')

        post = Post()
        post.post_id = post_id
        post.author = author
        post.title = title
        post.body = body
        post.likes = likes

        post.save()
        return redirect('post_list')

    context = {'post': Post.objects.all()}

    return render(request, 'create_post.html', context=context)
