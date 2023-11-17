from frequency_table import substring_count


As = [
      'esleastealaslatet',
    'lrldrrrllddrrlllrddd', 
      'kkkkkvvuvkvkkkvuuvkuukkuvvkukkvkkvuvukuk', 
      'trhtrthtrthhhrtthrtrhhhtrrrhhrthrrrttrrttrthhrrrrtrtthhhhrrrtrtthrttthrthhthrhrh',
      'hjjijjhhhihhjjhjjhijjihjjihijiiihhihjjjihjjiijjijjhhjijjiijhjihiijjiiiijhihihhiihhiiihhiijhhhiijhijj'
]

Bs = [
    ('tesla',),
    ('ldl', 'rld'),
    ('vkuk', 'uvku', 'kukk'),
    ('rrrht', 'tttrr', 'rttrr', 'rhrrr'),
    ('jihjhj', 'hhjiii', 'ihjhhh', 'jjjiji'),
]

for i in range(len(As)):
    A = As[i]
    tuple_bs = Bs[i]

    for B in tuple_bs:
        print(A)
        print(B)
        breakpoint()

        print(substring_count(A, B))        