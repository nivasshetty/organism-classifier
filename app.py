from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def classify():
    result = None
    image_url = None
    if request.method == "POST":
        unicellular = request.form["unicellular"]
        nucleus = request.form["nucleus"]
        photosynthesis = request.form["photosynthesis"]
        decay = request.form["decay"]

        if unicellular == "yes":
            if nucleus == "yes":
                result = "Protistaaa"
                image_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiLMJH_FLQLxzT1W2LI4vnH6YTNR3Cl2SWetrn2MrZyM7qaTe0Wj1ZhG2HQzaRNKitg-5a0Sch6zBZX4c29jXkGAk-kfq2qxiNDYe_ZMkM07GD2nwFivqwWORNyDxOIRoTqsHuUq1XCwTKhYLWX1AQ-F4Iy2j32RVeiMGJz-iC1tBeVyb7mZKPTWy7Qiv5/s1698/Kingom%20protista%20classification.jpg"
            else:
                result = "Moneraa"
                image_url = "http://image.slidesharecdn.com/plant-kingdom-1225607378783598-8/95/plant-kingdom-classification-3-728.jpg?cb=1279768732"
        else:
            if photosynthesis == "yes":
                result = "Plantae"
                image_url = "https://i.pinimg.com/originals/c0/48/04/c04804cab901247074730a2d5833d6de.jpg"
            elif decay == "yes":
                result = "Fungi"
                image_url = "https://image.slideserve.com/1429464/kingdom-fungi-l.jpg"
            else:
                result = "Animalia"
                image_url = "https://i.pinimg.com/originals/98/c3/a3/98c3a3e0c1d07dd941f3bb3b309e5a34.jpg"

    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run( host = '0.0.0.0', port = int(os.eviron.get('PORT', 5000)))

