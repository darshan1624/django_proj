# django_proj
This is my new django proj.

1) created a icoder project 
2) created a new app blog 
3) created virtualvenv
4) installed a one new package pipdeptree, very useful for viewing packages in tree structure
5) created a new app home 
6) created simple url pipeline for both apps blog, home 
7) created templates, static folder. templates configuration done in settings.py. 
8) created simple html pages for all pages.
9) template inheritance. created base.html from which other pages will inherit. 
10) installed one amazing library "django" by bapsite dartenay 
11) Learned how to add .gitignore. If not ignoring files. first clear cache, delete files being tracked and commit then push. 
12) a) Created a contact form using bootstrap. 
    b) Created a model for the same. Added Time stamp fileds to contact model by inherting from another abstract model(model that doesnt have table) TimeStamp.  
    c) Registered app in settings installed apps. (other wise migration file wont be created).
    d) Register app in admin.py file. (so, that we can view model via admin page).
    e) written orm query in views.py. To add post data to table. 
13) created a dismissible prompt using bootstarp to show error/success/warning/info prompts.
    Used django message templates. 
14) Active(highlight) tab from breadcrumb when pressed.
15) Created a Home page (for home app) and blogHome (for blogapp). 
    Created a model Post which will store blog data. Register model in settings.py 
    Ftech data from db to Home and blogHome page.
16) Create admin pannel button on UI. Not necessary. 
    Created blogPost page. When we click on any block we go to that specific blogPost page. 
    Created search utility on UI. Copied blogPost html for search html page. 
    Used title__icontains = 'keyword' filter in ORM query to get required blogs.
17) Handled case when no blog is fetched via search or search query is too big. Implemented dismissible message. Include content__icontains = 'keyword'.  
18) Created signup, Login button in nav bar. Used bootstrap modal. Inside modal created form. 
19) Register user using signup. Used User model provided by django. Handled cases when user already exist and passwords (confirm - renter) donot match. 
20) Login user using login button. Used authenticate, login, logout functions provided by django. 
21) Disappear Login,Signup button when logged in. Used user.is_authenticated() to now if user is aunthenticated. 
    Created dropdown in navbar to see logout option. 
22) Customized Admin pannel little bit. Created a model BlogComments. User, Post field will be a foreign key and parent will be self foreign key. 
23) Created a comments section under blogpost. 
    Comments are realted to post, user, parent_comment(which means its a reply).
    Created a model BlogComment with sno, comment, post, user, parent, timestamp. 
    Written apis in views.py to fetch data from form (comment) and store it in model BlogComment.
    Created a form (comment) to add comments in blogPost page. Import fields include comment, hidden(sno of post), submit.

    Modified blogPost api to fetch comments of particular post. 
    Modified blogPost page to view all comments.
    Handled case when user is not autheticated to add comments. 
    humanized time e.g.: 2 days ago, 2 hours ago
    New things: Forignkey, anonomous user when user not aunthenticated.