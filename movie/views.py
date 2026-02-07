from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# HOME
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


# ABOUT
def about(request):
    return render(request, 'about.html')


# MOVIES LIST + SEARCH
def movies(request):
    query = request.GET.get('q')

    if query:
        results = Movie.objects.filter(title__icontains=query)

        # Si solo hay una película, redirigir a su detalle
        if results.count() == 1:
            return redirect('movie_detail', id=results.first().id)

        # Si hay varias, mostrarlas
        return render(request, 'movies.html', {
            'movies': results,
            'query': query
        })

    # Si no hay búsqueda, mostrar todas
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})



# MOVIE DETAIL + REVIEWS
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    reviews = Review.objects.filter(movie=movie)

    if request.method == 'POST':
        Review.objects.create(
            movie=movie,
            author=request.POST['author'],
            content=request.POST['content']
        )
        return redirect('movie_detail', id=id)

    return render(
        request,
        'movie_detail.html',
        {
            'movie': movie,
            'reviews': reviews
        }
    )


# DELETE REVIEW
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    movie_id = review.movie.id
    review.delete()
    return redirect('movie_detail', id=movie_id)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
