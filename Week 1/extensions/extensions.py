#getting input from user
filename = input("File Name: ")
new_filename = filename.lower()
if '.gif' in new_filename:
    print("image/gif")
elif ".png" in new_filename:
    print("image/png")
elif ".jpg" in new_filename:
    print("image/jpeg")
elif ".jpeg" in new_filename:
    print("image/jpeg")

#If pdf or zip, print "application/type"
elif ".pdf" in new_filename:
    print("application/pdf")
elif ".zip" in new_filename:
    print("application/zip")
elif ".txt" in new_filename:
    print("text/plain")
#otherwise
else:
    print("application/octet-stream")
