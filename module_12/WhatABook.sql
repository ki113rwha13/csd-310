/*
    Title: whatabook.sql
    Author: Cory Thomaier
    Date: 3/1/2023
    Description: WhatABook database initialization script.
*/

DROP DATABASE whatabook;
CREATE DATABASE whatabook;



-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP USER IF EXISTS 'MySQL8IsGreat!';
-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password, 'MySQL8IsGreat!';
use whatabook;
 
-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook TO 'whatabook_user'@'localhost';

-- drop contstraints if they exist
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
-- ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1234 Fake St, Omaha, NE 68164');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Signal Fires', 'Dani Shapiro', 'Dani Shapiro?s first novel in 15 years');

INSERT INTO book(book_name, author, details)
    VALUES('Trust', 'Hernan Diaz', 'In 1920s New York, everyone who?s anyone knows Benjamin and Helen Rask, the wealthy couple sitting pretty at the top of the financial world.');

INSERT INTO book(book_name, author, details)
    VALUES('Lesser Known Monsters of the 21st Century', 'Kim Fu', "Fu brings magical realism to exciting heights, positioning her characters? relatable emotional battles within wonderfully constructed worlds.");

INSERT INTO book(book_name, author, details)
    VALUES('Young Mungo	', 'Douglas Stuart', 'Young Mungo is another visceral depiction of 20th-century working class Glasgow, this time centered on the impossible first love between two teenage boys.');

INSERT INTO book(book_name, author, details)
    VALUES('If I survive you', 'Jonathan Escoffery', 'The first entry in Jonathan Escoffery?s lyrical and kaleidoscopic debut If I Survive You introduces the character at the short story collection?s center: Trelawny, the sole American-born member of a Jamaican family.');

INSERT INTO book(book_name, author, details)
    VALUES('Vladimir', 'Julia May Jonas', 'The protagonist of Julia May Jonas? electric debut novel, an unnamed English professor, is grappling with the public fallout of her husband?s past affairs with students at the college where they both teach.');

INSERT INTO book(book_name, author, details)
    VALUES('All This Could Be Different	', 'Sarah Thankam Mathews', 'Though the work is soul-crushing, there?s a recession swirling and the money keeps Sneha afloat');

INSERT INTO book(book_name, author, details)
    VALUES('The Book of Goose', 'Yiyun Li', 'Agnès has just heard the news that her childhood best friend, Fabienne, is dead.');

INSERT INTO book(book_name, author, details)
    VALUES('The Hero of This Book', 'Elizabeth McCracken', 'An unnamed writer arrives in London for a trip. She feels her recently deceased mother?s absence-and presence-everywhere she goes.');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Cory', 'Thomaier');

INSERT INTO user(first_name, last_name)
    VALUES('Rachel', 'Moore');

INSERT INTO user(first_name, last_name)
    VALUES('John', 'Doe');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Cory'), 
        (SELECT book_id FROM book WHERE book_name = 'The Hero of This Book')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rachel'),
        (SELECT book_id FROM book WHERE book_name = 'The Book of Goose')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Vladimir')
    );