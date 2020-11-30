INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO meal_swipe (venmo, price, seller_id, buyer_id)
VALUES
  ('test_venmo', 5, 1, 2),
  ('test_venmo', 6, 1, NULL),
  ('other_venmo', 3, 2, NULL);

INSERT INTO review (seller_id, buyer_id, swipe_id, rating, description)
VALUES
  (1, 2, 1, 4, "test review");
