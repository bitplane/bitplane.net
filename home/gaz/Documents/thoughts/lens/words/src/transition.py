#!/usr/bin/env python3
import sys
import re
import random
import time
import argparse
import math
from functools import partial

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

def wipe(src, dst, transition_fn, frames=20, delay=0.05):
    _, _, width, height = pad_images(src, dst)
    mask = [[False]*width for _ in range(height)]
    current = [row[:] for row in src]

    print('\033[2J', end='')  # Clear screen once

    for frame in range(frames+1):
        t = frame / frames
        for y in range(height):
            for x in range(width):
                if not mask[y][x]:
                    current[y][x], transitioned = transition_fn(src, dst, x, y, t)
                    mask[y][x] = transitioned

        print('\033[H', end='')  # Cursor home
        for line in current:
            print(''.join(line))
        time.sleep(delay)

def random_transition(src, dst, x, y, t):
    random.seed(f"{x},{y}")
    if random.random() < t:
        return dst[y][x], True
    return src[y][x], False

def distance(x1, y1, x2, y2):
    return math.hypot(x1 - x2, (y1 - y2)*2)

def circle_transition(src, dst, x, y, t, cx, cy, max_dist, invert=False):
    dist = distance(x, y, cx, cy)
    threshold = t * max_dist
    if invert:
        condition = dist > (max_dist - threshold)
    else:
        condition = dist < threshold

    if condition:
        return dst[y][x], True
    return src[y][x], False

def main():
    parser = argparse.ArgumentParser(description='ANSI Art Transitions')
    parser.add_argument('source', help='Source ANSI art file')
    parser.add_argument('dest', help='Destination ANSI art file')
    parser.add_argument('-t', '--type', choices=['random', 'circle_grow', 'circle_shrink'], default='random', help='Transition type')
    parser.add_argument('-f', '--frames', type=int, default=20, help='Number of frames')
    parser.add_argument('-d', '--delay', type=float, default=0.05, help='Frame delay in seconds')

    args = parser.parse_args()

    src_img = parse_ansi_file(args.source)
    dst_img = parse_ansi_file(args.dest)
    _, _, width, height = pad_images(src_img, dst_img)

    max_dist = distance(0, 0, width / 2, height / 2) + 1
    cx, cy = width / 2, height / 2

    transitions = {
        'random': random_transition,
        'circle_grow': partial(circle_transition, cx=cx, cy=cy, max_dist=max_dist, invert=False),
        'circle_shrink': partial(circle_transition, cx=cx, cy=cy, max_dist=max_dist, invert=True),
    }

    wipe(src_img, dst_img, transitions[args.type], frames=args.frames, delay=args.delay)

if __name__ == '__main__':
    main()
