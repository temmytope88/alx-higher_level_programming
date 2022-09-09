-- select rom multiple table using join
select tv_genres.name, Count(tv_show_genres.genre_id)
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
