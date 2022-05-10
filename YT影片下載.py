from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=U4PWWK6ySeQ&list=PLLs_bviwxqA5LCQkBlalzao2T6xNaghea&index=6')
(yt.streams
.filter(progressive=True, file_extension='mp4')
.order_by('resolution')
.desc()
.first()
.download())

print("Finish!!")