from django.http import request, response
from django.shortcuts import render, redirect, get_object_or_404
from . models import MovieInfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def create(request):
    #frm = MovieForm()
    #if request.POST:
    if request.method == 'POST':
        frm = MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
        frm = MovieForm()

        
        #movie_obj.save()
    return render(request, 'create.html',{'frm': frm})


@login_required(login_url='login/')
def list(request):
     #print(request.COOKIES)
     recent_visits = request.session.get('recent_visits', [])
     count=request.session.get('count', 0)
     #visits = int(request.COOKIES.get('visits', 0)) 
     count= int(count)
     count= count + 1
     request.session['count'] = count
     recent_movie_set= MovieInfo.objects.filter(pk__in=recent_visits)
     #visits += 1
     #movie_set=  MovieInfo.objects.all()
     #movie_set=  MovieInfo.objects.filter(year='2023',title='jailer')
     #movie_set=  MovieInfo.objects.filter(year='2023'
     #movie_set=  MovieInfo.objects.exclude(year='2023')
     #movie_set=  MovieInfo.objects.exclude(year='2023').order_by('-year')
     #movie_set=  MovieInfo.objects.filter(actors='Mohanlal').order_by('-year')
     #movie_set=  MovieInfo.objects.filter(year__gt='2023')
     movie_set=  MovieInfo.objects.all()
     #movie_set=  MovieInfo.objects.filter(title__startswith='j')
     #movie_set=  MovieInfo.objects.filter(actors__name='Mohanlal')
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
     response = render(request, 'list.html', { 'recent_movies': recent_movie_set, 'movies': movie_set, 'visits': count})
     #response = render(request, 'list.html', {'movies': movie_set, 'visits': count})
     #response.set_cookie('visits', visits)
     return response

def edit(request,pk):
    
    instance_to_be_edited= MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm = MovieForm(request.POST, instance=instance_to_be_edited)
        if frm.is_valid():
             instance_to_be_edited.save()
    else:
         recent_visits = request.session.get('recent_visits', [])
         recent_visits.insert(0, pk)
         request.session['recent_visits'] = recent_visits   
         frm = MovieForm(instance=instance_to_be_edited)
    #return render(request, 'edit.html')
    return render(request, 'create.html', {'frm': frm})

def delete(request,pk):
         instance= MovieInfo.objects.get(pk=pk)
         instance.delete()
         movie_set=  MovieInfo.objects.all()
         print(movie_set)
         return render(request, 'list.html', {'movies': movie_set})