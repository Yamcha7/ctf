Hidden treasure 
------------------------
the patterns wre given 

Put them each in google map and we get a latitude and longitude 
Then we convert the latitude and longitude to asciii

We get the flag 

--------------------------------------

Secret admin 
-------------------------

We had a page with an error and the error said could not secret parameter 

The error seemed like to be a php lfi error and whatever was entered into the secret payload was reflected on the page 

We could also execute a reflected xss . 

Now we knew admin would visit this page . 

So we made a stored xss that would on opening the page send cookies to our server 

In this way when admin visits the page , we get to see the admin's cookies , where lies the flag . 



