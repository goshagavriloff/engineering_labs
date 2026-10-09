from pydub import AudioSegment
from pydub.playback import play

def quest_2(track1_name,track2_name):
    track1 = AudioSegment.from_file(track1_name)
    track2 = AudioSegment.from_file(track2_name)
    combined_track = track1 + track2

    print("Воспроизведение объединенной дорожки...")
    play(combined_track)


    start_time = 0
    end_time = 5000
    trimmed_track = track1[start_time:end_time]

    trimmed_track.export("trimmed_output.wav", format="wav")
    print("Фрагмент успешно вырезан и сохранен как 'trimmed_output.wav'")