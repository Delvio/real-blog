from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView
from blog.forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request, tag_slug=None):
    objects_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        objects_list = objects_list.filter(tags__in=[tag])

    paginator = Paginator(objects_list, 3)

    page = request.GET.get("page")

    if not page:
        page = 1

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "blog/post/list.html",
        {"page": page, "posts": posts, "tag": tag},
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": CommentForm,
        },
    )


def post_share_email(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(
                cd["name"], cd["email"], post.title
            )
            message = 'read "{}" at {}\n\n{}\'s comments: {}'.format(
                post.title, post_url, cd["name"], cd["comments"]
            )
            send_mail(subject, message, "myblog@elvioseverino.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        "blog/post/share.html",
        {"post": post, "form": form, "sent": sent},
    )
