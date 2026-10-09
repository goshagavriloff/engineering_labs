from moviepy import VideoFileClip, AudioFileClip

def quest_3(video_path, audio_path):
    output_path="result.mp4"
    try:
        print(f"Загрузка видео: {video_path}")
        video = VideoFileClip(video_path)
        
        print(f"Загрузка аудио: {audio_path}")
        audio = AudioFileClip(audio_path)
        
        print("Объединение дорожек...")
        final_video = video.with_audio(audio)
        
        print(f"Сохранение итогового видео в: {output_path}")
        final_video.write_videofile(
            output_path, 
            codec="libx264", 
            audio_codec="aac"
        )
        video.close()
        audio.close()
        final_video.close()
        print("Готово! Видео успешно сохранено.")
        
    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")