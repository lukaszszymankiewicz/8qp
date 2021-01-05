import os

from flask import Flask, render_template

from .src import (delete_all_images, draw_solution, filter_redundant_solutions,
                  find_all_solutions, get_all_solutions_images,
                  get_base_solutions_images)

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_CONFIG"))
delete_all_images()


@app.route("/")
def index():
    delete_all_images()
    all_solutions = find_all_solutions()
    filtered_solutions = filter_redundant_solutions(all_solutions)

    for solution in all_solutions:
        filename = "".join(str(n) for n in solution)
        draw_solution(solution=solution, path="app/static/solutions/all/" + filename + ".png")

    for solution in filtered_solutions:
        filename = "".join(str(n) for n in solution)
        draw_solution(solution=solution, path="app/static/solutions/base/" + filename + ".png")

    return render_template(
        template_name_or_list="index.html",
        title="Eight Queens Problem",
        all_solutions_imgs=get_all_solutions_images(),
        base_solutions_imgs=get_base_solutions_images(),
    )


if __name__ == "__main__":
    app.run()
