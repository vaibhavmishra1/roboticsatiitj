from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import IITJUser,Project,Feedback,IssueMaterial,MustKnowPeople,Messages
from .forms import RegistrationForm,ProjectCreateForm,FeedbackCreateForm,IssueCreateForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView
# Create your views here.
from django.http import HttpResponseRedirect



from django.urls import reverse_lazy

class HomeCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': FeedbackCreateForm()}
        return render(request, 'home/index.html', context)

    def post(self, request, *args, **kwargs):
        form = FeedbackCreateForm(request.POST)
        if form.is_valid():
        	feedback=Feedback()
        	feedback.description= form.cleaned_data.get('description')
        	feedback.user=request.user
        	feedback.save()
        	return HttpResponseRedirect(reverse_lazy('home'))
        return render(request,'home/index.html',{'form':form})


# class IssueCreateView(CreateView):
#     def get(self, request, *args, **kwargs):
#         context = {'form': IssueCreateForm()}
        
#         return render(request, 'issue.html', context)

#     def post(self, request, *args, **kwargs):
#         form = IssueCreateForm(request.POST)
        
#         if form.is_valid():
#             issuematerial=IssueMaterial()
#             issuematerial.description= form.cleaned_data.get('description')
#             issuematerial.user=request.user
#             issuematerial.save()
#             return HttpResponseRedirect(reverse_lazy('issue'))
#         return render(request,'issue.html',{'form':form})
#     def get_context_data(self,**kwargs):
#         ctx=super(IssueCreateView,self).get_context_data(**kwargs)
#         ctx['ids']=self.request.user.id
#         ctx['name']=self.request.user.username
#         ctx['materials']=IssueMaterial.objects.all()
#         return ctx
def IssueCreateView(request):
    materials=IssueMaterial.objects.filter(user=request.user)
    
    if request.method=='POST':
        form=IssueCreateForm(request.POST)
        if form.is_valid():
            material=IssueMaterial()
            material.item= form.cleaned_data.get('item')
            material.number= form.cleaned_data.get('number')
            material.provided=False
            material.user=request.user
            material.save()
            return HttpResponseRedirect("/issue/")
    else:
        form=IssueCreateForm()
    return render(request,'issue.html',{'form':form,'materials':materials})

def messagegiven(request):  
    if request.method == 'POST':
        form=Messages(request.POST)
        Material = Messages()
        Material.message = form.cleaned_data.get('message')
        Material.user=request.user
        Material.save()
        return HttpResponseRedirect("/")
    return redirect('/')        



class UserProfileView(UpdateView):
    model=IITJUser
    form_class=RegistrationForm
    template_name = 'registration.html'
    success_url=reverse_lazy('home')

class UserProjectsView(ListView):
	template_name="projects.html"
	ids=0
	name=""

	def get_queryset(self,**kwargs):
		ids=self.request.user.id
		name=self.request.user.username
		print("name=",name)
		print(ids)
		#return Project.objects.filter(id=ids)
		return Project.objects.all()
	def get_context_data(self,**kwargs):
		ctx=super(UserProjectsView,self).get_context_data(**kwargs)
		ctx['ids']=self.request.user.id
		ctx['name']=self.request.user.username
		return ctx


class GeneralProjectsView(ListView):
	template_name="projects_general.html"
	model=Project

class MustKnowView(ListView):
    template_name="mustknow.html"
    model=MustKnowPeople



def IssuedDelete(request, id):
    post = get_object_or_404(IssueMaterial, id=id)
    post.delete()
    return redirect('issue')

class ProjectCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ProjectCreateForm()}
        return render(request, 'addproject.html', context)

    def post(self, request, *args, **kwargs):
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            Project= form.save()
            Project.user=request.user
            Project.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'addproject.html', {'form': form})
        