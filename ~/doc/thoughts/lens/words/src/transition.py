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

def get_dimensions(img):
    """Return (width, height) of an ANSI image."""
    height = len(img)
    width = max(len(line) for line in img) if img else 0
    return width, height

def pad_images(img1, img2):
    """Pads two images to the same width and height."""
    width1, height1 = get_dimensions(img1)
    width2, height2 = get_dimensions(img2)

    width = max(width1, width2)
    height = max(height1, height2)

    for img in (img1, img2):
        for line in img:
            line.extend([' '] * (width - len(line)))
        while len(img) < height:
            img.append([' '] * width)

    return img1, img2, width, height

def distance(x1, y1, x2, y2):
    """Gets the distance between two points on a grid where cells are 2x higher than wide"""
    return math.hypot(x1 - x2, (y1 - y2) * 2)

def copy(src):
    """Duplicate an image"""
    return [row[:] for row in src]

def apply_transitions(src, dst, funcs, t):
    """Applies all transitions at each pixel, merging effects instead of replacing."""
    height, width = len(src), len(src[0])
    frame = copy(src)

    for y in range(height):
        for x in range(width):
            pixel = src[y][x]
            for func in funcs:
                pixel = func(src, dst, x, y, t, previous=pixel)
            frame[y][x] = pixel

    return frame

def transition(src, dst, funcs, frames=20, delay=0.05):
    _, _, width, height = pad_images(src, dst)

    for frame in range(frames + 1):
        t = frame / frames
        current = apply_transitions(src, dst, funcs, t)

        print('\033[H', end='')  # Cursor home
        for line in current:
            print(''.join(line))
        time.sleep(delay)

def random_transition(src, dst, x, y, t, previous):
    random.seed(f"{x},{y}")
    return dst[y][x] if random.random() < t else previous

def circle_transition(src, dst, x, y, t, previous, cx, cy, max_dist, invert=False):
    dist = distance(x, y, cx, cy)
    threshold = t * max_dist
    condition = dist > (max_dist - threshold) if invert else dist < threshold
    return dst[y][x] if condition else previous

def main():
    parser = argparse.ArgumentParser(description='ANSI Art Transitions')
    parser.add_argument('source', help='Source ANSI art file')
    parser.add_argument('dest', help='Destination ANSI art file')
    parser.add_argument('-t', '--type', action='append', choices=['random', 'circle_grow', 'circle_shrink'], help='Transition type(s)')
    parser.add_argument('-f', '--frames', type=int, default=20, help='Number of frames')
    parser.add_argument('-d', '--delay', type=float, default=0.05, help='Frame delay in seconds')

    args = parser.parse_args()

    if not args.type:
        args.type = ['random']

    src_img = parse_ansi_file(args.source)
    dst_img = parse_ansi_file(args.dest)
    _, _, width, height = pad_images(src_img, dst_img)

    max_dist = distance(0, 0, width / 2, height / 2) + 1
    cx, cy = width / 2, height / 2

    available_transitions = {
        'random': partial(random_transition),
        'circle_grow': partial(circle_transition, cx=cx, cy=cy, max_dist=max_dist, invert=False),
        'circle_shrink': partial(circle_transition, cx=cx, cy=cy, max_dist=max_dist, invert=True),
    }

    transition_fns = [available_transitions[t] for t in args.type]

    transition(src_img, dst_img, transition_fns, frames=args.frames, delay=args.delay)

if __name__ == '__main__':
    main()
