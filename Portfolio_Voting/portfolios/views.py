from .models import Work
from django.shortcuts import render

# Create your views here.
def index(request):
	'''
	### TESTING: 傳遞 session ###
	print("app: PORTFOLIOS ->", request.session['USER_INPUT_DEPARTMENT'])
	'''
	return render(request, 'portfolios/index.html')

def article(request, id):
	work = Work.objects.get(id=id)

	return render(request, 'portfolios/article.html', { 'work': work })