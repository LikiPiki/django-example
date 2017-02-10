from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth import authenticate, login, logout

from models import Post, Comment
from .forms import CommentForm, UserForm, UserLoginForm, AddMemeForm

class Lenta(View):
	model = Post

	def get(self, request, *args, **kwargs):
		context = {}
		context['posts'] = Post.objects.all()[:20:-1]
		return render(request, "index.html", context=context)

class ViewMemeDetail(DetailView):
	model = Post
	template_name = "showMem.html"
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super(ViewMemeDetail, self).get_context_data(**kwargs)
		context['form'] = CommentForm
		context['comments'] = Comment.objects.filter(post_id=kwargs['object'].id)
		return context

	def post(self, request, pk):
		form = CommentForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.comment_name = request.user.username
			instance.post_id_id = pk
			instance.save()
		return redirect('/blog/showmem/' + pk)
		

class Register(View):
	form_class = UserForm

	def get(self, request, *args, **kwargs):
		context = {}
		form = UserForm()
		context['form'] = form
		return render(request, "register.html", context=context)

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/blog')
		return render(request, self.template_name, {'form': form})

class LoginFormView(View):
	form_class = UserLoginForm
	template_name = 'login.html'

	def get(self, request):
		form = UserLoginForm()
		context = {}
		context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST)
		context = {}
		context['form'] = form
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/blog')

		return render(request, self.template_name, context)

class AddNewMeme(View):
	form_class = AddMemeForm
	template_name = 'addNewMeme.html'

	def get(self, request):
		context = {}
		form = AddMemeForm()
		context['form'] = form
		return render(request, self.template_name, context=context)

	def post(self, request):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user.username
			instance.save()
		else:
			print "Check it"
		return redirect('/blog/addnewmeme')

class AddLike(View):
	def get(self, request, pk):
		curPost = Post.objects.get(id=pk)
		curPost.likes += 1
		curPost.save()
		return redirect('/blog/showmem/' + pk)


class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect('/blog')
