import hashlib
import random

from sys import intern
from time import time, sleep
from itertools import islice
from typing import NamedTuple, Deque, DefaultDict, Set, Optional, List, Tuple, Dict
from collections import deque, defaultdict
from heapq import merge
from bisect import bisect

import secrets

from config import pepper, time_unit_cuts, time_units

HashAndSalt = Tuple[bytes, bytes]
Timestamp = float
User = str

Post = NamedTuple('Post', [('timestamp', float), ('user', str), ('text', str)])
UserInfo = NamedTuple(
    'UserInfo',
    [
        ('display_name', str),
        ('email', str),
        ('hashed_password', HashAndSalt),
        ('bio', Optional[str]),
        ('photo', Optional[str]),
    ],
)

# Posts from newest to oldest
posts = deque()  # type: Deque
user_posts = defaultdict(deque)  # type: DefaultDict[User, Deque]
following = defaultdict(set)  # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)  # type: DefaultDict[User, Set[User]]
user_info = dict()  # type: Dict[User, UserInfo]


def hash_password(password: str, salt: Optional[bytes] = None) -> HashAndSalt:
    salt = salt or secrets.token_bytes(16)
    salted_password = salt + password.encode('utf-8')
    return hashlib.pbkdf2_hmac('sha512', salted_password, pepper, 100000), salt


def set_user(
    user: User,
    display_name: str,
    email: str,
    password: str,
    bio: Optional[str] = None,
    photo: Optional[str] = None,
) -> None:
    user = intern(user)
    hashed_password = hash_password(password)
    user_info[user] = UserInfo(display_name, email, hashed_password, bio, photo)


def check_user(user: User, password: str) -> bool:
    hashpass, salt = user_info[user].hashed_password
    target_hash_pass = hash_password(password, salt)[0]
    sleep(random.expovariate(10))
    return secrets.compare_digest(hashpass, target_hash_pass)


def get_user(user: User) -> UserInfo:
    return user_info[user]


def age(post: Post) -> str:
    seconds = time() - post.timestamp
    divisor, unit = time_units[bisect(time_unit_cuts, seconds)]
    units = seconds // divisor
    return '%d %s ago' % (units, unit + ('' if units == 1 else 's'))


def post_message(user: User, text: str, timestamp: Timestamp = None) -> None:
    user = intern(user)
    timestamp = timestamp or time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)


def get_followers(user: User) -> List[User]:
    return sorted(followers[user])


def get_followed(user: User) -> List[User]:
    return sorted(following[user])


def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))


def posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    relevant_posts = merge(*[user_posts[fu] for fu in following[user]], reverse=True)
    return list(islice(relevant_posts, limit))


def personal_posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    personal_posts = user_posts[user]
    return list(islice(personal_posts, limit))


def search(phrase: str, limit: Optional[int] = None) -> List[Post]:
    return list(islice((post for post in posts if phrase in post.text), limit))
