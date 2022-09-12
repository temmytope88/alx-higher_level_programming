-- select rom multiple table using join
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'comedy' ORDER BY tv_shows.title;
