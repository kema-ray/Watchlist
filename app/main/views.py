from flask import redirect, render_template, request, url_for
from app import app
from . import main
from app.main.forms import ReviewFom #from app import rachel
from ..request import get_movies,get_movie,search_movie
from ..models import Review

# Review = reviews.Review

#views
@main.route('/') #localhost 5000 e.g rachel.route
def index():

    '''
    View root page function that returns the index page and its data
    '''
#Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
@main.route('/movie/<int:id>')
def movie(id):
    '''
    View root page function that returns the index page and its data
    '''
    # title = f"Hello"
    movie = get_movie(id)
    reviews = Review.get_reviews(movie.id)
    # title = f'{movie.title}'
    return render_template('movie.html',movie=movie,reviews=reviews)
@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    # title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)

@main.route('/movie/review/new/<int:id>',methods = ['GET','POST'])
def new_review(id):
    form = ReviewFom()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    # title = f'{movie.title} review'
    return render_template('new_review.html',review_form=form, movie=movie)

