CUSTOMER_COUNT = '''
    -- Total customers
    SELECT COUNT(*) AS total_customers
    FROM customers;
'''

CUSTOMER_STATE = '''
   -- How many customers for each state?
    SELECT customers.State, COUNT(DISTINCT customers.State) AS state_total
    FROM customers
    WHERE customers.State  IS NOT NULL
    GROUP BY customers.State
    ORDER BY state_total DESC; 
'''

TOTAL_ARTISTS = '''
    -- total number of artists
    SELECT COUNT(*) AS total_artists
    FROM artists;
'''

TOP_TEN_ARTISTS_TRACKS = '''
    -- What are the top ten Artists with the most tracks?
    SELECT artists.name AS artist, COUNT(tracks.name) AS tot_track
    FROM artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    JOIN tracks ON albums.AlbumId = tracks.AlbumId
    GROUP BY artists.Name
    ORDER BY tot_track DESC
    LIMIT 10;
'''

AVG_TRACK_PER_ARTIST = '''
    -- What's the average number of tracks for all the artists?
    SELECT (SELECT COUNT(*)
            FROM tracks)
            /
            (SELECT COUNT(*)
            FROM artists) AS avg_track_per_artist;
'''
ARTIST_BELOW_OR_ABOVE_AVG_TRACK = '''
    -- Which artists are below or above track average?
    SELECT artists.name AS artist, COUNT(tracks.TrackId) AS tot_track,
    CASE
    WHEN COUNT(tracks.name) < 12 THEN 'BELOW AVERAGE'
    WHEN COUNT(tracks.name) = 12 THEN 'AVERAGE'
    ELSE 'ABOVE AVERAGE'
    END AS below_or_above_avg
    FROM artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    JOIN tracks ON albums.AlbumId = tracks.AlbumId
    GROUP BY artists.name
    ORDER BY artists.name;
'''

ARTIST_BELOW_ABOVE_AVG_ALBUM = '''
    SELECT artists.Name, COUNT(albums.AlbumId) as tot_albums,
    CASE
    WHEN COUNT(albums.AlbumId) < 1 THEN 'BELOW AVERAGE'
    WHEN COUNT(albums.AlbumId) = 1 THEN 'AVERAGE'
    ELSE 'ABOVE AVERAGE'
    END AS below_above_album_avg
    FROM artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    GROUP BY artists.name
    ORDER BY tot_albums DESC;
'''

SONGS_PER_PLAYLIST = '''
    -- How many songs are in each playlist?
    SELECT playlists.name AS playlist, COUNT(tracks.name) AS track_tot
    FROM tracks
    JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    GROUP BY playlists.name;
'''

GENRE_PLAYLIST_TOT = '''
    -- Which genre has the most tracks in playlists?
    SELECT playlists.name AS playlist, genres.Name AS genre, COUNT(tracks.name) AS track_tot
    FROM tracks
    JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    JOIN genres ON tracks.GenreId = genres.GenreId
    GROUP BY genre
    ORDER BY track_tot DESC;
'''

ARTIST_PLAYLIST = '''
   -- Which artist is on the most playlists?
    SELECT artists.Name AS artist, COUNT(playlists.PlaylistId)AS playlist_count
    FROM artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    JOIN tracks ON albums.AlbumId = tracks.AlbumId
    JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    GROUP BY artist
    ORDER BY playlist_count DESC; 
'''
SONG_PLAYLIST = '''
    -- What songs are on the most playlists?
    SELECT tracks.Name AS track, genres.Name AS genre, COUNT(playlists.PlaylistId) AS playlist_tot
    FROM tracks 
    JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
    JOIN genres ON genres.GenreId = tracks.GenreId
    GROUP BY tracks.Name
    ORDER BY playlist_tot DESC;
'''

TRACK_INVOICES = '''
    -- Which track has the most customers?
    SELECT tracks.name AS track, COUNT(customers.CustomerId) AS tot_sales
    FROM tracks
    JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
    JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    JOIN customers ON invoices.CustomerId = customers.CustomerId
    GROUP BY tracks.Name
    ORDER BY tot_sales DESC;
'''


