import sys
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import mediainfo

def split_chunks(infile):
    current_track = AudioSegment.from_mp3(infile)
    original_bitrate = mediainfo(infile)['bit_rate']
    chunks = split_on_silence(current_track, min_silence_len=30, silence_thresh=-80)

    for i, chunk in enumerate(chunks):
        original_filename = os.path.split(infile)[1]
        original_path = os.path.split(infile)[0]
        outfile = "{} (Part {}).mp3".format(original_filename[:-4], i+1)
        chunk.export(os.path.join(original_path, outfile), format="mp3", bitrate=original_bitrate)
        print('exported chunk', outfile)

def split_dir(path):
    for fn in os.listdir(path):
        if fn.endswith("mp3") and "Part" not in fn and "part" not in fn:
            infile = os.path.join(path, fn)
            split_chunks(infile)

if __name__ == '__main__':
    path = sys.argv[1]
    split_dir(path)
            
