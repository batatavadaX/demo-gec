# importing folder.
import sys
sys.path.insert(
    1, 
    'web'
)

# importing env & main app.
import os

# import dotenv
from web import horse
HOST=os.environ.get("HOST", "0.0.0.0")
PORT=int(os.environ.get("PORT", 6969))

#run a standard server.
if __name__ == "__main__":
	
	horse.run(
	    host=HOST,
	    port=PORT,
	    debug=True
	)
