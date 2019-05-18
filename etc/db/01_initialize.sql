USE kuki;

CREATE TABLE images (
    id   INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    path VARCHAR(255),
    name VARCHAR(255)
);

CREATE TABLE comments (
    id       INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    image_id INT NOT NULL,
    comment  VARCHAR(255),
    FOREIGN KEY comments_image_id_fk (`image_id`) REFERENCES images (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)