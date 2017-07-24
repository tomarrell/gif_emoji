# gif_emoji
Turn images into animated rotating gifs.

## Usage
`python ./makeGif.py [PathToImage]`

## Output
![](http://imgur.com/download/xLj8ljQ)

A single gif output, `output.gif` is produced in local directory. 

Currently the output is fixed to a `32x32` GIF with `36 frames` rotated by `10˚` each. This produces GIFs that are below the 60kB filesize limit imposed by the custom emoji upload for Slack.

This was written to automatically generate rotating animations of people for use as Slack emojis. More info about custom Slack emojis here: https://get.slack.help/hc/en-us/articles/206870177-Create-custom-emoji.
