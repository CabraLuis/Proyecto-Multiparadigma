import json
from flask import Flask, jsonify, redirect, request, send_file

import controller

app = Flask(__name__)


@app.route("/createGame", methods=["POST"])
def createGame():
    name = request.form['name']
    developer = request.form['developer']
    distributor = request.form['distributor']
    released = request.form['released']
    controller.insertGame(name, developer, distributor, released)
    return redirect("http://localhost:4321/all")


@app.route("/viewGames", methods=["GET"])
def viewGames():
    games = controller.selectGames()
    print(games)
    return jsonify(games)


@app.route("/viewGame/<int:id>", methods=["GET"])
def viewGame(id):
    game = controller.selectGame(id)
    print(game)
    return jsonify(game)


@app.route("/updateGame/<int:id>", methods=["POST"])
def updateGame(id):
    name = request.form['name']
    developer = request.form['developer']
    distributor = request.form['distributor']
    released = request.form['released']
    controller.updateGame(name, developer, distributor, released, id)
    return redirect("http://localhost:4321/all")


@app.route("/deleteGame/<int:id>", methods=["POST"])
def deleteGame(id):
    controller.deleteGame(id)
    return redirect("http://localhost:4321/all")


@app.route("/download", methods=["GET"])
def downloadCSV():
    games = controller.selectGames()
    print(games)
    with open("./games.json", "w") as file:
        file.write(json.dumps(games))
    return send_file("../games.json", as_attachment=True, download_name="games.json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
