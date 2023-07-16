from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Category, Profile
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class home_view(ListView):
    model = Blog
    template_name = 'home.html'
    ordering = ['-date']
    #bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(home_view, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

def detail_view(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    liked = False
    if blog.likes.filter(id = request.user.id):
        liked = True
    total_likes = blog.total_like()
    comment = createCommentForm
    return render(request, 'blog_detail.html', {
        'blog' : blog,
        'total_likes': total_likes,
        'liked' : liked,
        'add_comment' : comment,
        'cate_menu' : Category.objects.all()
    })

def add_comment(request, pk):
    blog = Blog.objects.get(pk=pk)
    liked = False
    if blog.likes.filter(id=request.user.id):
        liked = True
    total_likes = blog.total_like()
    comment = createCommentForm
    comment_blog = Blog.objects.get(pk=request.POST['blog'])
    body = request.POST['body']
    comment_user = User.objects.get(pk=request.POST['user'])
    new_comment = Comment(blog = comment_blog, body = body, user = comment_user)
    new_comment.save()
    return render(request, 'blog_detail.html', {
        'blog': blog,
        'total_likes': total_likes,
        'liked': liked,
        'add_comment': comment,
        'cate_menu': Category.objects.all()
    })

class create_view(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = blogForm
    template_name = 'create_blog.html'
    login_url = '/members/login/'
    redirect_field_name = 'login.html'

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(create_view, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

class update_view(UpdateView):
    model = Blog
    form_class = editForm
    template_name = 'update_blog.html'

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(update_view, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

class delete_view(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home_page')

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(delete_view, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

class create_category(LoginRequiredMixin, CreateView):
    model = Category
    form_class = categoryForm
    login_url = '/members/login/'
    redirect_field_name = 'login.html'
    template_name = 'create_category.html'

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(create_category, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context


def listCategoryView(request, cates):
    if (Category.objects.filter(name=cates).exists() == False):
        return render(request, 'not_found_category.html')
    # get to take a record if it has only 1 in database
    category_id = Category.objects.get(name=cates)

    # filter to get many record(can >= 2) with condition
    blogs_category = Blog.objects.filter(category=category_id)
    return render(request, 'list_category.html', {
        'cates' : cates,
        'blogs_category': blogs_category,
        'cate_menu': Category.objects.all()
    })

def likeView(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if blog.likes.filter(id = request.user.id).exists():
        blog.likes.remove(request.user.id)
    else:
        blog.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail_view', args=[str(pk)]))

def userProfileView(request, pk):
    user = User.objects.get(id = pk)
    if Profile.objects.filter(user = user).exists():
        user_profile = Profile.objects.get(user=user)
        return render(request, 'user_profile.html', {
            'cate_menu': Category.objects.all(),
            'user_profile' : user_profile,
        })
    else:
        if request.user.id == pk:
            return render(request, 'add_user_profile_require.html', {
                'cate_menu': Category.objects.all(),
            })
        else:
            return render(request, 'not_found_user_profile.html', {
                'cate_menu': Category.objects.all(),
            })

class addUserProfile(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = profileForm
    template_name = 'add_user_profile.html'
    login_url = '/members/login/'
    redirect_field_name = 'login.html'

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(addUserProfile, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

class updateUserProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = editprofileForm
    template_name = 'update_user_profile.html'
    login_url = '/members/login/'
    redirect_field_name = 'login.html'

    # bring cate_menu data to layout_html
    def get_context_data(self, *args, **kwargs):
        context = super(updateUserProfile, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context
