CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?,?)
"""

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_COUNT_QUERY = """
UPDATE ban SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""

CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
AGE INTEGER,
ZODIAC_SIGN CHAR(30),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES (?,?,?,?,?,?,?)
"""

SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

SELECT_ALL_PROFILE_QUERY = """
SELECT * FROM profile 
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_profile
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_profile VALUES (?,?,?)
"""

FILTER_LEFT_JOIN_PROFILE_QUERY = """
SELECT * FROM profile
LEFT JOIN like_profile ON profile.TELEGRAM_ID = like_profile.OWNER_TELEGRAM_ID
AND like_profile.LIKER_TELEGRAM_ID = ?
WHERE like_profile.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""

ALTER_USER_TABLE = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""
ALTER_USER_V2_TABLE = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""

UPDATE_REFERENCE_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

CREATE_REFERENCE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""

INSERT_REFERENCE_QUERY = """
INSERT INTO referral VALUES (?,?,?)
"""

DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT 
    COALESCE(telegram_users.BALANCE, 0) as BALANCE,
    COUNT(referral.ID) as total_referrals
FROM
    telegram_users
LEFT JOIN
    referral on telegram_users.TELEGRAM_ID = referral.OWNER_TELEGRAM_ID
WHERE 
    telegram_users.TELEGRAM_ID = ?
"""

SELECT_USER_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""


CREATE_NEWS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS news
(
    ID INTEGER PRIMARY KEY,
    TITLE TEXT,
    DESCRIPTION TEXT,
    LINK TEXT,
    IMAGE TEXT
)
"""

INSERT_NEWS_QUERY = """
INSERT INTO news (ID, TITLE, DESCRIPTION, LINK, IMAGE) VALUES (?,?,?,?,?)
"""