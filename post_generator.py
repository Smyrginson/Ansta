
def post_generator(start_post: str, stop_post: str):
    begin = int(start_post.replace('-', ''))
    while begin < int(stop_post.replace('-', '')):
        yield f'{begin//1000}-{begin%1000}'
        begin += 1


g = post_generator('79-900', '80-155')
print(next(g))
print(next(g))
print(list(g))

