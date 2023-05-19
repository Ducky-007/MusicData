import sqlite3
import queries as q

conn = sqlite3.connect('/Users/cameron/Desktop/Projects/Music/Music.sqlite3')

cur = conn.cursor()


def execute_query(query):
    cur.execute(query)
    return cur.fetchall()

customer_count = execute_query(q.CUSTOMER_COUNT)
state_customer_total = execute_query(q.CUSTOMER_STATE)
total_artists = execute_query(q.TOTAL_ARTISTS)
avg_track_per_artist = execute_query(q.AVG_TRACK_PER_ARTIST)
artist_below_above_avg_track_tot = execute_query(q.ARTIST_BELOW_OR_ABOVE_AVG_TRACK)
artist_below_above_avg_album_tot = execute_query(q.ARTIST_BELOW_ABOVE_AVG_ALBUM)
songs_per_playlist = execute_query(q.SONGS_PER_PLAYLIST)
genre_playlist = execute_query(q.GENRE_PLAYLIST_TOT)
artist_playlist = execute_query(q.ARTIST_PLAYLIST)
song_playlist = execute_query(q.SONG_PLAYLIST)
track_invoices = execute_query(q.TRACK_INVOICES)
