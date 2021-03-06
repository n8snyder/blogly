"""Seed file to make sample data for pets db."""

from models import db, User, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty if
PostTag.query.delete()
Tag.query.delete()
Post.query.delete()
User.query.delete()

# Add users
whiskey = User(first_name="Whiskey", last_name="dog")
bowser = User(
    first_name="Bowser",
    last_name="dog",
    image_url="https://pbs.twimg.com/profile_images/949787136030539782/LnRrYf6e_400x400.jpg",
)
spike = User(first_name="Spike", last_name="porcupine")

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

db.session.commit()


# Add posts

whisky_post = Post(
    title= "Whiskey's Opinion's",
    content= "I have none.",
    user_id= whiskey.id
)

bowser_post = Post(
    title= "Bowser's Opinion's",
    content= "I have MANY.",
    user_id= bowser.id
)

db.session.add(whisky_post)
db.session.add(bowser_post)

# Commit--otherwise, this never gets saved!
db.session.commit()


# Create Tags
tag1 = Tag(name="opinion")
tag2 = Tag(name="nsfw")

db.session.add(tag1)
db.session.add(tag2)

whisky_post.tags.append(tag1)
bowser_post.tags.append(tag2)

db.session.commit()

# PostTag auto populated