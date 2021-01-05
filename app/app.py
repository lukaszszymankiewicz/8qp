import os

from flask import Flask, render_template

from .src import delete_all_images

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_CONFIG"))


@app.route("/")
def main():
    delete_all_images()

    return render_template(
        template_name_or_list="index.html",
        title="Eight Queens Problem",
    )


if __name__ == "__main__":
    app.run()
