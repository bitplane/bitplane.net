#!/usr/bin/env python3
import sys
import re
import random
import time

ANSI_ESCAPE = re.compile(r'(\x1B\[[0-9;]*[mK])')

def parse_ansi_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            parts = ANSI_ESCAPE.split(line.rstrip('\n'))
            current_seq = ''
            parsed_line = []
            for part in parts:
                if ANSI_ESCAPE.match(part):
                    current_seq = part
                else:
                    for char in part:
                        parsed_line.append(current_seq + char)
            lines.append(parsed_line)
    return lines

def pad_images(img1, img2):
    height = max(len(img1), len(img2))
    width = max(max(len(line) for line in img1), max(len(line) for line in img2))

    for img in (img1, img2):
        for line in img:
            line.extend([' '] * (width - len(line)))
        while len(img) < height:
            img.append([' '] * width)

    return img1, img2, width, height

def transition(img1, img2, frames=20, delay=0.05):
    _, _, width, height = pad_images(img1, img2)
    positions = [(y, x) for y in range(height) for x in range(width)]
    random.shuffle(positions)

    step = len(positions) // frames

    print('\033[2J', end='')  # clear screen once
    current_frame = [row[:] for row in img1]

    for i in range(0, len(positions) + step, step):
        for y, x in positions[:i]:
            current_frame[y][x] = img2[y][x]

        print('\033[H', end='')  # cursor home
        for line in current_frame:
            print(''.join(line))
        time.sleep(delay)

def main(file1, file2):
    img1 = parse_ansi_file(file1)
    img2 = parse_ansi_file(file2)
    transition(img1, img2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} file1.ans file2.ans')
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
