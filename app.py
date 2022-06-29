from flask import Flask, render_template, request
import pandas as pd
import csv

app = Flask(__name__)

#upload excel
@app.route('/', methods = ['GET','POST'])
def lihat():
    return render_template('unggah.html')

#lihat hasil upload
@app.route('/tentang', methods = ['GET', 'POST'])
def data():
    if request.method == 'POST':
            f = request.form ['file']
            data = []
            with open (f) as file:
                csvfile = csv.reader(file)
                for row in csvfile:
                    data.append (row)
                    res = max(file, key = len)
                    print('jumlah terpanjang', len(res))
                    return render_template('selesai.html', hasil=res)
            data = pd.DataFrame(data)
    return render_template('selesai.html', data=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)
    

