# rpsgame

# Prerequisites
    + Anaconda 3.7+
    + Python 3.7+
    + Pip

# To install game, fork rpsgame repository from GitHub, available at https://github.com/NoahBarratt/rpsgame , and download remote copy onto local computer

# To create and activate an Anaconda virtual environment specific to the game, use the command: 
    conda create -n my-game-env python=3.8 # (only use this the first time), 
# Then activate environment with command: 
    conda activate my-game-env

# After downloading rpsgame from GitHub to Desktop, open Terminal, activate game-specific environment as instructed above, type: 
    cd Desktop/GitHub/rpsgame 
# Then press enter, then type: 
    python game.py 
# Then press enter and follow prompts within game

# To change player name, first install package within game-specific Anaconda virtual environment with the command: 
    pip install python-dotenv , 
# Then create file titled .env on VS Code or preferred text editor, write 
    PLAYER_NAME="Desired Name" 
# in file and save file within the folder titled "rpsgame"