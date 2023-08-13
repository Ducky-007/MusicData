# Music Database

This is a mock music database

[music_schema.pdf](https://github.com/Ducky-007/MusicData/files/11781959/music_schema.pdf)


☝🏻 See music_schema.pdf for visualisation

Employees table stores employees data such as employee id, last name, first name, etc. It also has a field named ReportsTo to specify who reports to whom

Customers table stores customers data

Invoices & invoice_items tables: these two tables store invoice data. The invoices table stores invoice header data and the invoice_items table stores the invoice line items data

Artists table stores artists data. It is a simple table that contains only the artist id and name

Albums table stores data about a list of tracks. Each album belongs to one artist. However, one artist may have multiple albums

Media_types table stores media types such as MPEG audio and AAC audio files

Genres table stores music types such as rock, jazz, metal, etc

Tracks table stores the data of songs. Each track belongs to one album
    
Playlists & playlist_track tables: playlists table store data about playlists. Each playlist contains a list of tracks. Each track may belong to multiple playlists. The relationship between the playlists table and tracks table is many-to-many. The playlist_track table is used to reflect this relationship

# Stakeholder Questions Queries Answered:

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

What genres are on the most playlists?

Which track has the most customers?

# Conclusion

Total Customers: 99

See csv file for customers for each state

Total Artists: 275

Top Ten Artists with the Most Tracks:

Iron Maiden,
U2,
Led Zeppelin,
Metallica,
Lost,
Deep Purple,
Pearl Jam,
Lenny Kravitz,
Various Artists,
The Office

Average tracks per Artist: 12

See csv for each artst album totals being above or below average

Average Album per Artist: 1

Music and 90's Music genres are being used in most playlists

Track with the most customers: The Trooper

# Conclusion
Market and learn more from Iron Maiden and classic rock users

Get more customers to use Music Database

Get more artists loaded into the Database so a wider net can be spread to attract more users
