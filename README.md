# spotify2midi
This package creates MIDI file from Spotify URL using Get Track's Audio Analysis of [Spotify Web API](https://developer.spotify.com/documentation/web-api).

## Description
This package creates MIDI file from Spotify URL. For example, the package create [Twinkle Twinkle Little Star - Grand Piano Version.mid]() from [Twinkle Twinkle Little Star - Grand Piano Version](https://open.spotify.com/track/5Yx45WDFNYLFwj3pjtvfJ6). MIDI file is created by get_midi method of Spotify2Midi object. get_midi method has 7 arguments.
* url: Enter the Spotify URL of the music you want as a MIDI file.
* name: Enter the name of the MIDI file. Default is music name.
* path: Enter the directory where MIDI file is saved. Default is the current directory.
* limit: Enter natural number or real number between 0.0 and 1.0 to limit the number of notes to write to MIDI file.
  * For natural number, limit acts as Maximum Polyphony.
  * For real number, limit acts as Pronunciation Probability.
* confidence: 

## Requirement
* [spotipy](https://spotipy.readthedocs.io/)
* [numpy](https://numpy.org/)
* [mido](https://mido.readthedocs.io/)

## Install
```
pip install git+https://github.com/ryusei-hayashi/spotify2midi/
```

## Usage

```
import spotify2midi
```

```
id = ## Your Client ID ##
secret = ## Your Client Secert ##
s2m = spotify2midi.Spotify2Midi(id, secret)
```

```
url = 'https://open.spotify.com/track/5Yx45WDFNYLFwj3pjtvfJ6'
s2m.get_midi(url)
```

## Licence
[MIT license](https://en.wikipedia.org/wiki/MIT_License)
