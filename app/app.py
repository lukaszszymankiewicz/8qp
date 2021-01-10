import os
import time

from flask import Flask, render_template

from .src import (all_solutions_path, base_solutions_path, delete_all_images,
                  draw_solution, filter_redundant_solutions,
                  find_all_solutions, get_all_files_in_path, png_ext)

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_CONFIG"))
delete_all_images()
# TODO: add startup and exit signals, and put deleteion of images there


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
        draw_solution(solution=solution, path=all_solutions_path + filename + png_ext)
    images_time_end = time.time()
    images_time = images_time_end - images_time_start

    filter_time_start = time.time()
    filtered_solutions = filter_redundant_solutions(all_solutions)
    filter_time_end = time.time()
    filter_time = filter_time_end - filter_time_start

    images_time_start = time.time()
    for solution in filtered_solutions:
        filename = "".join(str(n) for n in solution)
        draw_solution(solution=solution, path=base_solutions_path + filename + png_ext)
    images_time_end = time.time()
    images_time += images_time_end - images_time_start

    return render_template(
        template_name_or_list="index.html",
        title="Eight Queens Problem",
        all_solutions_imgs=get_all_files_in_path(all_solutions_path),
        base_solutions_imgs=get_all_files_in_path(base_solutions_path),
        solve_time=solve_time,
        filter_time=filter_time,
        images_time=images_time,
    )


if __name__ == "__main__":
    app.run()
