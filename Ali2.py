Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> submit_btn=Button(root,text="Add Record to Database", command=submit)
... submit_btn.grind(row=6,
...                  column=0,
...                  columnspan=2,
...                  pady=10,
...                  pad=10,
...                  ipadx=100)
... 
... query_btn=Button(root,text="Show Records", command=query)
... query_btn.grind(row=7,
...                 column=0,
...                 columnspan=2,
...                 pady=10,
...                 pad=10,
...                 ipadx=137)
