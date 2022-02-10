from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash 


class Game:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.opponent = data['opponent']
        self.date = data['date']
        self.time = data['time']
        self.level = data['level']
        self.maces_score = data['maces_score']
        self.opponent_score = data['opponent_score']
        self.outcome = data['outcome']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.season_id = data['season_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM games;"
        results = connectToMySQL('maces_schema').query_db(query)
        games = []
        for game in results:
            games.append( cls(game) )
        return games

    @classmethod
    def save(cls, data):
        query = "INSERT INTO games (location, opponent, date, time, level, maces_score, opponent_score, outcome, type, created_at, updated_at, season_id ) VALUES (%(location)s, %(opponent)s, %(date)s, %(time)s, %(level)s, %(maces_score)s, %(opponent_score)s, %(outcome)s, %(type)s, NOW() , NOW(), %(season_id)s);"
        return connectToMySQL('maces_schema').query_db( query, data )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM games WHERE id = %(id)s;"
        results = connectToMySQL('maces_schema').query_db(query, data)
        return cls(results[0])
    
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM games WHERE id = %(id)s"
        return connectToMySQL('maces_schema').query_db(query, data)