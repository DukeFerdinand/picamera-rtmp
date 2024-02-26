import time

from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2

# Video Parameters
resolution = (1920, 1080)

picam2 = Picamera2()
#video_config = picam2.create_video_configuration(main={"size": resolution})
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder()
output = FfmpegOutput("-c:v copy -f flv -flvflags no_duration_filesize rtmp://192.168.4.79/live/picamera")
# output = FfmpegOutput("-f flv rtmp://192.168.4.79/live/picamera")


if __name__ == "__main__":
    try:
        print("Starting RTMP stream!")
        print(encoder.bitrate)

        picam2.start_recording(encoder=encoder, output=output, quality=Quality.VERY_HIGH)
        while True:
            print("recording is active...")
            time.sleep(5)
    except Exception as e:
        print(e)
        picam2.stop_recording()
