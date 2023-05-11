import spotipy
import numpy
import mido

class Spotify2Midi:
    def __init__(self, id, secret, ticks_per_beat=480):
        self.set_spotify(id, secret)
        self.ticks_per_beat = ticks_per_beat

    def set_spotify(self, id, secret):
        ccm = spotipy.oauth2.SpotifyClientCredentials(client_id=id, client_secret=secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=ccm)
        return self.spotify

    def loudness2velocity(self, loudness, l_min=-60, l_max=0, v_min=1, v_max=126):
        velocity = round((loudness - l_min) * (v_min - v_max) / (l_min - l_max) + v_min)
        return velocity

    def second2time(self, second, tempo):
        time = round(mido.second2tick(second, self.ticks_per_beat, tempo))
        return time

    def get_midi(self, url, name='', path='./', limit=1, confidence=0.5, base_note=60, offset=0):
        print('Get Audio Analysis')
        name = self.spotify.track(url)['name'] if name == '' else name
        analysis = self.spotify.audio_analysis(url)
        tempo = mido.bpm2tempo(analysis['track']['tempo'])
        track = mido.MidiTrack()
        track.append(mido.MetaMessage('set_tempo', tempo=tempo))

        if type(limit) == int:
            print('Create Track by Maximum Polyphony')
            for a in analysis['segments']:
                if confidence < a['confidence']:
                    notes = numpy.asarray(a['pitches']).argsort()[::-1][:limit]
                    if 0 < len(notes):
                        for i in range(len(notes)):
                            track.append(mido.Message('note_on', channel=0, note=notes[i]+base_note, velocity=self.loudness2velocity(a['loudness_max']), time=0 if 0 < i else self.second2time(a['start']-offset, tempo)))
                        for i in range(len(notes)):
                            track.append(mido.Message('note_off', channel=0, note=notes[i]+base_note, time=0 if 0 < i else self.second2time(a['duration'], tempo)))
                        offset = a['start'] + a['duration']
        elif type(limit) == float:
            print('Create Track by Pronunciation Probability')
            for a in analysis['segments']:
                if confidence < a['confidence']:
                    notes = numpy.where(limit < numpy.asarray(a['pitches']))[0]
                    if 0 < len(notes):
                        for i in range(len(notes)):
                            track.append(mido.Message('note_on', channel=0, note=notes[i]+base_note, velocity=self.loudness2velocity(a['loudness_max']), time=0 if 0 < i else self.second2time(a['start']-offset, tempo)))
                        for i in range(len(notes)):
                            track.append(mido.Message('note_off', channel=0, note=notes[i]+base_note, time=0 if 0 < i else self.second2time(a['duration'], tempo)))
                        offset = a['start'] + a['duration']
        else:
            print('\033[91mTypeError\033[0m: limit type must be int or float')
            return

        print(f'Create {name}.mid')
        mid = mido.MidiFile(ticks_per_beat=self.ticks_per_beat)
        mid.tracks.append(track)
        mid.save(f'{path}{name}.mid')

    def wakka(self):
        print('なんで寺院に機械があんだよ\n教えはどうなってんだ教えは\nお前ら禁じられた機械を平気で使ってんじゃねえか\n分かってんのか！？\n「シン」が生まれたのは人間が機械に甘えたせいだろうが\n金取んのかよ！？\nくそったれ！')
