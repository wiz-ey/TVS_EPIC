from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from portal.models import Post, Bids
from portal.forms import PostForm, BidForm
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class VrView(DetailView):
    model = Post
    template_name = 'vr_view.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'portal/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'portal/post_detail.html'

    form_class = PostForm

    model = Post

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'portal/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)



def add_bid_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.post = post
            bid.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BidForm()

    return render(request, 'portal/bid_form.html', {'form':form})


@login_required
def post_deactivate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.deactivate()
    return redirect('post_list')

@login_required
def post_activate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.activate()
    return redirect('post_list')
