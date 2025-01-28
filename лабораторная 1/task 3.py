# TODO Найдите количество книг, которое можно разместить на дискете
inf_mb = 1.44
pages = 100
string = 50
sim = 25
sim_size_b = 4

per = inf_mb * 2 ** 20
por = sim_size_b * sim * string * pages
print("Количество книг, помещающихся на дискету:", int(per // por))