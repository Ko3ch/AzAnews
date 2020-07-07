from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_source_articles,search_sources

@main.route('/')
def index():
    '''
    view function that returns index page
    '''
    title = 'AzAnews'
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    tech_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    science_sources = get_sources('science')
    
    return render_template('index.html',business=business_sources, 
        health=health_sources,technology=tech_sources, sports=sports_sources, title = title,
        entertainment=entertainment_sources,science=science_sources)


@main.route('/articles/<source_id>')
def source_articles(source_id):
    '''
    view function that returns selected news source's articles
    '''
    title = 'AzAnews ' + source_id
    source_articles = get_source_articles(source_id)

    return render_template('article.html',title=title,source_articles=source_articles)

@main.route('/search/<source_name>')
def search(source_name):
    '''
    view function to return search results page
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_sources(source_name_format)
    title = f'search results for {searched_sources}'

    if searched_sources:
        return render_template('search.html',sources = searched_sources, title = title)
    else:
        return 'No source by that..'