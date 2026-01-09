import sqlite3

con = sqlite3.connect("new_census.db")
cur = con.cursor()


cur.execute("""create table Density (
                province test, population integer, area real)
                """)

con.commit()


table = [
 ('Newfoundland and Labrador', 512930, 370501.69),
 ('Prince Edward Island', 135294, 5684.39),
 ('Nova Scotia', 908007, 52917.43),
 ('New Brunswick', 729498, 71355.67),
 ('Quebec', 7237479, 1357743.08),
 ('Ontario', 11410046, 907655.59),
 ('Manitoba', 1119583, 551937.87),
 ('Saskatchewan', 978933, 586561.35),
 ('Alberta', 2974807, 639987.12),
 ('British Columbia', 3907738, 926492.48),
 ('Yukon Territory', 28674, 474706.97),
 ('Northwest Territories', 37360, 1141108.37),
 ('Nunavut', 26745, 1925460.18),
 ]

print(table)

for row in table:
     cur.execute("insert into Density values (?, ?, ?)", row)
con.commit()
            
cur.execute("select * from Density")
for row in cur.fetchall():
    print(row)


cur.execute("select population from Density")
for row in cur.fetchall():
    print(row)


cur.execute("select province from Density where population < 1000000""")
for row in cur.fetchall():
    print(row)


cur.execute("select province from density where population < 1000000 or \
population > 5000000""")
for row in cur.fetchall():
    print(row)


cur.execute(""" select province from Density where not(population < 1000000  or \
population > 5000000)""")
for row in cur.fetchall():
    print(row)


cur.execute(""" select population from Density where area > 200000""")
for row in cur.fetchall():
    print(row)



cur.execute(""" create table Capitals(province text, capital text, population integer)""")
con.commit()

table = [
 ('Newfoundland and Labrador', "St. John's", 172918),
 ('Prince Edward Island', 'Charlottetown', 58358),
 ('Nova Scotia', 'Halifax', 359183),
 ('New Brunswick', 'Fredericton', 81346),
 ('Quebec', 'Qeubec City', 682757),
 ('Ontario', 'Toronto', 4682897),
 ('Manitoba', 'Winnipeg', 671274),
 ('Saskatchewan', 'Regina', 192800),
 ('Alberta', 'Edmonton', 937845),
 ('British Columbia', 'Victoria', 311902),
 ('Yukon Territory', 'Whitehorse', 21405),
 ('Northwest Territories', 'Yellowknife', 16541),
 ('Nunavut', 'Iqaluit', 5236),
]

for row in table:
    cur.execute("insert into Capitals values (?, ?, ?)", row)

con.commit()

cur.execute("select * from Capitals")
for row in cur.fetchall():
    print(row)


## from here
cur.execute("""" select density.population, capitals.population
                from capitals inner join density
                where capitals.province = density.province """)

for row in cur.fetchall():
    print(row)


cur.execute(""" select density.area
                from capitals inner join density
                where capitals.province = density.province
                and capitals.population > 100000 """)

for row in cur.fetchall():
    print(row)




cur.execute(""" select density.province
                from capitals inner join density
                where capitals.province = density.province
                and density.population / density.area < 2
                and capitals.population > 500000""")

for row in cur.fetchall():
    print(row)


cur.execute('select sum(area) from density')
print(cur.fetchone())

cur.execute("select avg(population) from capitals")
print(cur.fetchone())

cur.execute("select min(population) from capitals")
print(cur.fetchone())

cur.execute("select max(population) from density")
print(cur.fetchone())


cur.execute(""" select A.province, B.province
                from density A inner join density B
                where A.province < B.province
                and ABS(A.population / A.area - B.population / B.area) < 0.5
                """)
for row in cur.fetchall():
    print(row)


con.commit()


cur.execute("create table numbers (val integer)")
cur.execute("insert into numbers values (1), (2);")
con.commit()
cur.execute("select * from numbers where 1/0")
print(cur.fetchone())

cur.execute("select * from numbers where 1/0 and val > 0")
print(cur.fetchone())

cur.execute("select * from numbers where val > 0 and 1/0")
print(cur.fetchone())
