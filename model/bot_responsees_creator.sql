
-- create database music_challenger;

use music_challenger;

-- update Messages
-- set message = "Hey you… \nWelcome to the coolest Music Challenger ever!!!\n\nI’m gonna challenge you by sending u a small peek to a song I choose and your job is guessing the song name.\n\nOf course if you need help of any kind, pleas type /help.\nSoo… Are u ready??"
-- where state = 1;

-- update Messages
-- set message = "Asking for help it’s not  a shame! (Of course it is, I’m just being polite:)\nSo here are the ways I can help you with:\n\nplease text me back:\n /answer  - to get the answer (LOSER!!)\n/hint – to get a bigger peek to the song\n/restart – to start over\n/quit – to quit this game\nI hope I was being helpful:)"
-- where id = 8;

select * from Messages;
-- CREATE TABLE Messages (
--     id INT NOT NULL PRIMARY KEY auto_increment,
--     message VARCHAR(1000),
--     state int,
-- 	sub_state int default 0
-- );

-- start
-- insert into Messages
-- values(default , "Hey you…\nWelcome to the coolest Music Challenger ever!!!\nI’m gonna challenge you by sending u a small peek to a song I choose and your job is guessing the song name.\nOf course if you need help of any kind, pleas type /help.\nSoo… Are u ready??", 1, default);
-- -- finish
-- insert into Messages
-- values(default , "Hope you were having a great time with me, if you ever in the mood of challenge again, I am here for you !",3, default);
-- -- good guess
-- insert into Messages
-- values(default , "Hooray!! You did it! You must be a big fan!\n Would you like to try again?",2, 1);

-- insert into Messages
-- values(default , "Well done! You did a great job!\n Would you like to be challenged one more time?",2, 1);
-- -- bad guess
-- insert into Messages
-- values(default , "Oops, Try again or try spelling the name right",2, 2);

-- insert into Messages
-- values(default , "Bad guess, but you maybe close, Try again!",2, 2);

-- insert into Messages
-- values(default , "Feel free to call for help by typing /help, or just try again :)",2, 2);
-- help
-- insert into Messages
-- values(default , "Asking for help it’s not a shame! (Of course it is, I’m just being polite)\nSo here are the ways I can help you with:\nIf u want me to tell you the answer (LOSER!!), please text me back: answer\nIf you want a hint and get a bigger peek to the song, just type: hint\nAnd if you are really desperate, which I totally get, u can quit  by text me the word: quit, or try again with another artist by typing: restart.\nI hope I was being helpful\n ",5, default);

-- insert into Messages
-- values(default , "Umm, I do not provide this kind of help. Duwanna keep guessing? ",5,1);

-- insert into Messages
-- values(default , "It seems u wanna quit or any other shortcut to this thing\nPlease type: help, and see what I can do for u.",5,2);




