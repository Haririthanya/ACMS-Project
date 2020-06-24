# ACMS-Project

Personalized artwork based on user preference.

Based on user's preference display images that are close to what the user like in terms of genre.
The front end is developed using Python's Flaskvmicroframework and ML model is a CNN.

For the demonstartion purpose , I've chosen three genre - DRAMA,ACTION,THRILLER

Intially the images are classified using the ml model and stored in their respective csv files. Eg. The images to be displayed in books category is classifed and the images score for the three genre is stored in book.csv .
 
 The users.csv contains the score of prefered genre of each user.

File hierarchy:
static
  |_images
  |_css
  |_env
app.py
book.csv
magazine.csv
users.csv

![URL](https://github.com/Haririthanya/ACMS-Project/blob/master/url.png) 

Once this is entered you can see the newspaper page.

![Newspaper](https://github.com/Haririthanya/ACMS-Project/blob/master/newspaper.png)

## Changing the user id to u002 will display another image which is based on the user preference.

![Newspaper-another user]()
