from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import shutil
import sys

app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True
app.config['FOLDER_PATH'] = ""


@app.route("/")
def index():
    compare_images = []
    print(app.config['FOLDER_PATH'])
    folder_path = app.config['FOLDER_PATH']
    for file in os.listdir(folder_path):
        compare_images.append(file)
        shutil.copy(os.path.join(folder_path, file), 'static/images')
    images = compare_images
    return render_template('index.html', images=images)


if __name__ == "__main__":
    app.config['FOLDER_PATH'] = sys.argv[1]
    app.run()
