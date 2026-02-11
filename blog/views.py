from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Fulvio",
        "date": date(2026, 2, 2),
        "title": "Mountain Hiking",
        "excerpt": '''There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!''',
        "content": '''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quos alias ullam, voluptatibus odio itaque nostrum voluptate ad rerum laborum accusantium accusamus consequuntur eaque voluptatem sit, provident culpa natus deleniti cupiditate?'''
    },
    {
        "slug": "forest-adventure",
        "image": "forest.jpg",
        "author": "Ana",
        "date": date(2026, 1, 20),
        "title": "Forest Adventure",
        "excerpt": '''Dense trees, winding trails and the sound of birds — a forest walk to remember.''',
        "content": '''Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Integer sit amet eros non lacus vulputate convallis. Duis in urna sit amet lacus tincidunt tincidunt.'''
    },
    {
        "slug": "city-walks",
        "image": "city.jpg",
        "author": "Miguel",
        "date": date(2026, 1, 10),
        "title": "City Walks",
        "excerpt": '''Exploring alleys, cafes and street art — the city has stories on every corner.''',
        "content": '''Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Pellentesque in ipsum id orci porta dapibus.'''
    }
]


def get_date(post):
    return post.get('date')


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_details(request, slug):
    return render(request, "blog/post-details.html")
