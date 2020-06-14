import redis
from rq import Queue, Connection
from flask import render_template, Blueprint, jsonify, request, current_app
from project.server.main.tasks import create_task
from multiprocessing import Value

main_blueprint = Blueprint("main", __name__,)

@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")

@main_blueprint.route("/tasks", methods=["POST"])
def run_task():
    task_type = request.form["type"]
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        task = q.enqueue(create_task, task_type)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object)

@main_blueprint.route("/pop", methods=["POST"])
def run_pop():
    pop_type = request.form["type"]
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        pop = q.enqueue(create_task, pop_type)
    response_object = {
        "status code": "200",
        "body": {
            "status": "ok",
            "message": "what an awesome code",
        }
    }
    return jsonify(response_object), 200

@main_blueprint.route("/push", methods=["POST"])
def run_push():
    push_type = request.form["type"]
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        push = q.enqueue(create_task, push_type)
    response_object = {
        "status code": "200",
        "body": {
            "status": "ok",
        }
    }
    return jsonify(response_object), 200

@main_blueprint.route("/count", methods=["GET"])
def run_count():
    counter = Value('i', 0)
    with counter.get_lock():
         counter.value += 1
         out = counter.value
    response_object = {
            "status code": "200",
            "body": {
                "status": "ok",
                "count": out,
            },
        }
    return jsonify(response_object)
