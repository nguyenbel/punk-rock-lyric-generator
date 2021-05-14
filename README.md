# Punk Rock Lyric Generator
<center><img src = "https://images-na.ssl-images-amazon.com/images/I/71tgC6Xz7JL._SY800_.jpg" width = 500>
<br>
    <font size = 1.5>Image from: <a href = 'https://www.amazon.com/Rock-Robotic-Steampunk-Print-Decor/dp/B08F93NYF5'>https://www.amazon.com/Rock-Robotic-Steampunk-Print-Decor/dp/B08F93NYF5</a>
</center></font>

## Using LSTM (Long Short-Term Memory) to Create a Lyric Generator for Punk Rock Music
The idea for this project is to create a lyric generator based off of  punk rock music. The Long Short-Term Memory neural network trained on a set of punk rock artists from the AZ Song Lyrics Dataset found on <a href = 'https://www.kaggle.com/albertsuarez/azlyrics'>Kaggle</a>.

Due to the size of the procject, the LSTM can only write lyrics in the style of the following artists:


### Background Information



### The Model
The LSTM model takes in two inputs: the song lyrics and the respective artist of the song. 

In order for the model to take these two inputs, for the lyrics, we first tokenize the lyrics columns of the dataframe and fit the string version of each song to the text, then convert the tokenized text to a sequence, and, finally, created an n-gram padded sequence for each song (length of 11). For the artists, we stripped the white spaces for each artist/band so they were read as a single string, tokenized and fit the artists to the text, and, finally, converted the tokenized text to a sequence and appended that to a list which we later changed to a Numpy array.


### Results



### Conclusion
Transfer learning is a powerful tool and extremely useful tool and baseline when building an image processing convolutional neural network. Although the models were not as accurate as I wanted them to be, I believe they still performed well given the task at hand. The biggest take away I had from this project was lighting and angles of images make a difference. If possible, when building a model, make sure to distort images (e.g. change lighting using contrast and brightness, different angles for pictures, etc.) during training so the model can, potentially, have more accurate predictions during testing.

### Future Direction
- Add more bands to the last embedding layer
- Allow for different genres

### References
[1] https://www.kaggle.com/albertsuarez/azlyrics

[2] https://levelup.gitconnected.com/lyrics-generation-using-lstm-5a5a0bcac4fa

[3] https://www.pyimagesearch.com/2019/02/04/keras-multiple-inputs-and-mixed-data/