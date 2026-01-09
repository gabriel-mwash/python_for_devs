cur.execute("select SignedOut from Books where ISBN = ?", isbn)
signedOut = cur.fetchone()[0]
cur.execute("""UPDATE BOOKS SET SignedOut = ?
                WHERE ISBN = ?""", signedOut + 1, isbn)

cur.commit()



# when a patron returns a book, the reverse happens
cur.execute("Select SignedOut from Books where ISBN = ?", isbn)
signedOut = cur.fetchone()[0]
cur.execute("""UPDATE Books SET signedOut = ?
                WHERE ISBN = ?""", signedOut - 1, isbn)

cur.commit()
