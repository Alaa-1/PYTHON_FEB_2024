# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "full_crud"

# === C R U D ===

# model the class after the friend table from our database
class Car:
    def __init__(self, data):
        self.id = data["id"]
        self.make = data["make"]
        self.model = data["model"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    #! all queries are classmethods
        
    #* =========== READ ALL ===========
        
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM cars;"

        results = connectToMySQL(DATABASE).query_db(query)

        # print(results)

        cars_instances = []
        if results:
            for row in results:
               one_car = Car(row)
               cars_instances.append(one_car)

            return cars_instances
        
        return []
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):

        query = """
                INSERT INTO cars (make, model, color)
                VALUES (%(make)s, %(model)s,%(color)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        # print("The id of the created car is: ", result)

        return result
    
    #* =========== READ ONE ===========
    @classmethod
    def get_one_by_id(cls, data):

        query = """
                    SELECT * FROM cars
                    WHERE id = %(id)s;
                """
        
        result =  connectToMySQL(DATABASE).query_db(query, data)

        return Car(result[0])
    
    #* =========== UPDATE ===========
    @classmethod
    def update(cls, data):
        
        query = """
                    UPDATE cars
                    SET make = %(make)s, 
                    model = %(model)s, 
                    color = %(color)s
                 
                    WHERE id = %(id)s;
                """
        
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        pass
    #TODO