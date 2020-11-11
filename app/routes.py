from app.detection.mrz import Mrz
from app.detection.credit_card import  Credit_card
from app.config import Config
from app import app
import os
import glob
from flask import Flask, flash, render_template, request, redirect, url_for, session

@app.route('/', methods=['GET', 'POST'])
def upload():
    #Clear the data in the session
    session.clear()
    # Clean the folder where i upload file
    test = 'app/detection/upload/*'
    r = glob.glob(test)
    for i in r:
        os.remove(i)

    if request.method == 'POST':
        uploaded_file = request.files['file']
        #Checking if the file is not empty
        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
            #Checking if the file is in the right format before uploading and saving it in the application server
            if file_ext in Config.UPLOAD_EXTENSIONS:
                uploaded_file.save(os.path.relpath('app/detection/upload/' + uploaded_file.filename))
                detection_type = request.form.get('type')
                if detection_type == "Document":
                    mrz = Mrz(os.path.relpath('app/detection/upload/' + uploaded_file.filename))
                    session['data'] = mrz.detection()
                    return redirect(url_for('result', title="Document Scan"))
                if detection_type == "Credit_card":
                    credit_card = Credit_card(os.path.relpath('app/detection/upload/' + uploaded_file.filename), os.path.relpath('app/detection/ocr_a_reference.png'))
                    cc = credit_card.detection()
                    session['data'] = "".join(cc)
                    return redirect(url_for('result', title="Credit Card Scan"))
                else:
                    return redirect(url_for('upload'))
            else:
                #If the file is the wrong format the user is redirect to the upload page
                return redirect('upload')
    return render_template('upload.html')

@app.route('/result')
def result():
    data = session.get('data')
    title = request.args.get('title')
    return render_template('result.html', title=title, data=data)