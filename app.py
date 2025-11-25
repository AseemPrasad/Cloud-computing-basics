from flask import Flask, Response
import random

app = Flask(_name_)

@app.route("/metrics")
def metrics():
    cpu = random.randint(10, 90)
    memory = random.randint(20, 80)
    response = f"""# HELP cpu_usage CPU usage percentage
# TYPE cpu_usage gauge
cpu_usage {cpu}
# HELP memory_usage Memory usage percentage
# TYPE memory_usage gauge
memory_usage {memory}
"""
    return Response(response, mimetype="text/plain")

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)