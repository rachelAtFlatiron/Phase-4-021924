#!/usr/bin/env python3

# 4a. Imports
from app import app 
from models import Production, db
# 4b. Create application context `with app.app_context():`
with app.app_context():
    # 4c. Create a query to delete all existing records from Production
    Production.query.delete()

    # 4d. Create some seeds for production and commit them to the database.

    #create instance of Production class
    #that will end up being a row
    amsterdam = Production(
        title="amsterdam", #attributes, params
        genre="mystery",
        image="https://m.media-amazon.com/images/M/MV5BNDQwNzE0ZTItYmZjMC00NjI3LWFlNzctNTExZDY2NWE0Zjc0XkEyXkFqcGdeQXVyMTA3MDk2NDg2._V1_FMjpg_UX1000_.jpg",
        length=134,
        director="david o russell",
        composer="daniel pemberton",
        description="let the love, murder, and conspiracy begin"
    )

    db.session.add(amsterdam)
    db.session.commit()

    # Creating instances of the Movie class
    shawshank_redemption = Production(
        title="The Shawshank Redemption",
        genre="Drama",
        image="https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTAzMDM4MjM0._V1_FMjpg_UX1000_.jpg",
        length=142,
        director="Frank Darabont",
        composer="Thomas Newman",
        description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        year=1994
    )

    the_godfather = Production(
        title="The Godfather",
        genre="Crime, Drama",
        image="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg",
        length=175,
        director="Francis Ford Coppola",
        composer="Nino Rota",
        description="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        year=1972
    )
    inception = Production(
        title="Inception",
        genre="Action, Adventure, Sci-Fi",
        image="https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX1000_.jpg",
        length=148,
        director="Christopher Nolan",
        composer="Hans Zimmer",
        description="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        year=2010
    )

    the_dark_knight = Production(
        title="The Dark Knight",
        genre="Action, Crime, Drama",
        image="https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_FMjpg_UX1000_.jpg",
        length=152,
        director="Christopher Nolan",
        composer="Hans Zimmer",
        description="When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        year=2008
    )

    forrest_gump = Production(
        title="Forrest Gump",
        genre="Drama, Romance",
        image="https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg",
        length=142,
        director="Robert Zemeckis",
        composer="Alan Silvestri",
        description="The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.",
        year=1994
    )

    the_matrix = Production(
        title="The Matrix",
        genre="Action, Sci-Fi",
        image="https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg",
        length=136,
        director="Lana Wachowski, Lilly Wachowski",
        composer="Don Davis",
        description="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        year=1999
    )

    pulp_fiction = Production(
        title="Pulp Fiction",
        genre="Crime, Drama",
        image="https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg",
        length=154,
        director="Quentin Tarantino",
        composer="Various Artists",
        description="The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        year=1994
    )


    db.session.add_all([shawshank_redemption, the_godfather, inception, pulp_fiction, the_matrix, forrest_gump, the_dark_knight])
    db.session.commit()

    # 5. Check seeds
