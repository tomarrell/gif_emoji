# gif_emoji
Turn images into animated rotating gifs.

## Dependencies
This package depends on the Python image library [Pillow](https://pillow.readthedocs.io/en/5.0.0/installation.html).

```pip install Pillow``` 

Please make sure you have the required dependencies above installed before using the library.

## Usage
`python ./makeGif.py [PathToImage]`

The image will be automatically cropped to a square based on the smallest dimension in the horizontal or vertical direction. For best results, have the subject of the image in the center of the smallest-dimension-cropped-square from the top-left corner.

## Output
![](http://imgur.com/download/xLj8ljQ)

A single gif output, `output.gif` is produced in local directory. 

Currently the output is fixed to a `32x32` GIF with `36 frames` rotated by `10˚` each. This produces GIFs that are below the 60kB filesize limit imposed by the custom emoji upload for Slack.

This was written to automatically generate rotating animations of people for use as Slack emojis. More info about custom Slack emojis here: 

https://get.slack.help/hc/en-us/articles/206870177-Create-custom-emoji.

## License
Licensed under the MIT license. Free for personal, commercial and derivative works.
