# 在位于屏幕中央且宽度合适的方框内打印一个句子
sentence = input("Please input Sentence: ")

screen_width = 150
text_length = len(sentence)
box_width = text_length + 6
left_margin = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+'  + '-' * (box_width-4) +  '+')
print(' ' * left_margin + '| ' + ' ' * text_length    + ' |')
print(' ' * left_margin + '| ' +       sentence   + ' |')
print(' ' * left_margin + '| ' + ' ' * text_length    + ' |')
print(' ' * left_margin + '+'  + '-' * (box_width-4) +  '+')
print()