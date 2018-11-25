import requests, shutil
import os
import traceback


def get_extension(filepath):
    ext_place = filepath.rfind('.')
    if ext_place == -1:
        return ''
    return filepath[ext_place:]


_file_urls = open('litter_synset.txt', 'r')
if not os.path.isdir(os.path.curdir + '/images'):
    os.mkdir(os.path.curdir + '/images')
chunksize = 10
template_remove = open('litter_synset.txt', 'rb')
for i, line in enumerate(_file_urls):
    line = line[:-1]
    filereq = None
    try:
        filereq = requests.get(line, stream=True)
        filename = os.path.curdir + '/images/litter_' + str(i) + get_extension(line)
        with open(filename, "wb") as receive:
            if template_remove != filereq.raw:
                shutil.copyfileobj(filereq.raw, receive)
            else:
                print('skipped non-existing photo')
    except Exception:
        print(traceback.print_exc())
    finally:
        del filereq
        if (i + 1) % chunksize == 0:
            print('Processed %d files' % (i + 1))
