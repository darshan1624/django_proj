from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.

def blogHome(request):
    all_blogs = Post.objects.all()
    params = {'all_blogs': all_blogs }
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug):
    fetch_blog = Post.objects.filter(slug = slug)[0]
    comments = BlogComment.objects.filter(post=fetch_blog, parent=None)
    replies = BlogComment.objects.filter(post=fetch_blog).exclude(parent=None) 
    # Created a dict containing parentSno and the replies that belong to it.
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply.comment]
        else: 
            replyDict[reply.parent.sno].append(reply.comment)
    user = request.user
    params = {'fetch_blog': fetch_blog, 'comments':comments, 'user':user, 'replyDict':replyDict}
    return render(request, 'blog/blogPost.html', params)

def postComment(request):
    if request.method == 'POST': 
        user = request.user
        postSno = request.POST.get('postSno')
        commentSno = request.POST.get('commentSno')
        post = Post.objects.get(sno=postSno)
        if commentSno:
            comment = request.POST.get('replyComment')
            parent = BlogComment.objects.get(sno=commentSno)
            new_comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
        else:
            comment = request.POST.get('postComment')
            new_comment = BlogComment(comment=comment, user=user, post=post)
        new_comment.save()

        messages.success(request, 'Your comment has been submitted.')
        return redirect(f'/blog/{post.slug}/')
    else:
        messages.error(request, 'Error')
        return redirect(f'/blog/{post.slug}/')
