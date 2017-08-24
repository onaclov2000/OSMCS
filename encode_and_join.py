import os
def filter_m4v(x):
    if 'm4v' in x[-3:]:
            return True
# Plop in directory containing all videos for a class (folders and then videos)
for dirs in sorted(os.listdir(".")):
   if os.path.isdir(dirs):
      os.chdir(dirs)
      # Interstingly I was just thinking about this today, one could set it up so that each video was in some x time chunks
      # Udacity doesn't split the videos into folders anymore which is super annoying.
      out = open('mylist.txt', 'w')
      for vids in sorted(os.listdir(".")):
         if '.mp4' in vids:
            # remove non alpha-numeric characters by renaming for easier joining.
            tmp = ''.join(e for e in vids[:-4] if e.isalnum())
            os.rename(vids, tmp + '.mp4')
            vids = tmp + '.mp4'
            out.write("file '" + vids[:-4] + ".m4v'\n")
            # if you don't need to re-encode just comment this line out, however
            # OFTEN times the framerates are all wonky and this makes them all 25 fps so the audio/video *should
            # Stay in sync, with no weird pausing, also due to timestamp issues, re-encoding is necessary
            # otherwise the vidoes would say crazy inaccurate numbers for length of video.
            os.system('ffmpeg -i \"' + vids + '\" -c:v mpeg4 -b:v 1800k -c:a copy -vsync 1 -r 25 \"' + vids[:-4] + '.m4v\"')
      
      out.close()
      os.system('ffmpeg -f concat -safe 0 -i mylist.txt -c copy \"../' + dirs + '.m4v\"')
      os.chdir('..')
    
