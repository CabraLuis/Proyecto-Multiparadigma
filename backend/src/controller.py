from database import connect


def insertGame(name, developer, distributor, released):
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO games(name, developer, distributor, released) VALUES (%s, %s, %s, %s)",
                       (name, developer, distributor, released))
        connection.commit()
        connection.close()


def selectGames():
    connection = connect()
    games = []
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, name, developer, distributor, DATE_FORMAT(released, '%Y-%m-%d') as released FROM games")
        games = cursor.fetchall()
    connection.close()
    return games


def selectGame(id):
    connection = connect()
    game = None
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT name, developer, distributor, DATE_FORMAT(released, '%Y-%m-%d') as released FROM games WHERE id = {id}")
        game = cursor.fetchone()
    connection.close()
    return game


def updateGame(name, developer, distributor, released, id):
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE games SET name=%s, developer=%s, distributor=%s, released=%s WHERE id = %s",
            (name, developer, distributor, released, id))
    connection.commit()
    connection.close()


def deleteGame(id):
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM games WHERE id = {id}")
    connection.commit()
    connection.close()
