import os
import time

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

    start = time.time()
    all_solutions = find_all_solutions()
    end = time.time()
    solve_time = end - start

    images_time_start = time.time()
    for solution in all_solutions:
        filename = "".join(str(n) for n in solution)
        draw_solution(solution=solution, path="app/static/solutions/all/" + filename + ".png")
    images_time_end = time.time()
    images_time = images_time_end - images_time_start

    filter_time_start = time.time()
    filtered_solutions = filter_redundant_solutions(all_solutions)
    filter_time_end = time.time()
    filter_time = filter_time_end - filter_time_start

    images_time_start = time.time()
    for solution in filtered_solutions:
        filename = "".join(str(n) for n in solution)
        draw_solution(solution=solution, path="app/static/solutions/base/" + filename + ".png")
    images_time_end = time.time()
    images_time += images_time_end - images_time_start

    return render_template(
        template_name_or_list="index.html",
        title="Eight Queens Problem",
        all_solutions_imgs=get_all_solutions_images(),
        base_solutions_imgs=get_base_solutions_images(),
        solve_time=solve_time,
        filter_time=filter_time,
        images_time=images_time,
    )


if __name__ == "__main__":
    app.run()
