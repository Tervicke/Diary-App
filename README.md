# Diary-App
![screenshot](screenshot.jpg)
A simple python app that helps me maintain and write a diary . 
I wrote a blog about this app you can find it [here](https://tervicke.netlify.app/blogs/coding-a-app-to-help-me-maintain-a-diary.html)
## basics of this app
clone the repo and place the ```app.py``` file somewhere you would want to store your files for eg I keep app.py in ~/Diary
when you open the app it will open the current Diary entry , write your diary and save the file by either pressing the save button on the right hand side or pressing the Ctrl+s shortcut, this will turn the text grey indicating that the diary entry is saved  note: this will a create a file a file namely thedate-month-year.text in the directory you have the app.py therefore i said to place the file somewhere you would want to keep all your Diary entries .
## move / select other diary entrys
if you want to view previous diary entries / some specific entry you can select the particular date from the calendar given on the right side and clicking the select button or if you want to move to the prvious entry or the next one there are buttons for it on the right hand top . note: to this you would need to save the current file or it wont work . once you saved the file you can use the buttons on the top or even the arrow keys on the keyboard to move to next or previous diary entry's .if you want to edit today's diary entry again you do that by pressing ctrl+e or clicking edit todays button 
## Search for a sentence/word in your whole diary 
Note : this uses the grep command so its usable only in linux and mac idk about windows .
you can enter the text you want to search in the text field below the search in your diary label and after pressing enter the text box below it should be filled with the dates of the diary entry where the word/sentence was found you can manually select the date or copy the date you want and paste in the text above text field which is next to the back and next button on the top and press enter to open that diary entry  
