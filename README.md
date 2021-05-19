# Punk Rock Lyric Generator
## Using LSTM (Long Short-Term Memory) to Create a Lyric Generator for Punk Rock Music
### by Belinda Nguyen
[Linkedin](https://www.linkedin.com/in/bnguyen05/) * [Github](https://github.com/nguyenbel) * [Slides](https://github.com/nguyenbel/punk-rock-lyric-generator/blob/master/punk_rock_generator_presentation)

<center><img src = "https://images-na.ssl-images-amazon.com/images/I/71tgC6Xz7JL._SY800_.jpg" width = 300, class = 'center'>
<br>
    <font size = 1.5>Image from: <a href = 'https://www.amazon.com/Rock-Robotic-Steampunk-Print-Decor/dp/B08F93NYF5'>https://www.amazon.com/Rock-Robotic-Steampunk-Print-Decor/dp/B08F93NYF5</a>
</center></font>

## Using LSTM (Long Short-Term Memory) to Create a Lyric Generator for Punk Rock Music
### Background Information
The idea for this project is to create a lyric generator based off of  punk rock music. The Long Short-Term Memory neural network trained on a set of punk rock artists from the AZ Song Lyrics Dataset found on <a href = 'https://www.kaggle.com/albertsuarez/azlyrics'>Kaggle</a>.

The LSTM can write lyrics in the style of the following 15 artists:
        
- All Time Low
- Dashboard Confessional
- A Day to Remember
- Good Charlotte
- Green Day
- Jimmy Eat World
- The Menzingers
- My Chemical Romance
- Paramore
- Simple Plan
- State Champs
- Story of the Year
- The Story So Far
- Taking Back Sunday
- Yellowcard


### The Model
The LSTM model takes in two inputs: the song lyrics and the respective artist of the song. 

In order for the model to take these two inputs, for the lyrics, we first tokenize the lyrics columns of the dataframe and fit the string version of each song to the text, then convert the tokenized text to a sequence, and, finally, created an n-gram padded sequence for each song (length of 11). For the artists, we stripped the white spaces for each artist/band so they were read as a single string, tokenized and fit the artists to the text, and, finally, converted the tokenized text to a sequence and appended that to a list which we later changed to a Numpy array.


### Results
<img src = "https://github.com/nguyenbel/punk-rock-lyric-generator/blob/main/imgs/loss_v_acc.png">


### Conclusion


### Future Direction
- Refine model
    - Make outputs more currated to the artist whose writing style we are supposed to immitate
- Add more artists and song lyrics

### References
[1] https://www.kaggle.com/albertsuarez/azlyrics

[2] https://levelup.gitconnected.com/lyrics-generation-using-lstm-5a5a0bcac4fa

[3] https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/