from PIL import Image
from typing import cast
from rgb_types import RGBStream


THRESHOLD: int = 130


def binarify(
        input_path: str,
        output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size
    out_stream: list[int] = []  # 0 = black, 255 = white
    green: int
    for (_, green, _) in in_stream:
        out_stream.append(0 if green < THRESHOLD else 255)
    out_img: Image.Image = Image.new('1', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)

if __name__ == '__main__':
    binarify('images/woman.png',
             'images/woman_bnw.png')
    print('Done!')
