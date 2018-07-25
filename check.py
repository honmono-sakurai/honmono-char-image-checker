from PIL import Image
import sys
sys.path.append('/path/to/dir')

import pyocr
import pyocr.builders

tls = pyocr.get_available_tls()
if len(tls) == 0:
    sys.exit(1)
    
tool = tls[0]
langage = tool.get_available_languages()
extracted_txt = tool.image_to_string(
    Image.open('target.png'),
    lang='jpn',
    builder=pyocr.builders.TextBuilder()
)

if 'sakurai'.count('サクライ') == 0:
    print('you are suck')
else:
    print('awesome!')
