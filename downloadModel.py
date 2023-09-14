import gdown
from pyunpack import Archive

url = 'https://drive.google.com/file/d/1ukte8uX6GZuKAfBQWl8gWxB12Hq2vluA/view?usp=drive_link'
output = 'randomForestModel.7z'
gdown.download(url=url, output=output, quiet=False, fuzzy=True)
Archive('randomForestModel.7z').extractall("interfaz\IAB1_reto_int\modelInt")