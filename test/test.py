import spotify2midi

id = ## YOUR SPOTIFY ID ##
secret = ## YOUR SPOTIFY SECRET ##
s2m = spotify2midi.Spotify2Midi(id, secret)

url = 'https://open.spotify.com/track/5Yx45WDFNYLFwj3pjtvfJ6'
s2m.spotify2midi(url)
