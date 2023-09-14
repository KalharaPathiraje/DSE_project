from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_word():
    return render_template('website(D&D).html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['input-file']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)


    classification='Testing'
    return render_template('website(D&D).html', prediction=classification)


if __name__ == '__main__':
    app.run(port=3000, debug=True)