CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `date`	TEXT NOT NULL,
    `mood_id`	INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL
);


INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Angry");
INSERT INTO `Moods` VALUES (null, "Ok");
INSERT INTO `Moods` VALUES (null, "Hopeful");
INSERT INTO `Moods` VALUES (null, "Excited");
INSERT INTO `Moods` VALUES (null, "Humorous");
INSERT INTO `Moods` VALUES (null, "Reflective");
INSERT INTO `Moods` VALUES (null, "Existential");

INSERT INTO `Entries` VALUES (null, "Python", "Python is great so far and would have been super helpful when creating my client captone.", "Mon Apr 11 2022 10:10:47", 5);
INSERT INTO `Entries` VALUES (null, "Javascript", "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.", "Wed Sep 15 2021 10:10:47", 1);
INSERT INTO `Entries` VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", "Wed Sep 15 2021 10:11:33", 4);
INSERT INTO `Entries` VALUES (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks.", "Wed Sep 15 2021 10:13:11", 3);
INSERT INTO `Entries` VALUES (null, "Javascript", "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.", "Wed Sep 15 2021 10:14:05", 3);



SELECT * FROM Entries

SELECT * FROM Entries
WHERE Entries.id = 3