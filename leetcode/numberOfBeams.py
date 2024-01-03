# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

def numberOfBeams(bank: list[str]) -> int:
    count = 0
    prev_sec_dev_in_row = 0
    
    for row in bank:
        sec_dev_in_row = 0
        for i in row:
            if i == '1':
                sec_dev_in_row += 1
        if sec_dev_in_row != 0:
            if prev_sec_dev_in_row != 0:
                count += sec_dev_in_row * prev_sec_dev_in_row
            
            prev_sec_dev_in_row = sec_dev_in_row

    return count


bank = ["011001","000000","010100","001000"]
print(numberOfBeams(bank))