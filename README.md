Music Database

This is a mock music database

There are 11 tables in the chinook sample database.

See schema for visualisation.

    employees table stores employees data such as employee id, last name, first name, etc. It also has a field named ReportsTo to specify who reports to whom.
    
    customers table stores customers data.
    
    invoices & invoice_items tables: these two tables store invoice data. The invoices table stores invoice header data and the invoice_items table stores the invoice line items data.
    
    artists table stores artists data. It is a simple table that contains only the artist id and name.
    
    albums table stores data about a list of tracks. Each album belongs to one artist. However, one artist may have multiple albums.
    
    media_types table stores media types such as MPEG audio and AAC audio files.
    
    genres table stores music types such as rock, jazz, metal, etc.
    
    tracks table stores the data of songs. Each track belongs to one album.
    
    playlists & playlist_track tables: playlists table store data about playlists. Each playlist contains a list of tracks. Each track may belong to multiple playlists. The relationship between the playlists table and tracks table is many-to-many. The playlist_track table is used to reflect this relationship.

Questions queries answer:

How many customers are there currently?

How many customers for each state?

How many artists are there currently?

What are the ten Artists with the most tracks?

What's the average number of tracks for all the artists?

Which artists are below or above track average?

Which artists have more albums than the average number of albums for all artists?

How many songs are in each playlist?

Which genre has the most tracks in playlists?

Which artist is on the most playlists?

What songs are on the most playlists?

Which track has the most invoices?
