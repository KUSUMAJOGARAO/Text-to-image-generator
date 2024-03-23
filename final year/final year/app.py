from flask import Flask, render_template, request, jsonify
from diffusers import StableDiffusionPipeline
import datetime

app = Flask(__name__)

# Initialize Stable Diffusion Pipeline
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_image', methods=['POST'])
def generate_image():
    text_prompt = request.form['textPrompt']
    image = pipe(text_prompt, guidance_scale=7.5)["images"][0]

    # Generate a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Save the image with the timestamp as the filename
    image_path = f"static/output_image_{timestamp}.png"
    image.save(image_path)

    return jsonify({'image_path': image_path})


if __name__ == '__main__':
    app.run(debug=True)
