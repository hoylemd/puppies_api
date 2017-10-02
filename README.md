Read me!

Requirements
------------
python-virtualenvwrapper
You can probably get this fom your package manager(brew, apt-get, yum, etc)

Installation
------------
`mkvirtualenv puppies`
`workon puppies`
`pip install -r requirements.txt`
`./manage.py migrate`
`./manage.py createsuperuser`  And follow the instructions

Running
-------
`./manage.py runserver`

Testing
-------
'./manage.py test'

Demo Scripts
------------
create_user.sh: Demonstrates how to sign up a new user (run this first!)
create_post.sh: Demonstrates how to create a new post (run this second!)
list_users.sh: Demonstrates how to get a list of all users
user_profile.sh: Demonstrates how to get a user's profile
feed.sh: Demonstrates how to get the Feed (reverse-chonological order of all posts)
post_details.sh: Demonstrated how to get the details of a post
users_posts: Demonstrates how to get a list of a users' posts

Highlights
----------
The two largest problems I had to solve were handling the password field on the
User model and the owner field on the Puppy model.

Password was a challenge because I didn't want that field to be echo'd back or
to be editable in any way.  By default, if a field is included in a serializer,
it's included in GET responses.  I searched for posts on the internet about
solving similar problems, and chose my favourite.  In UserSerializer, I overrode
the `create` method to first create a user record with no password, and then
immediately used the `User.set_password` method to set the password as provided.
(The django `User.password` field actually stores a hash of the password, so
without manually hashingit first, it can't be set directly.  Also, a method
exists for this specific use case, so no point reinventing the wheel!).  I also
specified that the password field was 'write-only' in the serializer.  That
made sure it would never be included in a response request.

As for `Puppy.owner`, the challenge was that I didn't want to require that the
client identify themselves in the payload of the creation request, as that
information should be sourced from the context of the request. Unfortunately,
the `owner` field had to be a required field in the domain model, so validation
of the payload would fail. Luckily, I've done this  exact thing in the past, so
I was able to call upn my own experience. As with `User.password`, the solution
was to override the `create` method in the UserSerializer to populate that field
just as the record was created in the database. The `owner=` line pulls the user
from the request context, not the validated data.  Specifying `owner` as a read
only field took care of failing validation as well.

Limitations
-----------
I didn't go very deep into things like pagination or advanced authentication.
In a real project, these would be high priorities, but as this is a small toy
project, I decided to focus my efforts on the core functionality.  As a result,
pagination is hard-coded to 10 records / request (though to be fully honest,
I didn't test the pagination at all).

I also put more effort into the demo scripts than I did the actual tests, so
`tests.py` might seem a little light. I chose to do this because Django
Rest Framework (and Django itself) takes care of a lot of the fine detail of
the api, so a lot of tests would have simply been verifying the library
functionality.  That's not a good use of testing resources, as test coverage
is generally considered an important consideration when selecting a library
or framework.

I didn't implement the 'Like' feature at all. I already had most of the other
features done, and the requirements document said that only 4-5 were needed.
I mentally designed how it would work, so I can explain that if needed.

Lastly, I'm a little dissapointed with how unexpressive the code ended up.
Django Rest Framework provides so much 'for free', that following best
practices on minor projects tends to hide the interesting bits.  For example,
I only defined 2 individual views, yet something on the order of 16 exist.

