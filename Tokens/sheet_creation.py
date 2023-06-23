import utils

def create_sheets(imgs):
  return (generate_sheet(chunk) for chunk in utils.split(imgs,6*4))
def generate_sheet(imgs):
  assert len(imgs)<=6*4
  rows = [utils.img_concat(chunk) for chunk in utils.split(imgs,4)]
  return utils.img_concat(rows,horizontal=False)