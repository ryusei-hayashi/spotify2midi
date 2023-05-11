# spotify2midi
This package creates MIDI file from Spotify URL using Get Track's Audio Analysis of [Spotify Web API](https://developer.spotify.com/documentation/web-api).

## Description
This package creates MIDI file from Spotify URL. For example, It creates [Twinkle Twinkle Little Star - Grand Piano Version.mid](https://github.com/ryusei-hayashi/spotify2midi/blob/main/test/Twinkle%20Twinkle%20Little%20Star%20-%20Grand%20Piano%20Version.mid) from [Twinkle Twinkle Little Star - Grand Piano Version](https://open.spotify.com/track/5Yx45WDFNYLFwj3pjtvfJ6). MIDI file is created in the current directory by get_midi method of Spotify2Midi object. get_midi method has seven arguments.

### get_midi
* url: Enter Spotify URL you want as the MIDI file.
* name: Enter MIDI file name. The default is the music name.
* path: Enter MIDI file directory. The default is the current directory.
* limit: Enter a natural number or real number between 0.0 and 1.0 to limit the number of notes to write to the MIDI file.
  * For a natural number, limit acts as Maximum Polyphony.
  * For a real number, limit acts as Pronunciation Probability Threshold.
* confidence: Enter a real number between 0.0 and 1.0 to limit the confidence of records to write to the MIDI file.
* base_note: Enter MIDI file base note as a natural number. The default is C4.
* offset: Enter MIDI file offset. The default is 0.

## Requirement
* [spotipy](https://spotipy.readthedocs.io)
* [numpy](https://numpy.org)
* [mido](https://mido.readthedocs.io)

## Install
```
pip install git+https://github.com/ryusei-hayashi/spotify2midi
```

## Usage
### Get Client ID and Client Secret
If you don't have Client ID and Client Secret, please refer to the following websites to get them.
* https://stevesie.com/docs/pages/spotify-client-id-secret-developer-api
* https://nao-y.hatenablog.com/entry/2019/01/18/013416

### Use spotify2midi
```
import spotify2midi
```
* Enter Client ID and Client Secret.
* Create instance of Spotify2Midi object.
```
id = ## Your Client ID ##
secret = ## Your Client Secert ##
s2m = spotify2midi.Spotify2Midi(id, secret)
```
* Enter Spotify URL.
* Get MIDI file.
```
url = ## Spotify URL ##
s2m.get_midi(url)
```

## Licence
[MIT license](https://en.wikipedia.org/wiki/MIT_License)
