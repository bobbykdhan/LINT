import flask
app = flask.Flask(__name__)

@app.route("/")
async def root():
    return {"message": "Hello World"}


@app.route("/hello/<name>")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.route("/ticket/<building>/<machineNum>")
async def ticket(building, machineNum):
    return flask.render_template("ticket.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)