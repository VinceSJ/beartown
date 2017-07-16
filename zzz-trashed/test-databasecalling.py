import sqlalchemy as sa

engine = sa.create_engine('sqlite:///bears.db')


meta = sa.MetaData()  # Nothing special, just enables some sort of cleverness.

bears = sa.Table('bears', meta,
                 sa.Column('id', sa.Integer, primary_key=True),  # Used for pulling bear, also for locating profile pic.
                 sa.Column('name', sa.String),
                 sa.Column('species', sa.String),
                 sa.Column('age', sa.Integer),
                 sa.Column('weight', sa.Float),  # in pounds
                 sa.Column('gender', sa.String),  # 3 values: 'male', 'female', 'nonbinary'
                 sa.Column('furcolor', sa.String),
                 sa.Column('inrelationship', sa.Boolean),  # True means in relationship, false is single.
                 sa.Column('bio', sa.String)
                 )

meta.create_all(engine, checkfirst=True)  # checkfirst means it only creates if Table does not already exist

# engine.execute(bears.insert((3, 'Test', 'Species', 100, 80.2, 'male', 'orange', True, "He's a figment of your imagination. I'm sorry.")))

test = engine.execute(bears.select())

# Below is sample code for grabbing a single row from db based on id.
# test = engine.execute(bears.select().where(bears.c.id == 3))

for row in test:
    print(row)

engine.execute(bears.drop())
