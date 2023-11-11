from flask import Flask, request, render_template, jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/howItWorks')
def how_it_works():
    return render_template('howItWorks.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/process_image', methods=['POST'])
def process_image():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Read the image file
        img = Image.open(file)

        # Process the image (you can replace this with your own logic)
        result_string = f"Image processed. Dimensions: {img.size}"

        return jsonify({'result': result_string})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
