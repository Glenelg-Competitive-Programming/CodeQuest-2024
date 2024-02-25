import sys
sys.stdin = open("test.in", "r")

def solve_test_case():
    s = input()
    highlight = input()
    highlight = highlight.replace("(", "")
    highlight = highlight.replace(")", "")
    highlight = highlight.split(",") # String list

    temp_highlight = [] # int of highlight
    for element in highlight:
        element.split()
        temp_highlight.append(int(element))
    
    print(temp_highlight)

#     image_size = input()


    
#     mask = []
#     for x in range(image_size[0:]):
#         row = input()
#         row = row.split()
#         mask.append(row)

#     image = []
#     for x in range(image_size[0:]):
#         row = input()
#         row = row.split()
#         image.append(row)


# # converts string into int
#     int_image = []
#     for row in image:
#         pixels = []
#         row.replace("(", "")
#         row.replace(")", "")

#         temp = row.split(",")

        
#         for pixel in temp:
#             pixels.append(int(pixel))



    
#     regions_of_interest = []

#     for row in mask:
#         for column in row:
#             if mask[row][column] == '1':
#                 regions_of_interest.append([row, column])
    

#     for element in regions_of_interest:
#         row = element[0]
#         column = element[1]

#         updated_rgb = []
#         updated_rgb[0] = calc_red_highlight(image[row][column][0], int(highlight[0]))
#         updated_rgb[1] = calc_red_highlight(image[row][column][1], int(highlight[1]))
#         updated_rgb[2] = calc_red_highlight(image[row][column][2], int(highlight[2]))
        
#         image[row][column] = updated_rgb # come back to this


    
#     visited = regions_of_interest

#     for element in regions_of_interest:
#         row = element[0]
#         column = element[1]       



def calc_red_highlight(pixel_red, highlight_red):
    return 0.5 * pixel_red + 0.5  * highlight_red

        




    print()

for _ in range (int(input())):
    solve_test_case()