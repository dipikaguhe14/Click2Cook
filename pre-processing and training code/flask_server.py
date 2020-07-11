import flask
import werkzeug
import time
import sys
import subprocess

app = flask.Flask(__name__)
data_dir = 'C:\\Users\\Dell\\Desktop\\clg_docs\\Projects\\fyp\\codecon\\data\\'
@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save(data_dir+timestr+'_'+filename)
        image_num = image_num + 1
    print("\n one more"+timestr+'_'+filename)
    imgwtimestamp=timestr+'_'+filename

    output=subprocess.run('python demo.py '+imgwtimestamp,shell=True,stdout=subprocess.PIPE,text=True)
    print(output.stdout)
    return(output.stdout)


app.run(host="192.168.43.223", port=5000, debug=True)
