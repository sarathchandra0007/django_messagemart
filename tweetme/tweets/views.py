from django.shortcuts import render
from tweets.models import Tweet
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#
class TweetListView(LoginRequiredMixin,ListView):
    template_name="tweets/list_view.html"
    #queryset=Tweet.objects.all()
    def get_queryset(self,*args,**kwargs):
        qs =  Tweet.objects.all()
        # print (self.request.GET)    #dict with what we have searched  {'q':'search_text'}
        query = self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(Q(content__icontains=query) |
                         Q(user__username__icontains=query))
        paginator = Paginator(qs, 10) # Show 25 contacts per page
        page_request_var = "page"
        page = self.request.GET.get(page_request_var)
        try:
            qs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            qs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            qs = paginator.page(paginator.num_pages)
        return qs

    def get_context_data(self,*args,**kwargs):
        obj = super(TweetListView,self).get_context_data(*args,**kwargs)
        obj['create_form']  = TweetModelForm()
        obj['create_url']   = reverse_lazy('tweets_app:create')
        #print (obj)
        return obj



    # columns=[field.name for field in Tweet._meta.get_fields()]
    # print(columns)
    # obj=Tweet()
    # obj.content='Hello wvwry one'
    # obj.save()

class TweetDetailview(DetailView):
    queryset=Tweet.objects.all()
    template_name="tweets/detailed_view.html"
    # def get_object(self):
    #     print (self.kwargs)
    #     pk=self.kwargs.get("pk")
    #     print (pk)
    #     return Tweet.objects.get(id=pk)


class TweetCreateView(FormUserNeededMixin,LoginRequiredMixin,CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # If we are not redirecting output to any url it will user getabsoluteurl function defined in models
    # success_url='/tweet/create/'
    login_url = '/login/'
    success_url = '/'

class TweetUpdateView(LoginRequiredMixin,UpdateView):
    queryset=Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    success_url='/tweet/'

class TweetDeleteView(DeleteView):
    model = Tweet # or queryset=Tweet.objects.all()
    success_url=reverse_lazy("tweets_app:list")  #namespace : name
    template_name="tweets/delete_confirm.html"
