from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

def create(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('summary')
        #print(request.POST.get('title'))
        #print(request.POST.get('year'))
        print(request.POST.get('summary'))
        movie_obj = MovieInfo(title=title,year=year,description=desc)
        movie_obj.save()
    return render(request, 'create.html')

def list(request):
     movie_set=  MovieInfo.objects.all()
     print(movie_set)
    #  movie_data= {
    #         'movies' :[
    #             {
    #                 'title': 'The Shawshank Redemption',
    #                 #'summary': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    #                 'year': 1994,
    #                 'success': False,
    #                 'img': 'swawshankredumption.jpeg'
    #             },
    #             {
    #                 'title': 'titanic',
    #                 'summary': 'love story.',
    #                 'year': 1990,
    #                 'success': True,
    #                 'img': 'titanic.jpeg'

    #             },
    #             {
    #                 'title': 'Godfather',
    #                 'summary': 'gangster movie',
    #                 'year': 1996,
    #                 'success': False,
    #                 'img': 'godfather.jpeg'
    #             },
    
    #             {
    #                 'title': 'Into the wild',
    #                 'summary': 'adventure movie',
    #                 'year': 1998,
    #                 'success': False,
    #                 'img': 'intothewild.jpeg'
    #             }
    
    #         ]
    #     }
     #return render(request, 'list.html',movie_data)
     return render(request, 'list.html', {'movies': movie_set})

def edit(request):
    return render(request, 'edit.html')