import shutil
import datetime

def create_backup():
    name = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
    shutil.copyfile("berserk.db", name)
    return name
