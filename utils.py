import qrcode

def make_qr(link, user_id):
    path = f"{user_id}.png"
    img = qrcode.make(link)
    img.save(path)
    return path