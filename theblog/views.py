from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
def LikePost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():#if the user who is logged in has liked the post
        post.likes.remove(request.user)#remove from liked table
        liked = False
    else:
        post.likes.add(request.user)#save the like for the user
        liked = True
    return HttpResponseRedirect(reverse('articles_detail', args=[str(pk)]))
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_posts})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    #ordering = ['-id']#mose last post at the bottom
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles_detail.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        like = get_object_or_404(Post, id=self.kwargs['pk'])#grab from Post table of that pk blog  
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        liked = False
        if like.likes.filter(id = self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        total_likes = like.total_likes()#calling from out views.py file
        context["likes"] = total_likes
        context['liked'] = liked
        return context
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
    #fields = '__all__'
class AddCategoryView(CreateView):
    model = Category
    
    template_name = 'add_category.html'
    fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    ordering = ['-timestamp']
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)