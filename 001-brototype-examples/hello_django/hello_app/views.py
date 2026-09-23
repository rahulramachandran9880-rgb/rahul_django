from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def print_hello(request):

    #movie_details = {
     #   'title': 'The Shawshank Redemption',
      #  'summary': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
       # 'year': 1994,
        #'success': True
    #}

    movie_data= {
        'movies' :[
            {
                'title': 'The Shawshank Redemption',
                #'summary': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'year': 1994,
                'success': False
            },
            {
                'title': 'titanic',
                'summary': 'love story.',
                'year': 1990,
                'success': True
            },
            {
                'title': 'Godfather',
                'summary': 'gangster movie',
                'year': 1996,
                'success': False
            },

            {
                'title': 'Into the wild',
                'summary': 'adventure movie',
                'year': 1998,
                'success': False
            }

        ]
    }
    #return HttpResponse("<b>Hello Django</b>")
    return render(request, 'hello.html', movie_data)

