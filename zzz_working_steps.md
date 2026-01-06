Here i will write the steps i am following in my webapp.

1. 
```
How are you, <u>{{ user_name or "Guest User (Login to view your name)"}}</u>? 😊
```
I will use the or to get the value of the variable in the jinja.

2.
I will use a macro function so that i can use it to generate the navbar for now?
I will also use the table and it will come from the macro.

3. 
https://tedboy.github.io/jinja2/templ11.html
This website help to get some idea about the jinja things.

4. I will make blueprint for which i need to make different folders and inside this i need to make routes.py and own things maybe.

5. I found when working with sqlite3 > sqlmodel when having the username column as unique = true, the null values so i will do for now unique = false and on adding new user first it will check of username already present or not?

6. In the place of when in admin blueprint i enter the username in the field and then it send the html and refresh it cause resubmit, so i will need to make, `POST → redirect → GET`, that's why i will need to make a url like get to fetch the username field. and after the post i will redirect.

7. i need to work on the admin blueprints or maybe others places so that in flash() i can shows html things?

8. ONe question i am confused that i want to mark the navbar tab shows active when i am in this tab? i will do it in python check or in js i am in little confused?

