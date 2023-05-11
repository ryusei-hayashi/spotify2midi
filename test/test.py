import spotify2midi

id = 'dcd3bbfb67b645c5a0a9c7568cbbc6dd' ### YOUR SPOTIFY ID ###
secret = '566145b7875649989721a1bed96bc315' ### YOUR SPOTIFY SECRET ###
s2m = spotify2midi.Spotify2Midi(id, secret)

url = 'https://open.spotify.com/track/5Yx45WDFNYLFwj3pjtvfJ6'
s2m.spotify2midi(url)