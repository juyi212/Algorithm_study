import sys
# 가장 큰 거 기준으로 왼, 오
# 가장 큰 거 다음으로 큰 거 기준

w, h = map(int, sys.stdin.readline().split()) # 세로 , 가로
blocks = list(map(int, sys.stdin.readline().split()))

max_block = blocks.index(max(blocks))
left_rains = 0
right_rains = 0
total = 0

left_block = blocks[:max_block]
right_block = blocks[max_block+1:]

left_max_block = max_block
right_max_block = max_block

if len(left_block) > 0:
    while left_max_block > 0 and len(left_block) > 0:
        next_max = max(left_block)
        left_max_block = left_block.index(next_max)
        for i in range(left_max_block+1, len(left_block)):
            left_rains += blocks[left_max_block] - blocks[i]

        next_max_index = blocks.index(next_max)
        left_block = blocks[:next_max_index]

if len(right_block) > 0:
    while right_max_block < len(blocks) and len(right_block) > 0:
        next_max = max(right_block)
        right_max_block = right_block.index(next_max)
        for i in range(0, right_max_block):
            right_rains += right_block[right_max_block] - right_block[i]
        right_block = right_block[right_max_block+1:]

print(left_rains+right_rains)
