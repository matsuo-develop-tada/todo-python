-- Todo一覧
DELETE FROM test_database.todo WHERE id_todo >= 1;
INSERT INTO test_database.todo (id_todo, content, color_code, checked, dt_do, dt_create, dt_update)
VALUES (1, '買い物に行く', '#FFBCD3', 0, '2021-01-10', '2021-01-01', '2021-01-02');
INSERT INTO test_database.todo (id_todo, content, color_code, checked, dt_do, dt_create, dt_update)
VALUES (2, '洗濯をする', '#D2CCFF', 0, '2021-02-10', '2021-02-01', '2021-02-02');
INSERT INTO test_database.todo (id_todo, content, color_code, checked, dt_do, dt_create, dt_update)
VALUES (3, '郵便局に行く', '#9EFF9A', 0, '2021-03-10', '2021-03-01', '2021-03-02');
INSERT INTO test_database.todo (id_todo, content, color_code, checked, dt_do, dt_create, dt_update)
VALUES (4, '部屋を片付ける', '#F8F6B1', 0, '2021-04-10', '2021-04-01', '2021-04-02');

-- カラー一覧
DELETE FROM test_database.color WHERE id_color >= 1;
INSERT INTO test_database.color (id_color, color_code) VALUES (1, '#ffffff');
INSERT INTO test_database.color (id_color, color_code) VALUES (2, '#ff0000');
INSERT INTO test_database.color (id_color, color_code) VALUES (3, '#00ff00');
INSERT INTO test_database.color (id_color, color_code) VALUES (4, '#0000ff');
INSERT INTO test_database.color (id_color, color_code) VALUES (5, '#ffff00');
INSERT INTO test_database.color (id_color, color_code) VALUES (6, '#ff00ff');
INSERT INTO test_database.color (id_color, color_code) VALUES (7, '#00ffff');
INSERT INTO test_database.color (id_color, color_code) VALUES (8, '#FFBCD3');
INSERT INTO test_database.color (id_color, color_code) VALUES (9, '#D2CCFF');
INSERT INTO test_database.color (id_color, color_code) VALUES (10, '#9EFF9A');
INSERT INTO test_database.color (id_color, color_code) VALUES (11, '#F8F6B1');