from app import app
from models import Production, Role, db

with app.app_context():
    Production.query.delete()
    Role.query.delete()

    menu = Production(title='the menu',
                    genre='thriller',
                    length=107,
                    image='https://m.media-amazon.com/images/M/MV5BMzdjNjI5MmYtODhiNS00NTcyLWEzZmUtYzVmODM5YzExNDE3XkEyXkFqcGdeQXVyMTAyMjQ3NzQ1._V1_FMjpg_UX1000_.jpg',
                    language='english',
                    director='mark mylod',
                    description='Painstakingly prepared.  Brilliantly executed.',
                    composer='colin stetson',
                    year=2022
                    )

    everything = Production(
        title="everything everywhere all at once",
        genre='sci-fi',
        length=139,
        image="https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyMTgtYzk5Y2M3ZDVmMDk1XkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_FMjpg_UX1000_.jpg",
        language='english, mandarin',
        director='daniel kwan',
        description='Sucked into a bagel.',
        composer='son lux',
        year=2022
    )

    guardians = Production(
        title="guardians of the galaxy vol. 2",
        genre='sci-fi',
        length=137,
        language='english',
        image='https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_FMjpg_UX1000_.jpg',
        composer='tyler bates',
        year=2017,
        director='james gunn',
        description='when things get bad, they\'ll do their worst'
    )
    budapest = Production(
        title='the grand budapest hotel',
        genre='comedy',
        length=100,
        year=2014,
        image='https://m.media-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_FMjpg_UX1000_.jpg',
        language='english',
        director='wes anderson',
        composer='alexandre desplat',
        description='keep your hands off my lobby boy!'
    )

    margot = Role(
        role_name='Margot',
        #built relationships, therefore instead of using foreign_key integer, we can pass in an instance instead
        production=menu 
    )
    chef = Role(
        role_name='Chef Slowik',
        production=menu
    )
    evelyn = Role(
        role_name='Evelyn Quan Wang',
        production=everything
    )
    monsieur = Role(
        role_name='Monsieur Gustave H.',
        production=budapest
    )
    deputy = Role(
        role_name="Deputy Vilmos Kovacs",
        production=budapest
    )
    aleta = Role(
        role_name='Aleta Ogord',
        production=guardians
    )
    gamora = Role(
        role_name='gamora',
        production=guardians
    )

    roles = [margot, chef, evelyn, monsieur, deputy, aleta, gamora]
    prods = [menu, everything, guardians, budapest]

    db.session.add_all(roles)
    db.session.add_all(prods)
    db.session.commit()