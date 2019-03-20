from pubsub import set_user, post_message, follow
from pprint import pprint
from time import time

set_user(
    'felix',
    display_name='Felix the Cat',
    password='123456',
    email='felix@cat.com',
    bio='Felix!',
    photo='felix.jpg',
)
set_user(
    'popeye',
    display_name='Popeye the Sailor',
    password='123456',
    email='popeye@sailor.com',
    bio='Popeye!',
    photo='popeye.jpg',
)
set_user(
    'homer',
    display_name='Homer Simpson',
    password='123456',
    email='homer@simpson.com',
    bio='Husband of Marge Simpson.',
    photo='homer.jpg',
)

now = time()
post_message('felix', '#python tip: use named tuples', now - 3600 * 48)
post_message('felix', '#python tip: develop interactively', now - 500)
post_message('popeye', 'gradient descent save me money on travel', now - 2500)
post_message('popeye', 'join a band today', now - 3600)
post_message('homer', 'Donuts?', now - 80)
post_message('homer', 'Anybody here?', now - 50)
post_message('homer', 'have you ever wanted to unpack mappings?', now - 46)

follow('felix', followed_user='homer')
follow('felix', followed_user='popeye')
follow('homer', followed_user='felix')
follow('homer', followed_user='popeye')
follow('popeye', followed_user='homer')

if __name__ == '__main__':
    from pubsub import posts, followers, following, user_info
    from pubsub import posts_by_user, posts_for_user, search
    from pubsub import get_followers, get_followed, get_user, check_user, age

    assert check_user('felix', password='123456')
    assert not check_user('homer', password='1234567890')

    print()
    pprint(list(posts))

    print('\nFollowers')
    pprint(dict(followers))

    print('\nFollowing')
    pprint(dict(following))

    print("\nUser info")
    pprint(user_info)

    print('-' * 50)

    print('\nPosts by felix (3)')
    pprint(posts_by_user('felix', limit=3))

    print('\nPosts for homer (6)')
    pprint(posts_for_user('homer', limit=6))

    print('\nSearch for #python (4)')
    pprint(search('#python', limit=4))

    print("\nFelix 's followers")
    pprint(get_followers('felix'))

    print("\nHomer follows")
    pprint(get_followed('homer'))

    print("\nPopeye's info")
    print(get_user('popeye'))

    print("\nPost ages")
    pprint(list(map(age, posts)))
