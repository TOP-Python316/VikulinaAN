SELECT DISTINCT hair, eye
FROM MarvelCharacters
WHERE hair IS NOT NULL AND eye IS NOT NULL
ORDER BY hair, eye;
