-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS meal_swipe;
DROP TABLE IF EXISTS message;
DROP TABLE IF EXISTS review;

CREATE TABLE user (
  /*id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  payment_info TEXT*/

  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE meal_swipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  seller_id INTEGER NOT NULL,
  buyer_id INTEGER NOT NULL,
  timestamp_sell TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  timestamp_buy TIMESTAMP,
  price DECIMAL NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (seller_id) REFERENCES user (id),
  FOREIGN KEY (buyer_id) REFERENCES user (id)
);

CREATE TABLE review (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  seller_id INTEGER NOT NULL,
  buyer_id INTEGER NOT NULL,
  swipe_id INTEGER NOT NULL,
  'timestamp' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  rating INTEGER NOT NULL,
  description TEXT NOT NULL,
  FOREIGN KEY (seller_id) REFERENCES user (id),
  FOREIGN KEY (buyer_id) REFERENCES user (id),
  FOREIGN KEY (swipe_id) REFERENCES meal_swipe (id)
);

CREATE TABLE message (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  seller_id INTEGER NOT NULL,
  buyer_id INTEGER NOT NULL,
  swipe_id INTEGER NOT NULL,
  'timestamp' TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  'read' BOOLEAN NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (seller_id) REFERENCES user (id),
  FOREIGN KEY (buyer_id) REFERENCES user (id),
  FOREIGN KEY (swipe_id) REFERENCES meal_swipe (id)
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);