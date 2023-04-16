from flask import Flask,jsonify,request

app = Flask(__name__)

movies = [

    {
        "name": "Avengers",
        "casts": ["Chris Evans", "Chris Hemsworth", "Scarlett Johansson"],
        "genres": ["Action", "Comedy"]
    },
      {
        "name": "Frozen",
        "casts": ["Idina Menzel", "Jonathan Groff", "Josh Gad"],
        "genres": ["Drama", "Comedy"]
      },

]

@app.route('/movies', methods=['GET'])
def getMovies():
  return jsonify(movies)

@app.route('/movies', methods=['GET'])
def add_Movies():
    movies = request.get_json()
    movies.append(movie)
    return{'id':len(Movies)},200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_Movie(index):
    movies.pop(index)
    return "Successfully deleted",200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_Movie(index):
    name = request.json.get("name")
    casts = request.json.get("casts")
    genres = request.json.get("genres")
    movies[index] = [{"name":name, "casts":casts, "genres":genres}]
    return "Successfully updated",200

@app.route('/movies/<int:index>', methods=['GET'])
def display_Movie(index):
    return jsonify(movies{index})

@app.route('/movies', methods=['DELETE'])
def delete_All_Movie():
    movies.clear()
    return "Successfully deleted",200

if __name__ == "__main__":
    app.run()

