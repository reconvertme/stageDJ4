from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from journaux.models import Journal

# # Create your views here.
# def listeJournaux(request):
#     # Ramener tous les journaux
#     journaux = Journal.objects.all() 
    
#     # request, template, objet contextuel (le 1er élément)
#     # return render(request, "journaux/home.html", {"journaux":journaux[0]}
#     # )
    
#     page_num = request.GET.get('page', 1)
#     paginator = Paginator(journaux, 2) # 2 journaux per page


#     try:
#         page_obj = paginator.page(page_num)
#     except PageNotAnInteger:
#         # if page is not an integer, deliver the first page
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         # if the page is out of range, deliver the last page
#         page_obj = paginator.page(paginator.num_pages)

#     # render(request, template, objet contextuel (tout))
#     # return render(request, "journaux/home.html", {"journaux":journaux}) 
#     return render(request, "journaux/home.html", {"page_obj":page_obj})

# Vue générique
from django.views.generic import ListView

class HomePageView(ListView):
	model = Journal
	context_object_name = 'page_obj'
	template_name = "journaux/home.html"


# PAGINATION AVEC UNE CLASSE
# from django.views.generic import ListView

# class HomePageView(ListView):
#     model = Journal
#     context_object_name = 'page_obj'
#     paginate_by = 1
#     template_name = "journaux/home.html"