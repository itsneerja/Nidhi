import glob
from pathlib import Path
from Nidhi.utils import load_plugins
import logging
from Nidhi import Nidhi

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Nidhi/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
 
bsdk = "» ʙᴏᴛ ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ... !"

print(ramdi)

if __name__ == "__main__":
    Nidhi.run_until_disconnected()
