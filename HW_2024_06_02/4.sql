SELECT name, year
FROM MarvelCharacters
WHERE eye = 'blue' AND hair = 'blond' AND ((year >= 1960 AND year < 1970) OR (year >= 1980 AND year < 1990))
ORDER BY year;
