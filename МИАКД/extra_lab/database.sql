CREATE TABLE videos
(
    id     	INT primary key NOT NULL AUTO_INCREMENT,
    name   	VARCHAR(45)     NOT NULL,
    description VARCHAR(45)     NOT NULL,
    lasting 	INT             NOT NULL
);

create table comments
(
    id           int primary key not null auto_increment,
    text	 VARCHAR(45)     NOT NULL,
    author	 VARCHAR(45)     NOT NULL,
    video_id     int,
    foreign key (video_id) references videos (id) on delete cascade on update cascade
);

insert into videos(name, description, lasting)   
values ('TV-News', 'Fresh february news', 36),
       ('Tennis-2021', 'Tennis championship for young sportsmen', 106),
       ('Oscar-2021', 'The official ceremony of Oscar 2021', 180);

insert into comments(text, author, video_id)
values ('Omg, cool', 'redcat99', 1),
       ('This show is so intense', 'cooldancer10', 2),
       ('The films are unbelievable, really', 'moviefan56', 3),
       ('incredible ceremony', 'teenagerdude', 3);

select * from videos m join comments t on m.id = t.video_id;

-- ЛАБОРАТОРНАЯ 6
-- чтобы быстро отсортировать видео по длительности
create index year on videos(lasting);
-- чтобы быстро найти нужный комментарий для проверки модератором
create index value on comments(text);     
       
                                          