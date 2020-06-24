# ACMS-Project

Personalized artwork based on user preference.

Based on user's preference display images that are close to what the user like in terms of genre.
The front end is developed using Python's Flaskvmicroframework and ML model is a CNN.

For the demonstartion purpose , I've chosen three genre - DRAMA,ACTION,THRILLER

Intially the images are classified using the ml model (ml.py uses tensorflow backend)  and stored in their respective csv files. Eg. The images to be displayed in books category is classifed and the images score for the three genre is stored in book.csv .
 
 The users.csv contains the score of prefered genre of each user.

File hierarchy:
static
  |_images_
  |_css_
  |_env_
app.py
book.csv
magazine.csv
users.csv

# Newspaper

![URL](https://github.com/Haririthanya/ACMS-Project/blob/master/url.png) 

Once this is entered you can see the newspaper page.

![Newspaper](https://github.com/Haririthanya/ACMS-Project/blob/master/newspaper.png)

## Changing the user id to u004 will display another image which is based on the user preference.

![Newspaper-another user](https://github.com/Haririthanya/ACMS-Project/blob/master/newspaper2.png)

Moving on to checking the books category, Here I have chosen two books - The DaVinci Code and The Famous Five.
Each book has 4 images.

# Books

In the same way, we change the url for books.
![URL](https://github.com/Haririthanya/ACMS-Project/blob/master/book%20url.png)

Here u004 is chosen
![Book](https://github.com/Haririthanya/ACMS-Project/blob/master/book.png)

Now changing the user , we get a different image .

![Book2](https://github.com/Haririthanya/ACMS-Project/blob/master/book2.png)
