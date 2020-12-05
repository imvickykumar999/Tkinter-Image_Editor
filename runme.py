import urllib.request, os

url = "https://github.com/imvickykumar999/Tkinter-Image_Editor/raw/main/image%20editor/editor.py"
pyfile = 'editor.py'

if not os.path.exists(pyfile):
    web_file = urllib.request.urlopen(url)
    file = open(pyfile,'w')

    for line in web_file:
        decoded_line = line.decode("utf-8")

        # print(decoded_line)
        file.write(f'{decoded_line}')
    file.close()

with open('README.md', "w") as f:
  f.write(f'''
  # Tkinter-Image_Editor
  ### Horizontal Eye Alignment

  [![screenshot.png](screenshot.png)]({url})
  ''')

os.system(f'py {pyfile}')
