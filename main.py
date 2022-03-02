import json

from flask import Flask
import functions

app = Flask(__name__)


@app.route("/<id>")
def get_by_id(id: str):
    param = (id)
    sql = """SELECT 
             new_animal.id,
             new_animal.animal_id,
             new_animal.type_id,
             new_animal.breed_id,
             new_animal.name,
             new_animal.age_upon_outcome,
             animal_type.name as 'type',
             animal_breed.name as 'breed'
             FROM new_animal
             LEFT JOIN animal_type 
                 ON animal_type.id = new_animal.type_id
            LEFT JOIN animal_breed 
                 ON animal_breed.id = new_animal.breed_id
             WHERE new_animal.id = ?
             """
    result = []
    for item in functions.get_result(sql, param):
        s = {
            "id": item.get("id"),
            "animal_id": item.get("animal_id"),
            "age_upon_outcome": item.get("age_upon_outcome"),
            "name": item.get("name"),
            "type_id": item.get("type"),
            "breed_id": item.get("breed")
        }
        result.append(s)

    return app.response_class(response=json.dumps(result),
                              status=200,
                              mimetype="application/json")


if __name__ == '__main__':
    app.run()
